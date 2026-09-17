# BOLA Differential Response Comparison

This document analyzes the HTTP response behavior when manipulating the client-controlled object parameter `userId` while maintaining a constant authentication token.

---

## 1. Baseline Request (`userId=14321`)

* **Endpoint:** `GET /api/MobileApp/GetAttendanceByUserId?userId=14321&date=01-01-2026`
* **Authenticated Token Identity:** User `14321`
* **HTTP Status Code:** `200 OK`
* **Response Payload:**

```json
{
  "overAll": [
    {
      "userId": 14321,
      "userName": "inspirer10042@inspirer.edu.pk",
      "studentCode": 10042,
      "attendanceMonth": 1,
      "monthName": "January",
      "attendanceYear": 2026,
      "workingDays": 2,
      "presentDays": 2,
      "attendancePercentage": 100
    }
  ]
}
