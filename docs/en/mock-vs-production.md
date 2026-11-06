# Run the contract mock: capabilities and limitations

## What this repository demonstrates

TalentBridge is a **fictional API documentation portfolio**. The OpenAPI specification describes an illustrative contract. Prism can serve static or generated mock responses from that contract. Neither Prism nor this portfolio implements a production authentication service, authorization checks, persistent jobs, an application lifecycle, uniqueness constraints, or cursor-based database pagination.

Do not treat a successful HTTP response from a mock as proof of business behavior. `Authorization: Bearer <token>` in an example illustrates the request format; it does not establish token validation by a backend.

## Local setup

From the repository root, identify the actual OpenAPI file (`openapi.yaml`, `openapi.yml`, or the documented alternative). With Node.js and npm installed:

```powershell
npx --yes @stoplight/prism-cli mock .\openapi.yaml
```

If your spec is located elsewhere, replace `.\openapi.yaml` with its real path. Prism commonly starts on `http://127.0.0.1:4010` (confirm the address in terminal output).

In a second PowerShell window, query a documented route using the path defined by the specification:

```powershell
curl.exe -i http://127.0.0.1:4010/v1/jobs
```

If the spec uses `/jobs` without `/v1`, adjust the path. `curl.exe` is used explicitly because `curl` aliases differ across PowerShell versions. Replace example IDs and bodies with values from the OpenAPI examples.

## What to verify

| Claim | Supported by a Prism response? | What is needed for stronger evidence? |
| --- | --- | --- |
| Endpoint/example is described in OpenAPI | Yes | OpenAPI lint + inspect contract |
| Mock endpoint can return a response | Yes, when configured | Local Prism smoke command |
| Token is cryptographically validated | No | Auth implementation + integration test |
| Recruiter ownership is enforced | No | Backend permission tests |
| Status transitions persist | No | Stateful backend and tests |
| Duplicate applications return 409 reliably | No | Uniqueness implementation / contract tests |
| Cursor returns a real next page | No | Stateful pagination test |

## Example policy

- **Illustrative API URL:** `https://api.talentbridge.example` — reserved example domain, not a live service.
- **Local mock URL:** the URL printed by Prism after launch.
- **Request examples:** intended to demonstrate the contract; do not promise they reach a deployed application.
- **Credentials:** never put actual tokens in repository examples.

For each tutorial, label the execution target and expected output as **mock** or **hypothetical production**. Never present static examples as observed production responses.
