# Jobs API

The Jobs API lets clients discover job opportunities and lets recruiters
create new job listings.

## List jobs

`GET /jobs`

Returns available jobs.

### Query parameters

| Parameter | Type | Required | Description |
|---|---|---:|---|
| `location` | string | No | Filters jobs by location. |
| `limit` | integer | No | Maximum results. Range: 1–100. Default: 20. |
| `cursor` | string | No | Opaque cursor for the next page. |
| `sort` | string | No | Sort order. Default: `createdAt:desc`. |

Supported sort values:

```text
createdAt:desc
createdAt:asc
title:asc
title:desc
```

### Example request

```bash
curl \
  "https://api.talentbridge.example/v1/jobs?location=Remote&limit=20"
```

### 200 response

```json
{
  "items": [
    {
      "id": "job_124",
      "title": "Technical Writer",
      "description": "Create developer documentation and API guides.",
      "location": "Remote",
      "recruiterId": "user_902",
      "createdAt": "2026-10-21T08:30:00Z"
    }
  ],
  "nextCursor": null
}
```

---

## Create a job

`POST /jobs`

Creates a job listing.

The caller must be authenticated as a recruiter.

The API derives `recruiterId` from the authenticated user. Clients must
not provide it in the request body.

### Request body

| Field | Type | Required | Constraints |
|---|---|---:|---|
| `title` | string | Yes | 3–100 characters |
| `description` | string | Yes | 20–5000 characters |
| `location` | string | Yes | 2–100 characters |

### Example request

```bash
curl -X POST \
  https://api.talentbridge.example/v1/jobs \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Backend Developer",
    "description": "Build and maintain recruitment platform APIs.",
    "location": "Ho Chi Minh City"
  }'
```

### 201 response

```json
{
  "id": "job_123",
  "title": "Backend Developer",
  "description": "Build and maintain recruitment platform APIs.",
  "location": "Ho Chi Minh City",
  "recruiterId": "user_901",
  "createdAt": "2026-10-24T12:00:00Z"
}
```

### Errors

| Status | Meaning |
|---:|---|
| `400` | The request body is invalid. |
| `401` | Authentication is missing or invalid. |
| `403` | The authenticated user cannot create jobs. |

See [Error handling](errors.md) for the common error response format.


---

**Navigation:** [English documentation index](README.md) · [Bản tiếng Việt](../vi/jobs-api.md)
