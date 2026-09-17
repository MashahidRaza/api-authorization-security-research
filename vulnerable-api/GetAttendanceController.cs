[HttpGet("GetAttendanceByUserId")]
public IActionResult GetAttendanceByUserId([FromQuery] string userId, [FromQuery] string date)
{
    // VULNERABLE: Directly trusts user input without validating JWT claims
    var attendanceData = FetchAttendanceFromDatabase(userId, date);
    return Ok(attendanceData);
}
