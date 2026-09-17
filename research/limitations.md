# Research Limitations

## 1. Controlled Environment

The primary experiment is conducted against a locally controlled API using synthetic users and synthetic data.

Results from the laboratory environment may not represent all production API architectures.

---

## 2. Authorization Model Dependency

Differential testing requires knowledge of the expected authorization relationship between the requesting identity and the target object.

Without reliable authorization ground truth, response differences alone may not establish a vulnerability.

---

## 3. Response-Based Detection

The initial detector relies on observable HTTP behavior and response differences.

Some authorization failures may not produce obvious differences in status codes or response structures.

---

## 4. Complex Business Logic

Applications may implement authorization through complex business rules, workflows, tenant relationships, or contextual permissions.

A simple object-identifier substitution test may not capture every authorization scenario.

---

## 5. Token Management

Automated testing requires valid authentication credentials for the controlled test environment.

Token expiration, authentication flows, and refresh mechanisms may affect automated testing.

---

## 6. Limited Initial Vulnerability Scope

The initial implementation focuses on Broken Object Level Authorization.

Other API authorization problems, such as property-level and function-level authorization, are outside the primary experimental scope.

---

## 7. Dataset Size

The initial experiment uses a small synthetic dataset.

Larger datasets and additional API structures would be required to evaluate scalability and generalization.

---

## 8. Ethical Scope

No automated testing is performed against unauthorized production resources.

Real-world observations are used only as motivation and contextual evidence. Reproducible experiments use controlled synthetic data.
