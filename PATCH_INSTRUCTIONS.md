# Patch: resolve duplicate-application decision and test copyable examples

Apply this ZIP **on top of the repository already merged to `main`**. It does NOT include or overwrite `openapi.yaml`, preserving your recent GitHub CI fixes.

## Changes
- TB-005 is approved **only as a fictional v1.1 contract rule**: duplicate candidate/job submissions yield 409; withdrawn applications, races, retries remain open.
- EN/VI release notes and decision register agree on that scope.
- Markdown JSON examples now carry `doc-test` classification: request / response / excluded version comparison with reason.
- New static validator checks every documented curl command against method/path/query/auth/request schema and every JSON block against its annotated response/request schema; rejects unclassified blocks.
- 5 negative/positive regression tests, run in GitHub Actions.

## Apply in Windows
1. Download and extract this patch ZIP.
2. Open your existing VS Code repository folder and confirm `git status` is clean.
3. Copy the extracted `docs`, `scripts`, `tests`, `.github`, and `README*` into that **existing** repo, allowing overwrite. Do **not** copy the parent folder and do **not** delete `.git`.
4. Install dependencies once: `python -m pip install -r requirements-docs.txt`.
5. Run:
   `python scripts/audit_docs.py`
   `python scripts/check_openapi.py`
   `python scripts/check_markdown_examples.py`
   `python -m unittest discover -s tests -p "test_*.py"`
6. Push through a PR or your normal Git flow. New CI must pass before merge.

## Verification scope
Checks are **static contract validation only**. They do not execute curl, start Prism, verify authentication/role checks, test duplicate detection, or prove a production backend exists. The 4 excluded blocks are partial migration examples for a future v2 contract and are still JSON-syntax checked.
