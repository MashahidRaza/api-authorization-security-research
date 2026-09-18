using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace VulnerableApi.Controllers
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
             * INTENTIONALLY VULNERABLE
             *
             * The endpoint requires authentication, but it does not
             * verify whether the authenticated user owns the requested
             * userId.
             *
             * A token belonging to User A can request User B's data
             * by changing the userId parameter.
             */

            var attendanceData = FetchAttendanceFromDatabase(userId, date);

            return Ok(attendanceData);
        }

        private static object FetchAttendanceFromDatabase(
            int userId,
            string date)
        {
            /*
             * Synthetic laboratory data only.
             *
             * This data does not represent real students or production
             * records.
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
