#!/usr/bin/env python3
"""Validate local OpenAPI $refs and representative examples (not backend behavior)."""
import copy
import sys
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft4Validator, FormatChecker
except ImportError:
    sys.exit('Missing dependencies. Run: python -m pip install -r requirements-docs.txt')

ROOT = Path(__file__).resolve().parents[1]
API = yaml.safe_load((ROOT / 'openapi.yaml').read_text(encoding='utf-8'))
problems = []
checked = 0


def resolve(pointer):
    if not pointer.startswith('#/'):
        raise ValueError(f'External/invalid reference: {pointer}')
    node = API
    for segment in pointer[2:].split('/'):
        node = node[segment.replace('~1', '/').replace('~0', '~')]
    return node


def schema_for_validation(schema):
    """Convert OAS3 nullable and local refs to JSON Schema draft 4 constructs."""
    if isinstance(schema, list):
        return [schema_for_validation(value) for value in schema]
    if not isinstance(schema, dict):
        return schema
    if '$ref' in schema:
        return schema_for_validation(resolve(schema['$ref']))
    result = {key: schema_for_validation(value) for key, value in schema.items() if key != 'nullable'}
    if schema.get('nullable'):
        typ = result.get('type')
        if isinstance(typ, str):
            result['type'] = [typ, 'null']
        elif isinstance(typ, list):
            result['type'] = [*typ, 'null']
    return result


def validate_example(example, schema, context):
    global checked
    checker = Draft4Validator(schema_for_validation(schema), format_checker=FormatChecker())
    for error in checker.iter_errors(example):
        problems.append(f'{context}: {error.message} at {list(error.absolute_path)}')
    checked += 1


for path, path_item in API['paths'].items():
    for method, operation in path_item.items():
        if method not in ('get', 'post', 'patch', 'put', 'delete'):
            continue
        location = f'{method.upper()} {path}'
        for response_code, response in operation.get('responses', {}).items():
            if '$ref' in response:
                try:
                    response = resolve(response['$ref'])
                except (KeyError, ValueError) as error:
                    problems.append(f'{location} {response_code}: {error}')
                    continue
            for media_type, content in response.get('content', {}).items():
                schema = content.get('schema')
                if not schema:
                    continue
                samples = []
                if 'example' in content:
                    samples.append(('example', content['example']))
                for name, item in content.get('examples', {}).items():
                    if 'value' in item:
                        samples.append((name, item['value']))
                for label, value in samples:
                    validate_example(value, schema, f'{location} {response_code} {media_type} {label}')
        for media_type, content in operation.get('requestBody', {}).get('content', {}).items():
            if 'example' in content and 'schema' in content:
                validate_example(content['example'], content['schema'], f'{location} request {media_type}')

# Contract/docs consistency checks: prevent missing endpoints in a human reference.
reference = (ROOT / 'docs/en/applications-api.md').read_text()
for endpoint in ('POST /jobs/{jobId}/applications', 'GET /jobs/{jobId}/applications', 'PATCH /applications/{applicationId}'):
    if endpoint not in reference:
        problems.append(f'Applications reference missing {endpoint}')

print(f'Validated {checked} OpenAPI examples and 3 applications-reference operations')
if problems:
    for issue in problems:
        print('ERROR:', issue)
    sys.exit(1)
print('OpenAPI example checks passed (mock contract only; no backend tested)')
