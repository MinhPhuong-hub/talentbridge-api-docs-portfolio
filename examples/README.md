# Runnable contract/mock examples

**English | [Tiếng Việt](README.vi.md)**

Scripts demonstrate requests to a **local Prism mock** generated from `openapi.yaml`. They do **not** verify production backend behavior, real authentication, real authorization, persistence, or business-rule enforcement. In particular, a mocked `403` or `404` does not prove access control or resource lookup logic.

## Start Prism

From the repository root, with Node.js/npm available:

```bash
npx @stoplight/prism-cli mock openapi.yaml
```

Prism runs at `http://127.0.0.1:4010` by default. Keep it running in a separate terminal.

## Run the Bash examples

Use Git Bash, WSL, or another Bash shell (the `.sh` scripts do not run directly in PowerShell):

```bash
bash examples/list-jobs.sh
bash examples/list-jobs-empty.sh
bash examples/create-job.sh
bash examples/simulate-forbidden.sh
bash examples/simulate-not-found.sh
```

## Windows PowerShell alternatives

```powershell
npx.cmd @stoplight/prism-cli mock openapi.yaml
# In a second terminal:
curl.exe -H "Prefer: example=empty" http://127.0.0.1:4010/jobs
curl.exe -i -H "Prefer: code=404" http://127.0.0.1:4010/jobs/job_unknown
```

The `Prefer` headers select mock examples or simulated statuses; they do not establish server-side business behavior. Prism behavior depends on its version and configuration.
