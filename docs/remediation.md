# BOLA Remediation

## Objective

The remediation objective is to prevent an authenticated user from accessing
another user's protected object by manipulating a client-controlled object
identifier.

The security control must be enforced on the server side.

---

## Vulnerable Design

The vulnerable implementation accepts the requested `userId` and directly
uses it to retrieve data.

Conceptually:

```text
Authenticated User: 1001
Requested userId:   1002

        ↓

API trusts userId

        ↓

User 1002 data returned
