# Documentation contribution workflow

TalentBridge is a fictional docs-as-code case study. This workflow is a recommended process, not evidence of reviews by a real engineering team.

## 1. Create a documentation branch

```bash
git switch -c docs/update-application-errors
```

## 2. Update the API contract and both languages

When documented API behavior changes, update `openapi.yaml` and the corresponding pages under `docs/en/` and `docs/vi/`. Preserve names, statuses, examples, and the intent of both translations. Consult the [English style guide](docs/style-guide.md) and [Vietnamese style guide](docs/vi/style-guide.md). If behavior is undefined, record a question instead of inventing a rule.

## 3. Contract and documentation verification

Prism can demonstrate selected examples generated from the OpenAPI contract. Check the OpenAPI structure, request/response shapes, example payloads, documented response statuses, Markdown links, and bilingual consistency. Run:

```bash
npx @stoplight/prism-cli mock openapi.yaml
```

Then try the local scripts described in [examples/README.md](examples/README.md). The mock is useful for inspecting examples, but a mocked status is not proof that business logic enforces it.

## 4. Runtime/backend verification (out of scope)

Real authentication, authorization, persistence, business-rule enforcement, and external-service integration require an implemented backend and a dedicated test/staging environment. None are provided by this portfolio; do not claim these checks passed.

## 5. Communicate changes

Update `CHANGELOG.md` and bilingual release notes for relevant changes. If a real contract-breaking change is proposed, prepare corresponding migration guidance in both languages. The current v1 → v2 migration guide is only a hypothetical example.

## 6. Open a pull request

Explain what changed, the reason, affected operations and languages, compatibility implications, tests actually performed, limitations, and outstanding questions. Review the English–Vietnamese parity before merging.

No reviewer approval or backend verification is implied by the existence of this workflow.
