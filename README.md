# api-authorization-security-research
Research-driven REST API security project for detecting and remediating Broken Object Level Authorization (BOLA) using authenticated differential testing, Burp Suite, and automated security validation
# API Authorization Security Research: BOLA / IDOR

## Executive Summary
During security research on the target API (`api.inspirertechnologies.com`), a **Broken Object Level Authorization (BOLA)** / **Insecure Direct Object Reference (IDOR)** vulnerability was identified in the `GetAttendanceByUserId` endpoint. 

An authenticated user can view attendance records and personal identifiers of other users simply by changing the `userId` parameter in the HTTP GET request.

---

## Vulnerability Details

* **Vulnerability Class:** Broken Object Level Authorization (OWASP API Security Top 10 - API1:2023)
* **Vulnerable Endpoint:** `GET /api/MobileApp/GetAttendanceByUserId`
* **Vulnerable Parameter:** `userId`
* **Authentication Required:** Yes (Valid Bearer JWT Token)

---

## Proof of Concept (PoC)

1. **Baseline Request (`userId=14321`):**
   * An authenticated user sends a valid request for their own attendance data.
   * **Evidence:** `evidence/02-burp-baseline/request.txt` & `response.txt`
   * **User Returned:** `inspirer10042@inspirer.edu.pk`

2. **Parameter Tampering (`userId=14324`):**
   * The attacker keeps their own Bearer JWT token but changes `userId` to `14324` in the query string.
   * **Evidence:** `evidence/03-burp-object-id-change/request_2.txt` & `response_2.txt`
   * **User Returned:** `inspirer10044@inspirer.edu.pk`

3. **Impact:**
   * Full access to sensitive attendance logs, student codes, and user details across the tenant without proper authorization enforcement.

---

## Remediation & Patch Recommendation

To fix this vulnerability, implement object-level authorization checks in the backend controller before querying the database:

1. Extract the authenticated user's ID directly from the validated JWT claims (`User.FindFirst("sub")` or similar).
2. Ensure the requested `userId` parameter matches the JWT claim ID before processing the database query.
3. If the IDs do not match and the requesting user lacks elevated administrative rights, return a `403 Forbidden` response.
