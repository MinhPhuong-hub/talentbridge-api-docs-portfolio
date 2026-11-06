# API contract decision record

> **Portfolio classification:** Fictional case study. The decisions below are **proposed documentation assumptions**, not confirmed production behavior. No actual backend, production identity system, customer traffic, or developer sign-off is claimed.

## Why this record exists

An OpenAPI operation lists the syntax a client can send. Integrators also need explicit rules for authorization, ownership, conflicting operations, retries, and state transitions. A writer must not invent those rules and present them as implemented behavior.

## Decision register

| ID | Contract question | Current evidence | Proposed rule for review | Status | Verification needed |
| --- | --- | --- | --- | --- | --- |
| TB-001 | Who may create a job? | Documentation describes recruiter role | Only authenticated recruiters | **Proposed** | Confirm authorization policy and 401/403 behavior |
| TB-002 | Who supplies `recruiterId`? | Review notes indicate token-derived identity | Server derives identity; ignore/reject client-supplied ownership | **Proposed** | Confirm exact request schema, behavior on extra fields, token claims |
| TB-003 | Who may update an application? | PATCH is recruiter-restricted | Only an owner/authorized member of the associated job's recruiting team | **Open** | Specify tenant isolation, ownership, 403 vs 404 policy |
| TB-004 | Which status transitions are valid? | PATCH accepts `accepted` or `rejected` | Only `pending` → `accepted` or `pending` → `rejected` | **Open** | Define full state machine, repeated updates, invalid transitions |
| TB-005 | Duplicate applications | Error guidance mentions HTTP 409 | One active application per (candidate, job) | **Open** | Define uniqueness boundary, withdrawn applications, race conditions |
| TB-006 | Cursor pagination | Getting started mentions `nextCursor` | Opaque cursor; absent/null cursor means no more results | **Open** | Define stable ordering, filters, invalid/expired cursor behavior |
| TB-007 | API error representation | Error documentation lists statuses | Structured stable application error code in addition to HTTP status | **Open** | Confirm schema and existing client compatibility |
| TB-008 | Retry safety | Not yet established | GET safe to retry; POST not guaranteed idempotent | **Open** | Confirm idempotency-key support, timeout handling, retry headers |

## Example: application status transition questions

Before publishing PATCH `/applications/{applicationId}`, obtain explicit answers to:

1. Is the initial status `pending`, `submitted`, or another value?
2. Are `accepted` → `rejected` and `rejected` → `accepted` permitted?
3. Does repeating the same PATCH return success, conflict, or a validation error?
4. Must the recruiter own the parent job, and how is cross-tenant access handled?
5. Which response and error body identify an invalid transition?
6. Does an update require an optimistic concurrency token (ETag / If-Match)?

### State transition table — illustrative proposal, NOT an API guarantee

| Current | Requested | Proposed outcome | Validation status |
| --- | --- | --- | --- |
| `pending` | `accepted` | Transition permitted | Unverified |
| `pending` | `rejected` | Transition permitted | Unverified |
| `accepted` | `rejected` | Reject or require explicit reopening action | Unresolved |
| `rejected` | `accepted` | Reject or require explicit reopening action | Unresolved |
| `accepted` | `accepted` | Define idempotent repeat behavior | Unresolved |

**Publication gate:** Do not copy the illustrative table into normative endpoint documentation until a business/domain decision is recorded. Once approved, synchronize OpenAPI descriptions, examples, tests, migration notes, and EN/VI pages in the same PR.

## Decision recording template

- **Decision ID:** TB-XXX
- **Question:**
- **Why this matters to consumers:**
- **Alternatives considered:**
- **Decision and rationale:**
- **Owner:** Fictional case study / actual approver only if real
- **Decision status:** Proposed / Approved in case study / Verified against implementation
- **Contract impact:** Endpoint, status, field, example, version, client behavior
- **Verification evidence:** Test case or source reference; "not available" if fictional
