#!/usr/bin/env python3
"""Standard-library, read-only Markdown quality audit for the repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', 'node_modules', '.venv', 'venv'}
problems = []
files = [p for p in ROOT.rglob('*.md') if not set(p.relative_to(ROOT).parts) & SKIP]

for p in files:
    content = p.read_text(encoding='utf-8-sig')
    rel = p.relative_to(ROOT)
    fences = [line for line in content.splitlines() if re.match(r'^\s*(`{3,}|~{3,})', line)]
    active = None
    for line in fences:
        m = re.match(r'^\s*(`{3,}|~{3,})', line)
        mark = m.group(1)
        if active is None:
            active = mark
        elif mark[0] == active[0] and len(mark) >= len(active):
            active = None
    if active is not None:
        problems.append(f'{rel}: unmatched Markdown code fence')
    for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
        target = target.split('#', 1)[0].strip().split(' ',1)[0]
        if not target or target.startswith(('https://', 'http://', 'mailto:', '/')):
            continue
        if not (p.parent / target).exists():
            problems.append(f'{rel}: missing relative link: {target}')
    if re.search(r'\b(TODO|FIXME|lorem ipsum)\b', content, re.IGNORECASE):
        problems.append(f'{rel}: editorial placeholder marker (review manually)')

print(f'Scanned {len(files)} Markdown files')
if problems:
    print('\n'.join('ERROR: ' + x for x in problems))
    sys.exit(1)
print('Markdown structural checks passed')
