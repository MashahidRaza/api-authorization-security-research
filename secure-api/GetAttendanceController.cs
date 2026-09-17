using System.Security.Claims;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace Api.Controllers
{
    [ApiController]
    [Route("api/MobileApp")]
    [Authorize] // Enforces authentication
    public class MobileAppController : ControllerBase
    {
        [HttpGet("GetAttendanceByUserId")]
        public IActionResult GetAttendanceByUserId([FromQuery] string userId, [FromQuery] string date)
        {
            // Extract the authenticated User ID directly from the JWT sub/NameIdentifier claim
            var tokenUserId = User.FindFirst(ClaimTypes.NameIdentifier)?.Value 
                              ?? User.FindFirst("sub")?.Value;

            // BOLA Mitigation: Validate that the requested userId matches the JWT claim ID
            if (string.IsNullOrEmpty(tokenUserId) || !tokenUserId.Equals(userId, StringComparison.OrdinalIgnoreCase))
            {
                // Return 403 Forbidden if an authenticated user attempts to read another user's data
                return StatusCode(403, new { message = "Forbidden: Unauthorized access to target resource." });
            }

            // Proceed with fetching attendance data safely
            var attendanceData = FetchAttendanceFromDatabase(userId, date);
            return Ok(attendanceData);
        }

        private object FetchAttendanceFromDatabase(string userId, string date)
        {
            // Database lookup logic
            return new { userId = userId, status = "Success" };
        }
    }
}
