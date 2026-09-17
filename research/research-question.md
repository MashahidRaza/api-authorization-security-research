# Research Question and Objectives

## Primary Research Question

**Can authenticated differential manipulation of REST API object identifiers reliably detect Broken Object Level Authorization (BOLA) vulnerabilities without reliance on static source code analysis?**

---

## Hypothesis

If an API fails to enforce server-side object ownership authorization, modifying an object identifier in an HTTP request while preserving a constant, valid authentication context will yield unauthorized access (HTTP 200 with sensitive payload) rather than an authorization failure (HTTP 403 Forbidden).

---

## Research Objectives

1. **Establish a Reproducible Methodology:** Define a structured, step-by-step differential testing framework to evaluate API object authorization boundaries.
2. **Local Controlled Reproduction:** Construct a local ASP.NET Core REST API featuring an intentional BOLA vulnerability alongside a remediated control version.
3. **Automate Detection:** Develop an automated Python tool that programmatically executes baseline vs. manipulated HTTP requests and flags potential BOLA conditions based on response differentials.
4. **Evaluate Remediation Efficacy:** Verify that server-side claims-based authorization checks successfully mitigate BOLA risks without disrupting legitimate application workflows.
