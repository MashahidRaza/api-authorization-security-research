#!/usr/bin/env python3

"""
Authenticated differential BOLA detector.

This tool is intended only for the controlled local laboratory API.

It compares:

1. An authorized baseline request
2. A cross-object request using the same authentication identity

The detector does not test production systems and does not contain
real JWTs, passwords, or personal data.
"""

from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class TestCase:
    name: str
    requesting_user_id: int
    target_user_id: int
    expected_authorized: bool


# Local laboratory endpoints only.
VULNERABLE_API_URL = "http://localhost:5001/api/attendance/by-user"
SECURE_API_URL = "http://localhost:5002/api/attendance/by-user"

TEST_DATE = "2026-01-01"

# These are synthetic lab tokens.
#
# Replace these values only after you configure your local API's
# authentication mechanism. Never place a real production JWT here.
SYNTHETIC_USER_A_TOKEN = "LAB_TOKEN_USER_A"
SYNTHETIC_USER_B_TOKEN = "LAB_TOKEN_USER_B"


def send_request(
    base_url: str,
    token: str,
    target_user_id: int,
) -> requests.Response:
    """
    Send one authenticated request to the local laboratory API.
    """

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    params = {
        "userId": str(target_user_id),
        "date": TEST_DATE,
    }

    return requests.get(
        base_url,
        headers=headers,
        params=params,
        timeout=5,
    )


def response_contains_target_user(
    response: requests.Response,
    target_user_id: int,
) -> bool:
    """
    Check whether the response contains the requested synthetic
    object identifier.

    This is a simple initial detector. It should later be improved
    with structured JSON parsing and ownership-aware comparisons.
    """

    target_value = str(target_user_id)

    return (
        response.status_code == 200
        and target_value in response.text
    )


def classify_result(
    response: requests.Response,
    requesting_user_id: int,
    target_user_id: int,
    expected_authorized: bool,
) -> str:
    """
    Classify the observed result against the known laboratory
    authorization ground truth.
    """

    object_returned = response_contains_target_user(
        response,
        target_user_id,
    )

    if expected_authorized:
        if response.status_code == 200 and object_returned:
            return "PASS: authorized access succeeded"

        return "FAIL: expected authorized access was not successful"

    if response.status_code in (401, 403):
        return "PASS: unauthorized access was denied"

    if object_returned:
        return "POTENTIAL BOLA: unauthorized object returned"

    return "REVIEW: response requires manual analysis"


def run_test_case(
    api_name: str,
    base_url: str,
    token: str,
    test_case: TestCase,
) -> None:
    """
    Execute and print one test case.
    """

    response = send_request(
        base_url=base_url,
        token=token,
        target_user_id=test_case.target_user_id,
    )

    classification = classify_result(
        response=response,
        requesting_user_id=test_case.requesting_user_id,
        target_user_id=test_case.target_user_id,
        expected_authorized=test_case.expected_authorized,
    )

    print(f"\nAPI: {api_name}")
    print(f"Test case: {test_case.name}")
    print(f"Requesting user: {test_case.requesting_user_id}")
    print(f"Target user: {test_case.target_user_id}")
    print(f"HTTP status: {response.status_code}")
    print(f"Classification: {classification}")


def main() -> None:
    """
    Run the initial four-case authorization matrix.
    """

    test_cases = [
        (
            "TC-01",
            SYNTHETIC_USER_A_TOKEN,
            TestCase(
                name="User A requests own object",
                requesting_user_id=1001,
                target_user_id=1001,
                expected_authorized=True,
            ),
        ),
        (
            "TC-02",
            SYNTHETIC_USER_A_TOKEN,
            TestCase(
                name="User A requests User B object",
                requesting_user_id=1001,
                target_user_id=1002,
                expected_authorized=False,
            ),
        ),
        (
            "TC-03",
            SYNTHETIC_USER_B_TOKEN,
            TestCase(
                name="User B requests own object",
                requesting_user_id=1002,
                target_user_id=1002,
                expected_authorized=True,
            ),
        ),
        (
            "TC-04",
            SYNTHETIC_USER_B_TOKEN,
            TestCase(
                name="User B requests User A object",
                requesting_user_id=1002,
                target_user_id=1001,
                expected_authorized=False,
            ),
        ),
    ]

    for test_name, token, test_case in test_cases:
        run_test_case(
            api_name="Vulnerable API",
            base_url=VULNERABLE_API_URL,
            token=token,
            test_case=test_case,
        )

        run_test_case(
            api_name="Secure API",
            base_url=SECURE_API_URL,
            token=token,
            test_case=test_case,
        )


if __name__ == "__main__":
    main()
