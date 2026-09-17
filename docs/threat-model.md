
---


```markdown
# Threat Model

## System

The system under assessment is a REST API providing authenticated access to user-owned resources.

---

## Asset

Protected user-specific API resources.

For the laboratory environment, the data is synthetic.

---

## Threat Actor

An authenticated user who is authorized to use the API but is not authorized to access another user's object.

---

## Entry Point

Client-controlled object identifiers such as:

```text
?userId=1001
