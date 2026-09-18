using System.Security.Claims;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace SecureApi.Controllers
{
    [ApiController]
    [Route("api/attendance")]
    [Authorize]
    public class GetAttendanceController : ControllerBase
    {
        [HttpGet("by-user")]
        public IActionResult GetAttendanceByUserId(
            [FromQuery] int userId,
            [FromQuery] string date)
        {
            /*
             * SECURE IMPLEMENTATION
             *
             * The endpoint requires authentication and verifies that
             * the requested userId matches the authenticated identity.
             */

            var authenticatedUserId =
                User.FindFirst(ClaimTypes.NameIdentifier)?.Value
                ?? User.FindFirst("sub")?.Value;

            if (!int.TryParse(authenticatedUserId, out var tokenUserId))
            {
                return Unauthorized(new
                {
                    message = "The authenticated identity is missing or invalid."
                });
            }

            /*
             * Object-level authorization check.
             *
             * A normal user may access only their own attendance data.
             */

            if (tokenUserId != userId)
            {
                return StatusCode(403, new
                {
                    message = "Forbidden: access to this object is not allowed."
                });
            }

            var attendanceData = FetchAttendanceFromDatabase(userId, date);

            return Ok(attendanceData);
        }

        private static object FetchAttendanceFromDatabase(
            int userId,
            string date)
        {
            /*
             * The secure API uses the same synthetic data as the
             * vulnerable API. The important difference is the
             * authorization check before this method is called.
             */

            var records = new[]
            {
                new
                {
                    UserId = 1001,
                    StudentName = "Synthetic User A",
                    Date = "2026-01-01",
                    AttendanceStatus = "Present"
                },
                new
                {
                    UserId = 1002,
                    StudentName = "Synthetic User B",
                    Date = "2026-01-01",
                    AttendanceStatus = "Absent"
                }
            };

            var result = records.FirstOrDefault(
                record => record.UserId == userId &&
                          record.Date == date);

            if (result == null)
            {
                return new
                {
                    UserId = userId,
                    Date = date,
                    Records = Array.Empty<object>()
                };
            }

            return new
            {
                UserId = result.UserId,
                StudentName = result.StudentName,
                Date = result.Date,
                AttendanceStatus = result.AttendanceStatus
            };
        }
    }
}
