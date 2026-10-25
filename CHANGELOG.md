# Changelog

All notable changes to the TalentBridge API documentation are recorded
in this file.

## [1.1.0] - 2026-10-24

### Added

- Optional `coverLetter` field when creating an application.
- `409 Conflict` response for duplicate job applications.
- Named mock examples for normal and empty job-list responses.
- Vietnamese getting-started documentation.
- API review and requirement-clarification notes.

### Documentation

- Clarified the difference between `401 Unauthorized` and
  `403 Forbidden`.
- Clarified that `recruiterId` and `candidateId` are derived from the
  authenticated user rather than supplied by clients.

## [1.0.0] - 2026-10-01

### Added

- Initial Jobs API.
- Initial Applications API.
- Bearer authentication.
- Standard problem error response.
- Cursor-based job pagination.
