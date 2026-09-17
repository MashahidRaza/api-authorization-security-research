
---

```markdown
# Authorization Model

## Purpose

This document defines the authorization relationships used by the controlled laboratory experiment.

---

## Synthetic Users

| User | ID | Expected Ownership |
|---|---:|---|
| User A | 1001 | Object A |
| User B | 1002 | Object B |
| Admin | 9000 | Defined by administrative policy |

---

## Normal User Policy

A normal user may access resources for which the user has authorization.

For the initial experiment:

```text
User A → Object A → ALLOW
User A → Object B → DENY

User B → Object B → ALLOW
User B → Object A → DENY
