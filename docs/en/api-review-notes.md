# API review and requirement clarification

This document records questions raised while converting product
requirements into developer documentation.

It demonstrates the clarification process that should occur before
publishing API behavior as fact.

## 1. Source of recruiterId

**Initial ambiguity**

The Job model contains `recruiterId`, but the create-job request did not
specify whether the client should send it.

**Question for engineering**

Is `recruiterId` supplied by the client, or derived from the authenticated
user?

**Resolved behavior**

The server derives `recruiterId` from the authenticated recruiter.

**Documentation impact**

`recruiterId` appears in Job responses but not in `CreateJobRequest`.

---

## 2. New application status

**Question**

Can candidates specify an application status when applying?

**Resolved behavior**

No. New applications always start with `pending`.

Only authorized recruiters can later change the status.

---

## 3. Duplicate applications

**Question**

What happens when the same candidate applies for the same job twice?

**Resolved behavior**

The API returns:

`409 Conflict`

This behavior is documented in both OpenAPI and the error guide.

---

## 4. Application permissions

**Question**

Can every recruiter list applications for every job?

**Resolved behavior**

No.

Only the recruiter who owns the job can list its applications.

Other authenticated users receive `403 Forbidden`.

---

## 5. Pagination cursor

**Question**

Can clients decode the cursor or construct their own cursor values?

**Resolved behavior**

No.

The cursor is opaque and must be reused exactly as returned by the API.

---

## 6. Application status transitions

**Question**

Which values may recruiters send when reviewing a pending application?

**Resolved behavior**

The review endpoint accepts:

- `accepted`
- `rejected`

The candidate cannot directly update application status.

---

## Documentation principle

When API behavior is ambiguous, documentation should not silently
invent a rule.

The writer should identify the ambiguity, ask the responsible engineer
or business stakeholder, record the decision, and then update the API
contract and documentation consistently.
