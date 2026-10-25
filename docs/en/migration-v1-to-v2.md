# Migrating from API v1 to v2

This document demonstrates how breaking API changes should be
communicated to integration developers.

## Overview

Version 2 introduces two breaking changes:

1. `recruiterId` is renamed to `ownerId`.
2. Application status values are renamed.

Clients using these fields must be updated before migrating to v2.

## recruiterId renamed to ownerId

### v1

```json
{
  "id": "job_123",
  "recruiterId": "user_901"
}
```

### v2

```json
{
  "id": "job_123",
  "ownerId": "user_901"
}
```

### Required client change

Replace code that reads:

```javascript
job.recruiterId
```

with:

```javascript
job.ownerId
```

This is a breaking change because clients that depend on
`recruiterId` will no longer receive that property.

---

## Application status values

Version 1 uses:

```text
pending
accepted
rejected
```

Version 2 uses:

```text
pending
approved
declined
```

Update any comparisons, UI mappings, database mappings, or validation
logic that depend on the old values.

For example:

```javascript
if (application.status === "accepted") {
  // v1
}
```

becomes:

```javascript
if (application.status === "approved") {
  // v2
}
```

## Migration checklist

Before switching production traffic to v2:

- update generated or handwritten API types
- update field references
- update status mappings
- update automated tests
- verify v2 responses in a staging environment
- deploy the client changes
- switch the integration to the v2 base URL
