
---

This one is important. **Do not use your real `14321` / `14324` accounts here.**

```markdown
# Experimental Design and Test Matrix

## Test Environment

The experiment uses a controlled local API environment.

### Technology

- ASP.NET Core REST API
- C#
- JWT-based authentication
- Local test environment
- Synthetic users
- Synthetic attendance records
- Python-based detection tool
- Burp Suite for manual validation

---

## Synthetic Test Identities

The experiment uses synthetic identities that do not represent real users.

| Identity | User ID | Ownership |
|---|---:|---|
| User A | 1001 | Object A |
| User B | 1002 | Object B |
| Admin | 9000 | Administrative access |

---

## Authorization Model

Normal users are expected to access only resources for which they have authorization.

Therefore:

```text
User A → Object A → ALLOW
User A → Object B → DENY

User B → Object B → ALLOW
User B → Object A → DENY
