# TalentBridge Recruitment API Documentation

**Language:** English | [Tiếng Việt](README.vi.md)

> Portfolio case study demonstrating API documentation, OpenAPI,
> developer experience, docs-as-code, bilingual technical writing,
> and API change management.

**TalentBridge is a fictional recruitment platform created for this portfolio project.**

## Portfolio highlights

API documentation portfolio showcasing OpenAPI, docs-as-code, runnable examples, bilingual technical writing, and API change management.

| Artifact | What it demonstrates |
|---|---|
| [`openapi.yaml`](openapi.yaml) | Contract-first API reference |
| [API review notes](docs/en/api-review-notes.md) | Requirement ambiguity and portfolio assumptions |
| [Jobs API](docs/en/jobs-api.md) | Developer-focused reference |
| [Error handling](docs/en/errors.md) | Status codes and troubleshooting |
| [Release notes](docs/en/release-notes/v1.1.0.md) | User-facing change communication |
| [Migration guide](docs/en/migration-v1-to-v2.md) | Fictional breaking-change scenario |
| [Style guide](docs/style-guide.md) | Editorial consistency |
| [Runnable examples](examples/README.md) | Local contract/mock demonstrations |
| [English docs](docs/en/README.md) / [Tiếng Việt](docs/vi/README.md) | Bilingual documentation |

## About this project

This repository demonstrates how I document and review an HTTP API for developers integrating with a recruitment platform.

The project covers:

- OpenAPI 3.0.3 API specification
- Developer-focused API reference documentation
- Runnable curl examples
- Authentication and authorization documentation
- Consistent error documentation
- Requirement clarification and API review notes
- API versioning and migration documentation
- Release notes and changelog management
- Vietnamese-English technical documentation
- Git-based docs-as-code workflow

## API domain

TalentBridge connects two types of users:

- **Candidates**, who search for jobs and submit applications.
- **Recruiters**, who create jobs and review applications.

The primary resources are:

- `Job`
- `Application`

## API overview

| Method | Endpoint | Description |
|---|---|---|
| GET | `/jobs` | List available jobs |
| POST | `/jobs` | Create a job |
| GET | `/jobs/{jobId}` | Get a job |
| POST | `/jobs/{jobId}/applications` | Apply for a job |
| GET | `/jobs/{jobId}/applications` | List applications for a job |
| PATCH | `/applications/{applicationId}` | Update application status |

## Run the API mock locally

The API can be explored without a backend implementation by running the OpenAPI specification with Prism.

```bash
npx @stoplight/prism-cli mock openapi.yaml
```

The mock server is available at:

```text
http://127.0.0.1:4010
```

Example request:

```bash
curl \
  -H "Prefer: example=normal" \
  http://127.0.0.1:4010/jobs
```

**Mock-server scope:** Prism generates responses from `openapi.yaml`. It is not a production backend and cannot prove real authentication, authorization, persistence, business-rule enforcement, or service integrations.

## Documentation

- [Getting started](docs/en/README.md)
- [Authentication](docs/en/authentication.md)
- [Jobs API](docs/en/jobs-api.md)
- [Error handling](docs/en/errors.md)
- [API review notes](docs/en/api-review-notes.md)
- [Migration guide](docs/en/migration-v1-to-v2.md)
- [Vietnamese getting started guide](docs/vi/getting-started.md)
- [Documentation style guide](docs/style-guide.md)

## Change management

API changes are documented through:

- `CHANGELOG.md`
- version-specific release notes
- migration guides for breaking changes
- Git pull-request review

See [CONTRIBUTING.md](CONTRIBUTING.md) for the documentation workflow.

## Skills demonstrated

This project is designed to demonstrate practical Technical Writer skills:

**API documentation**
Reading an OpenAPI contract and turning it into developer-facing documentation.

**Technical investigation**
Identifying ambiguous requirements and asking engineers or business stakeholders targeted questions.

**Developer experience**
Providing usable request examples, error documentation, authentication guidance, and integration instructions.

**Docs-as-code**
Managing documentation through Git branches and pull requests.

**Change communication**
Identifying breaking changes and documenting release impact and migration steps.

**Bilingual technical writing**
Maintaining equivalent Vietnamese and English documentation while preserving technical meaning.
