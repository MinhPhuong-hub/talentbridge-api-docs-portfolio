# Applications API

The Applications API supports candidate submissions and recruiter review in the **fictional** TalentBridge contract. The base URL for runnable examples is the [local Prism mock](getting-started.md), not a deployed service. Prism does not enforce roles, uniqueness, ownership, or state transitions.

## Apply for a job

`POST /jobs/{jobId}/applications` · Bearer token · Candidate role (assumed design rule)

| Input | Location | Required | Contract |
|---|---|---|---|
| `jobId` | Path | Yes | Job identifier |
| `coverLetter` | JSON body | No | String, maximum 1,000 characters |

Do not send `candidateId` or `status`. Under the portfolio's **assumed design**, the server derives the candidate from the access token and initializes the application as `pending`.

```bash
curl -i -X POST 'http://127.0.0.1:4010/jobs/job_123/applications' \
  -H 'Authorization: Bearer demo-token' \
  -H 'Content-Type: application/json' \
  -d '{"coverLetter":"I have experience documenting HTTP APIs."}'
```

**201 Created** — Example JSON response:

<!-- doc-test: response POST /jobs/{jobId}/applications 201 -->
```json
{"id":"app_456","jobId":"job_123","candidateId":"user_321","status":"pending","coverLetter":"I have experience documenting HTTP APIs.","createdAt":"2026-10-24T13:00:00Z"}
```

**Errors:** `400` invalid body; `401` missing/invalid token; `403` insufficient permission; `404` unknown job; `409` duplicate application for the candidate–job pair (assumed business rule). For `409`, do **not** blindly repeat an identical submission. See [Error handling](errors.md).

## List applications for a job

`GET /jobs/{jobId}/applications` · Bearer token · Job-owning recruiter (assumed design rule)

```bash
curl -i 'http://127.0.0.1:4010/jobs/job_123/applications' \
  -H 'Authorization: Bearer demo-token'
```

**200 OK** returns an `items` array of `Application` objects. A job with no applications returns `{"items":[]}`. This collection is nested under the job; an empty collection is **not** a `404`. Errors: `401`, `403`, `404` (for unknown job).

## Update application status

`PATCH /applications/{applicationId}` · Bearer token · Authorized recruiter

```bash
curl -i -X PATCH 'http://127.0.0.1:4010/applications/app_456' \
  -H 'Authorization: Bearer demo-token' \
  -H 'Content-Type: application/json' \
  -d '{"status":"accepted"}'
```

Request JSON: **required** `status`, one of `accepted` or `rejected`. **200 OK** returns an `Application` object. Errors currently documented: `400`, `401`, `403`, `404`.

**Important contract gap:** The specification restricts **target status values**, but does **not** define which source statuses may transition, whether a repeated update succeeds, who qualifies as an authorized recruiter for this operation, or concurrent-update semantics. Do not infer these rules from the enum. They are tracked in the [contract decision record](contract-decision-record.md) as unresolved assumptions requiring a domain owner in a real implementation. This mock must not be described as proof of those behaviors.

## Fields returned

`Application` contains `id`, `jobId`, `candidateId`, `status`, `createdAt`, and optionally `coverLetter`. The values of `status` are `pending`, `accepted`, `rejected` (read schema); only `accepted` and `rejected` are accepted by the PATCH request schema.

---

[API reference index](README.md) · [Bản tiếng Việt](../vi/applications-api.md)
