# Error handling

TalentBridge uses a consistent JSON error format.

Error responses use:

```http
Content-Type: application/problem+json
```

Example:

```json
{
  "type": "https://api.talentbridge.example/problems/not-found",
  "title": "Resource not found",
  "status": 404,
  "detail": "The requested resource could not be found.",
  "instance": "/jobs/job_unknown"
}
```

## Error fields

| Field | Description |
|---|---|
| `type` | Identifies the category of error. |
| `title` | Short human-readable summary. |
| `status` | HTTP status code. |
| `detail` | Explanation of the specific error occurrence. |
| `instance` | Identifies the request or resource associated with the error. |

## Common status codes

### 400 Bad Request

The request is syntactically valid HTTP but contains invalid API input.

Examples:

- required field missing
- invalid enum value
- string exceeds its allowed length

Review the `detail` field and correct the request before retrying.

### 401 Unauthorized

Authentication is missing or invalid.

Obtain a valid access token before retrying the request.

### 403 Forbidden

Authentication succeeded, but the caller does not have permission to
perform the operation.

Changing the request body usually does not resolve this error. Verify
the user's role or resource permissions.

### 404 Not Found

The requested resource does not exist.

Check the resource identifier before retrying.

### 409 Conflict

The request conflicts with the current state of the system.

For example, the API returns `409` when a candidate attempts to apply
for the same job more than once.
