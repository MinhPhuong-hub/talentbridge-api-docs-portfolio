# Authentication

TalentBridge uses bearer access tokens for protected API operations.

Send the token in the `Authorization` header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Example:

```bash
curl -X POST \
  http://127.0.0.1:4010/jobs \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Backend Developer",
    "description": "Build and maintain recruitment platform APIs.",
    "location": "Ho Chi Minh City"
  }'
```

## Authentication and authorization errors

### 401 Unauthorized

A `401` response means the request could not be authenticated.

Common causes include:

- no access token
- an invalid token
- an expired token

### 403 Forbidden

A `403` response means the caller is authenticated but does not have
permission to perform the requested operation.

For example, a candidate cannot create a job because that operation
requires the recruiter role.

Authentication answers:

**Who are you?**

Authorization answers:

**Are you allowed to do this?**


---

**Navigation:** [English documentation index](README.md) · [Bản tiếng Việt](../vi/authentication.md)
