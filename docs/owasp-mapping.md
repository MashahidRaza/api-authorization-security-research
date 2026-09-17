# OWASP API Security Mapping

## Primary Finding

### API1:2023 — Broken Object Level Authorization

The primary security focus of this project is Broken Object Level Authorization (BOLA).

The vulnerability occurs when an API exposes an object through a client-controlled identifier but fails to properly enforce whether the authenticated requester is authorized to access that specific object.

---

## Project Test Scenario

The controlled laboratory scenario uses:

```text
Authenticated User A
        ↓
GET /api/...?...objectId=ObjectA
        ↓
Authorized response
