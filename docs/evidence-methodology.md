
---

```markdown
# Evidence Methodology

## Purpose

This document defines how security evidence is collected and organized for the project.

---

## Evidence Categories

### 01 — Real-World Observation

Contains sanitized screenshots documenting the original security observation that motivated the research.

No authentication tokens, passwords, personal information, or unnecessary production data should be published.

The observation is treated as contextual evidence rather than the complete reproducible experiment.

---

### 02 — Burp Baseline

Contains evidence of an authorized baseline API request.

The evidence should show:

- HTTP method
- endpoint
- object identifier
- authentication context represented safely
- HTTP response
- relevant response structure

Authentication tokens must be redacted.

---

### 03 — Burp Object-ID Change

Contains the differential request where the object identifier is changed while the authentication context remains constant.

Only authorized test accounts or controlled laboratory accounts should be used.

---

### 04 — Remediation Re-Test

Contains evidence demonstrating the behavior after server-side authorization is implemented.

The cross-object request should be denied according to the API's authorization policy.

---

### 05 — Automated Detector

Contains output from the Python detector executing against the controlled laboratory API.

The output should show:

- test case
- expected authorization
- observed response
- detector classification
- execution information

---

## Evidence Naming

Evidence files should use descriptive names.

Example:

```text
bola-baseline.png
bola-object-substitution.png
secure-authorization-denied.png
detector-output.png
