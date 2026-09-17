# Research Question and Objectives

## Primary Research Question

**Can authenticated differential manipulation of REST API object identifiers reliably detect Broken Object Level Authorization (BOLA) in a controlled API environment?**

---

## Hypothesis

If an API fails to enforce server-side object-level authorization, changing an object identifier while keeping the authenticated identity constant may allow access to an object owned by another user.

A properly authorized implementation should deny the cross-user request.

---

## Research Objectives

1. **Establish a Reproducible Methodology**
   
   Define a structured differential-testing methodology for evaluating REST API object-level authorization.

2. **Construct a Controlled Test Environment**
   
   Develop a local ASP.NET Core REST API containing:
   - an intentionally vulnerable authorization implementation
   - a remediated authorization implementation
   - synthetic users and synthetic data

3. **Perform Differential Testing**
   
   Compare requests where the authenticated identity remains constant while the target object identifier changes.

4. **Automate BOLA Detection**
   
   Develop a Python-based detector that compares authorized baseline requests with cross-object requests and identifies potential authorization failures.

5. **Verify Remediation**
   
   Confirm that the secure implementation denies unauthorized object access while preserving legitimate access.

6. **Evaluate Detection Performance**
   
   Measure detector outcomes using controlled test cases and report true positives, true negatives, false positives, and false negatives where applicable.

---

## Research Scope

The initial research focuses on:

- REST APIs
- authenticated requests
- object-level authorization
- user-owned resources
- identifier substitution
- HTTP response comparison
- server-side authorization
- API1:2023 Broken Object Level Authorization

The research does not attempt to assess production systems or access unauthorized real-world user data.
