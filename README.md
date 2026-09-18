# api-authorization-security-research
Research-driven REST API security project for detecting and remediating Broken Object Level Authorization (BOLA) using authenticated differential testing, Burp Suite, and automated security validation
# Authenticated API Authorization Assessment & Automated BOLA Detection

A research-oriented Application Security project investigating whether authenticated differential testing of REST API object identifiers can identify Broken Object Level Authorization (BOLA).

The project combines manual API security testing, controlled vulnerable/secure implementations, automated differential testing, remediation, and experimental evaluation.

---

## Research Focus

### Primary Question

**Can authenticated differential manipulation of REST API object identifiers reliably detect Broken Object Level Authorization (BOLA) in a controlled API environment?**

### Hypothesis

If a REST API fails to enforce server-side object-level authorization, changing an object identifier while keeping the authenticated identity constant may allow access to an object owned by another user.

A properly authorized implementation should deny the cross-object request.

---

# Project Method

The project follows the workflow:

```text
Real-World Security Observation
              ↓
       Security Hypothesis
              ↓
    Controlled Local Reproduction
              ↓
       Vulnerable API
              ↓
      Differential Testing
              ↓
     Automated Detection
              ↓
     Server-Side Remediation
              ↓
          Re-Testing
              ↓
     Experimental Evaluation
