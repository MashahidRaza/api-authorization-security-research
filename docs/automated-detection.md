# Automated BOLA Detection

## Objective

The project proposes an automated differential testing approach for
identifying potential Broken Object Level Authorization (BOLA) in
authenticated REST APIs.

The detector keeps the authenticated identity constant while changing the
object identifier supplied to the endpoint.

---

## Detection Concept

The basic test is:

```text
Authenticated User A
        |
        +----> Object A → expected: ALLOW
        |
        +----> Object B → expected: DENY
