# Research Methodology

This project uses a controlled, empirical security-testing methodology based on authenticated differential requests.

The overall workflow is:

**Threat Model → Baseline → Differential Test → Ground Truth → Detection → Remediation → Re-Test → Evaluation**

---

## Phase 1 — Threat Modeling and Endpoint Identification

Identify REST API endpoints that accept client-controlled object identifiers.

Examples include:

- query parameters
- route parameters
- JSON body fields

The selected endpoint must represent a resource that belongs to a specific authenticated user.

---

## Phase 2 — Establish Authorization Ground Truth

Create a controlled dataset containing synthetic users and resources.

For example:

- User A owns Object A
- User B owns Object B
- User A should not access Object B
- User B should not access Object A

The expected authorization relationship is defined before testing.

---

## Phase 3 — Baseline Request

Authenticate as User A and request an object owned by User A.

Record:

- HTTP method
- endpoint
- object identifier
- authentication context
- HTTP status
- response structure
- relevant response fields

This establishes the legitimate access baseline.

---

## Phase 4 — Differential Request

Duplicate the baseline request.

Keep the following constant:

- authentication identity
- authentication token
- HTTP method
- endpoint
- relevant headers

Change only the target object identifier.

Example:

```text
Baseline:
User A token → Object A

Differential:
User A token → Object B
