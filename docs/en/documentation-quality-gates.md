# Documentation quality gates

## Definition of done for a documentation pull request

- [ ] The intended reader and task are explicitly stated.
- [ ] Every normative assertion traces to an approved contract decision or verified behavior.
- [ ] Endpoint methods, paths, parameters, fields, examples and statuses agree with OpenAPI.
- [ ] 401 (missing/invalid credentials) and 403 (authenticated but forbidden) are distinguished where applicable; do not invent concealment policy (403 vs 404).
- [ ] 404 for a missing individual resource is distinguished from a successful empty collection.
- [ ] Request and response examples are syntactically valid and tied to the correct media type.
- [ ] Error responses describe actionable client behavior, not only HTTP names.
- [ ] Claims about retries, authorization, duplication and pagination are evidenced or flagged as unresolved.
- [ ] Code snippets name the correct base URL, shell and required prerequisites.
- [ ] Mock examples explicitly disclose that persistence, auth and business logic are not implemented.
- [ ] EN and VI versions preserve technical meaning, identifiers and API semantics.
- [ ] Release notes communicate the consumer impact, upgrade action and actual compatibility evidence.
- [ ] No editorial commentary, placeholders, unmatched code fences, broken relative links or secrets remain.
- [ ] A second reviewer checks the diff before merge; fictional review simulations are labeled.

## Severity rubric

| Severity | Example | Release action |
| --- | --- | --- |
| Critical | Incorrect authorization guidance, misleading production claim, breaking example | Block publication |
| Major | Undocumented state transition, unsupported compatibility assertion, ambiguous error behavior | Resolve or label explicitly before publication |
| Minor | Repetition, inconsistent capitalization without semantic impact | Fix during review |

## Reviewer questions

1. What can the reader accomplish after following this page?
2. What might a reasonable reader incorrectly assume?
3. Which claims require product/developer confirmation?
4. Can every example be inspected against the OpenAPI schema?
5. If behavior changes, which tutorials, reference pages and release notes must change together?

## Source-of-truth hierarchy (case study)

1. **Approved decisions** recorded with owner and date (in a real product)
2. **Verified implementation / tests** (not available in this fictional portfolio)
3. **Published OpenAPI contract** for described API syntax
4. **Explanatory documentation** derived from that contract
5. **Proposed design assumptions**, always flagged and never asserted as verified behavior

If sources disagree, do not silently pick one. Open an issue, track the conflict and withhold an unsupported statement.
