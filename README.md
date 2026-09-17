# api-authorization-security-research
Research-driven REST API security project for detecting and remediating Broken Object Level Authorization (BOLA) using authenticated differential testing, Burp Suite, and automated security validation

Vulnerability Title: Broken Object Level Authorization (BOLA) in GetAttendanceByUserId
Target Endpoint: GET /api/MobileApp/GetAttendanceByUserId
Vulnerable Parameter: userId
Summary of Finding:
An authenticated user (userId=14321) can manipulate the userId query parameter to 14324 while keeping their original JWT Bearer token. The API returns full attendance records and personal identifiers (userName: inspirer10044@inspirer.edu.pk) belonging to another user without performing backend authorization checks.
