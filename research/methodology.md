# Research Methodology

This research employs an empirical, laboratory-based experimental framework divided into nine distinct operational phases:

---

## Phase 1 — Threat Modeling & Endpoint Mapping
Identify candidate API endpoints that accept client-controlled object identifiers (e.g., query parameters, route parameters, JSON request body fields).

## Phase 2 — Baseline Context Establishment
Authenticate as User A, issue a legitimate request for User A's authorized resource, and record baseline HTTP metadata (Status, Body Length, Structural Keys).

## Phase 3 — Differential Request Injection
Duplicate the baseline HTTP request. Retain User A's JWT token and headers, but replace the target object identifier with User B's resource ID.

## Phase 4 — Response Differential Analysis
Compare the response against baseline criteria:
* Did the status code remain HTTP 200 OK?
* Does the returned payload contain User B's data attributes?
* Is there an absence of authorization error messages?

## Phase 5 — Ground Truth & Ownership Model Verification
Cross-examine observed results against the system's known database ownership relationships to eliminate false positives.

## Phase 6 — Vulnerability Remediation
Apply claims-based server-side authorization checks (`User.FindFirst(ClaimTypes.NameIdentifier)`) within the application layer.

## Phase 7 — Remediation Verification Re-Testing
Re-run the differential request against the patched API to ensure the server enforces HTTP 403 Forbidden for cross-user requests.

## Phase 8 — Automated Scanner Implementation
Engineered a lightweight script (`bola_detector.py`) to execute differential testing programmatically.

## Phase 9 — Experimental Evaluation
Calculate detection rates, false positive rates, and execution performance across test cases.
