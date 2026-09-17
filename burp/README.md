# Burp Suite API Authorization Testing

This directory contains sanitized, text-based HTTP request and response artifacts captured using Burp Suite Repeater during the authorization assessment.

## Manual Testing Methodology

1. **Capture Baseline:** Intercept and capture a valid, authenticated API request for an authorized object (`userId=14321`).
2. **Send to Repeater:** Pass the captured HTTP request to Burp Suite Repeater.
3. **Record Baseline Response:** Execute the request and verify a successful `200 OK` response containing student record data.
4. **Duplicate Request:** Create a secondary Repeater tab using the exact same request headers and authentication context.
5. **Manipulate Object Identifier:** Modify only the target object identifier parameter (`userId=14324`) while preserving the active JWT token.
6. **Execute & Compare:** Send the manipulated request and analyze the server response for unauthorized data access.
7. **Verify Ownership Boundary:** Confirm whether the second object belongs to a distinct identity and whether cross-account data access occurred.
8. **Remediation Testing:** Re-issue the modified request against the patched application to verify `403 Forbidden` enforcement.

## Security Notice

All sensitive authentication artifacts, including live JSON Web Tokens (JWTs), authorization headers, and session cookies, have been redacted (`[REDACTED]`) from public repository files to prevent session hijacking and credentials exposure.
