# Future Research Directions

## 1. Broken Object Property Level Authorization

Extend the detector to evaluate whether authenticated users can access or modify object properties that they are not authorized to access.

This corresponds to API3:2023.

---

## 2. Broken Function Level Authorization

Extend the methodology to test whether users can invoke API functions outside their assigned permissions.

This corresponds to API5:2023.

---

## 3. OpenAPI-Based Test Generation

Integrate OpenAPI/Swagger specifications to automatically identify:

- API endpoints
- object identifiers
- HTTP methods
- request parameters
- potential authorization test targets

---

## 4. Role-Based Authorization Matrices

Extend testing beyond two normal users by introducing multiple roles and permission relationships.

Example:

```text
User
Manager
Moderator
Administrator
