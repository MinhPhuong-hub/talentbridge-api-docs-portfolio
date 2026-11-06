# Case study: designing developer documentation for a fictional hiring API

## Project overview

**Role simulated:** Technical Writer / API Documentation contributor

**Domain:** Recruitment platform with jobs and applications

**Deliverables:** OpenAPI 3.0.3 specification, developer-facing documentation, bilingual reference material, change communication, contract review and static API mocking.

**Disclosure:** TalentBridge is fictional. I did not implement a production backend, operate an authentication service, interview real TalentBridge developers, or measure outcomes with real customers. Prism provides contract-based responses, not production business logic.

## Documentation problem

An endpoint list does not tell integrators who can act on a resource, which transitions are allowed, what failures mean, or whether retries are safe. Ambiguous behavior spreads into examples, error documentation and release notes.

## My approach

1. Organize the contract around reader tasks rather than simply listing HTTP methods.
2. Write example request and response shapes with clearly identified mock limitations.
3. Review business-critical ambiguity: role vs ownership, `401` vs `403`, empty list vs missing resource, duplicate submission, retry semantics and status transitions.
4. Track unresolved decisions in a decision register instead of inventing server behavior.
5. Use a Markdown audit and OpenAPI linting in the review workflow.
6. Review release notes from the consumer's perspective: what changed, who is affected, what must be updated.

## One concrete documentation challenge

The statement “a recruiter may update an application” is insufficient for developer documentation. The missing constraints include parent-job ownership, cross-tenant visibility, valid status transitions, and repeated PATCH behavior. My proposed clarification matrix is in [API contract decision record](contract-decision-record.md). Every proposed answer remains explicitly unverified.

## What is demonstrated and what is not

| Demonstrated in repository | Not demonstrated |
| --- | --- |
| Documentation structure and OpenAPI authoring | Production backend design or implementation |
| Drafted requirement clarification questions | Real stakeholder interviews |
| Static mock usage and documented limitations | Authentication and authorization enforcement |
| Proposed editorial and contract quality gates | Production user metrics and client integration outcomes |
| Release-note editing process | Real customer deployment |

## Next validation steps

- Add schema-validation tests for representative request and response examples.
- Resolve the proposed decisions through a fictional, explicitly labeled design review or a real reviewer when available.
- Demonstrate a real pull request with review comments, test results and change rationale.
- Align any updated operation descriptions and code examples with the corresponding OpenAPI changes.

**For reviewers:** Evaluate my ability to communicate technical uncertainty accurately, not a claim to have built or maintained the fictional service.
