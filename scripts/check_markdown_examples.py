#!/usr/bin/env python3
"""Statically validate every Markdown JSON and curl example against OpenAPI.

This validates syntax, documented routes, request/response shapes, selected
parameters, and auth-header presence; it does NOT execute HTTP requests or
assert runtime behavior. Every JSON fence requires an explicit doc-test marker.
"""
import json
import re
import shlex
import sys
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

import yaml
from jsonschema import Draft4Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
API = yaml.safe_load((ROOT / 'openapi.yaml').read_text(encoding='utf-8'))
FENCES = re.compile(r'^```([^\n]*)\n(.*?)^```\s*$', re.MULTILINE | re.DOTALL)
MARKER = re.compile(r'<!--\s*doc-test:\s*(request|response|skip)\s+([^\n]*?)\s*-->\s*$', re.IGNORECASE)
ERRORS = []
COUNTS = {'json': 0, 'curl': 0, 'skip': 0}


def deref(obj):
    seen = set()
    while isinstance(obj, dict) and '$ref' in obj:
        pointer = obj['$ref']
        if pointer in seen or not pointer.startswith('#/'):
            raise ValueError(f'invalid/cyclic reference: {pointer}')
        seen.add(pointer)
        value = API
        for key in pointer[2:].split('/'):
            value = value[key.replace('~1', '/').replace('~0', '~')]
        obj = value
    return obj


def json_schema(schema):
    if isinstance(schema, list):
        return [json_schema(x) for x in schema]
    if not isinstance(schema, dict):
        return schema
    schema = deref(schema)
    result = {k: json_schema(v) for k, v in schema.items() if k != 'nullable'}
    if schema.get('nullable') and 'type' in result:
        ty = result['type']
        result['type'] = [ty, 'null'] if isinstance(ty, str) else [*ty, 'null']
    return result


def verify_payload(payload, schema, context):
    for err in Draft4Validator(json_schema(schema), format_checker=FormatChecker()).iter_errors(payload):
        ERRORS.append(f'{context}: schema violation: {err.message} at {list(err.absolute_path)}')


def route(method, path):
    for template, operations in API['paths'].items():
        pattern = re.sub(r'\{[^/]+\}', r'[^/]+', re.escape(template).replace(r'\{', '{').replace(r'\}', '}'))
        if re.fullmatch(pattern, path) and method.lower() in operations:
            return template, operations[method.lower()]
    return None, None


def find_operation(method, target, context):
    # Map a documented URL to an actual API operation, stripping only the
    # configured server base paths (never guessing an arbitrary /v1 prefix).
    parsed = urlsplit(target)
    if parsed.scheme not in ('http', 'https') or not parsed.netloc:
        ERRORS.append(f'{context}: curl URL must be an absolute http(s) URL: {target}')
        return None, None, None
    matching = []
    for server in API.get('servers', []):
        base = urlsplit(server['url'])
        basepath = base.path.rstrip('/')
        if (parsed.scheme, parsed.netloc) != (base.scheme, base.netloc):
            continue
        if basepath and not (parsed.path == basepath or parsed.path.startswith(basepath + '/')):
            continue
        matching.append(parsed.path[len(basepath):] or '/')
    if not matching:
        ERRORS.append(f'{context}: URL not covered by OpenAPI servers: {target}')
        return None, None, None
    for path in matching:
        template, operation = route(method, path)
        if operation is not None:
            return template, operation, parsed
    ERRORS.append(f'{context}: no {method} operation for URL {target}')
    return None, None, None


def check_curl(code, context):
    code = re.sub(r'\\\s*\n', ' ', code).strip()
    try:
        tokens = shlex.split(code, posix=True)
    except ValueError as exc:
        ERRORS.append(f'{context}: invalid curl shell quoting: {exc}')
        return
    if not tokens or tokens[0] != 'curl':
        ERRORS.append(f'{context}: bash example must start with curl or be a recognized non-curl tooling command')
        return
    method, headers, data, url, i = None, {}, None, None, 1
    while i < len(tokens):
        token = tokens[i]
        if token in ('-i', '--include', '-s', '--silent', '-S', '--show-error', '-L', '--location'):
            i += 1; continue
        if token in ('-X', '--request', '-H', '--header', '-d', '--data', '--data-raw', '--url'):
            if i + 1 >= len(tokens):
                ERRORS.append(f'{context}: missing value for {token}'); return
            value = tokens[i + 1]
            if token in ('-X', '--request'): method = value.upper()
            elif token in ('-H', '--header'):
                if ':' not in value:
                    ERRORS.append(f'{context}: malformed header: {value}')
                else:
                    name, val = value.split(':', 1); headers[name.lower().strip()] = val.strip()
            elif token in ('-d', '--data', '--data-raw'): data = value
            else: url = value
            i += 2; continue
        if token.startswith('-'):
            ERRORS.append(f'{context}: unsupported curl flag {token}; add parser support rather than silently skip')
        elif url is None:
            url = token
        else:
            ERRORS.append(f'{context}: extra curl positional argument {token}')
        i += 1
    if not url:
        ERRORS.append(f'{context}: curl URL missing'); return
    method = method or ('POST' if data is not None else 'GET')
    template, operation, parsed = find_operation(method, url, context)
    if operation is None: return
    if operation.get('security', API.get('security', [])) and 'authorization' not in headers:
        ERRORS.append(f'{context}: missing Authorization header for secured {method} {template}')
    if parsed:
        actual = parse_qs(parsed.query, keep_blank_values=True)
        params = [deref(x) for x in operation.get('parameters', [])]
        declared = {x['name']: x for x in params if x.get('in') == 'query'}
        for name, values in actual.items():
            if name not in declared:
                ERRORS.append(f'{context}: undocumented query parameter {name} for {method} {template}')
                continue
            schema = declared[name].get('schema', {})
            for value in values:
                try:
                    if schema.get('type') == 'integer': value = int(value)
                    elif schema.get('type') == 'number': value = float(value)
                    elif schema.get('type') == 'boolean':
                        if value not in ('true', 'false'): raise ValueError('invalid boolean')
                        value = value == 'true'
                except ValueError:
                    ERRORS.append(f'{context}: invalid query value for {name}'); continue
                verify_payload(value, schema, f'{context} query {name}')
    body = operation.get('requestBody')
    if body and body.get('required') and data is None:
        ERRORS.append(f'{context}: required request body missing')
    if data is not None:
        if not body:
            ERRORS.append(f'{context}: operation has no request body'); return
        try: payload = json.loads(data)
        except json.JSONDecodeError as exc:
            ERRORS.append(f'{context}: curl -d is not valid JSON: {exc}'); return
        ctype = headers.get('content-type', '').split(';')[0].strip()
        if ctype not in body.get('content', {}):
            ERRORS.append(f'{context}: request Content-Type {ctype!r} not defined by operation'); return
        verify_payload(payload, body['content'][ctype]['schema'], f'{context} request {method} {template}')
    COUNTS['curl'] += 1


def check_json(text, marker, context):
    if not marker:
        ERRORS.append(f'{context}: JSON block missing preceding <!-- doc-test: ... --> annotation'); return
    kind, rest = marker.group(1).lower(), marker.group(2)
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        ERRORS.append(f'{context}: invalid JSON: {exc}')
        return
    if kind == 'skip':
        if len(rest.split()) < 5:
            ERRORS.append(f'{context}: skip requires a substantive reason')
        COUNTS['skip'] += 1; return
    parts = rest.split()
    expected = 2 if kind == 'request' else 3
    if len(parts) != expected:
        ERRORS.append(f'{context}: expected {kind} METHOD PATH' + (' STATUS' if kind == 'response' else '')); return
    method, path = parts[:2]
    template, operation = route(method, path)
    if operation is None or template != path:
        ERRORS.append(f'{context}: annotation references unknown {method} {path}'); return
    if kind == 'request':
        content = operation.get('requestBody', {}).get('content', {}).get('application/json', {})
    else:
        status = parts[2]
        response = operation.get('responses', {}).get(status)
        if response is None:
            ERRORS.append(f'{context}: undocumented response {status} for {method} {path}'); return
        content = deref(response).get('content', {})
        # Error responses use application/problem+json.
        content = content.get('application/json', content.get('application/problem+json', {}))
    if 'schema' not in content:
        ERRORS.append(f'{context}: no schema for annotated {kind}'); return
    verify_payload(payload, content['schema'], context)
    COUNTS['json'] += 1


def check_file(path):
    content = path.read_text(encoding='utf-8')
    for match in FENCES.finditer(content):
        language, code = match.group(1).strip().lower(), match.group(2)
        if language not in ('json', 'bash', 'sh', 'shell'): continue
        lineno = content.count('\n', 0, match.start()) + 1
        context = f'{path.relative_to(ROOT)}:{lineno}'
        if language == 'json':
            preceding = content[:match.start()].rstrip()
            marker = MARKER.search(preceding)
            check_json(code, marker, context)
        else:
            # Local mock launch commands aren't HTTP examples.
            if re.match(r'^\s*npx\s+@stoplight/prism-cli\s+mock\b', code):
                continue
            check_curl(code, context)


def main():
    for path in sorted((ROOT / 'docs').rglob('*.md')):
        check_file(path)
    print(f"Markdown examples: {COUNTS['curl']} curl commands, {COUNTS['json']} JSON schema checks, {COUNTS['skip']} explicitly excluded version-comparison fragments")
    if ERRORS:
        for error in ERRORS: print('ERROR:', error)
        return 1
    print('All inspected Markdown examples pass static OpenAPI contract validation (no server execution).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
