# Documentation contribution workflow

TalentBridge documentation follows a docs-as-code workflow.

## 1. Create a branch

Example:

```bash
git checkout -b docs/update-application-errors
```

## 2. Update the source of truth

If API behavior changes, update `openapi.yaml` before or together with
the related developer documentation.

Documentation must not intentionally contradict the API contract.

## 3. Run the mock API

```bash
npx @stoplight/prism-cli mock openapi.yaml
```

## 4. Verify examples

Run any affected curl examples against the mock server.

Check:

- method and path
- parameters
- request body
- response status
- response schema
- documented error behavior

## 5. Review terminology

Check the documentation against `docs/style-guide.md`.

## 6. Document API changes

For externally visible API changes, update:

- `CHANGELOG.md`
- release notes
- migration documentation if the change is breaking

## 7. Open a pull request

The pull request should explain:

- what changed
- why it changed
- which API operations are affected
- whether the change is breaking
- how the documentation was verified

Documentation changes are reviewed before merge in the same way as
code changes.
