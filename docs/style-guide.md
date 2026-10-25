# TalentBridge documentation style guide

## Audience

Primary audience:

Developers integrating applications with the TalentBridge API.

## Voice

Use direct, concise, task-oriented language.

Prefer:

> Send the cursor returned by the previous request.

Avoid:

> Users may perhaps wish to consider using the cursor that was
> previously returned by the system.

## Terminology

Use these terms consistently:

| Preferred term | Avoid |
|---|---|
| job | vacancy, job post, position |
| candidate | applicant user, job seeker user |
| recruiter | employer user, hiring user |
| application | job request |
| access token | auth key, login token |
| request body | payload body |

## HTTP terminology

Write HTTP methods in uppercase:

`GET`, `POST`, `PATCH`, `DELETE`

Write status codes with both number and name when introducing them:

`404 Not Found`

Afterwards, `404` is acceptable.

## Parameter names

Parameter and property names must exactly match the API contract.

Use:

`candidateId`

Do not rewrite it as:

`candidate_id`

## Examples

Examples must:

- match the current OpenAPI schema
- use fictional data
- contain no production secrets
- use `YOUR_ACCESS_TOKEN` for credentials
- be executable when presented as runnable examples

## Error documentation

Do not document only the status code.

Explain:

- why the error occurs
- how the developer can identify the problem
- what action the developer can take next

## Translation

Technical identifiers must not be translated.

For example:

`nextCursor`, `candidateId`, `/jobs`, `Authorization`

must remain unchanged in Vietnamese documentation.
