# Getting started

This guide shows how to make your first request to the TalentBridge API.

## Base URL

Production example:

`https://api.talentbridge.example/v1`

For this portfolio project, you can run a local mock server instead.

## Run the local mock API

From the repository root:

```bash
npx @stoplight/prism-cli mock openapi.yaml
```

The mock API runs at:

`http://127.0.0.1:4010`

## List jobs

```bash
curl \
  -H "Prefer: example=normal" \
  http://127.0.0.1:4010/jobs
```

Example response:

```json
{
  "items": [
    {
      "id": "job_123",
      "title": "Backend Developer",
      "description": "Build and maintain recruitment platform APIs.",
      "location": "Ho Chi Minh City",
      "recruiterId": "user_901",
      "createdAt": "2026-10-20T10:00:00Z"
    }
  ],
  "nextCursor": "cursor_abc123"
}
```

## Pagination

Use the `limit` parameter to control the maximum number of jobs returned.

```bash
curl "http://127.0.0.1:4010/jobs?limit=10"
```

When `nextCursor` contains a value, send that value in the next request:

```bash
curl \
  "http://127.0.0.1:4010/jobs?limit=10&cursor=cursor_abc123"
```

Treat cursors as opaque values. Clients should not parse or modify them.

## Authenticated requests

Protected endpoints require a bearer access token:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

See [Authentication](authentication.md) for details.
