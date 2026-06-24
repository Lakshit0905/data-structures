"""
SDET Problem: Parse Automation Log File
=========================================
Given a list of log lines from a test automation run,
parse them to extract test results, count pass/fail/skip,
find failed test names, and calculate pass rate.

Interview Explanation:
    Log parsing is a very common SDET coding problem. Use string parsing
    and regex to extract structured data from unstructured log lines.
    Key skills: split(), strip(), re.search(), dict/Counter.

SDET Use Case:
    After a CI/CD test run, parse the log to generate a summary report
    or trigger alerts when failure rate exceeds a threshold.
"""

import re
from collections import Counter


# Sample log format:
# [2024-01-15 10:30:01] [PASS] TestLogin.test_valid_credentials
# [2024-01-15 10:30:05] [FAIL] TestLogin.test_invalid_password - AssertionError: Expected 401, got 200
# [2024-01-15 10:30:10] [SKIP] TestPayment.test_credit_card - Skipped: feature flag disabled
# [2024-01-15 10:30:12] [ERROR] TestAPI.test_timeout - ConnectionError: Request timed out

SAMPLE_LOG = """
[2024-01-15 10:30:01] [PASS]  TestLogin.test_valid_credentials
[2024-01-15 10:30:03] [PASS]  TestLogin.test_remember_me
[2024-01-15 10:30:05] [FAIL]  TestLogin.test_invalid_password - AssertionError: Expected 401, got 200
[2024-01-15 10:30:08] [PASS]  TestUser.test_create_user
[2024-01-15 10:30:10] [SKIP]  TestPayment.test_credit_card - Skipped: feature flag disabled
[2024-01-15 10:30:12] [FAIL]  TestAPI.test_get_users - AssertionError: Expected 10 items, got 9
[2024-01-15 10:30:15] [PASS]  TestUser.test_update_user
[2024-01-15 10:30:17] [ERROR] TestAPI.test_timeout - ConnectionError: Request timed out
[2024-01-15 10:30:20] [FAIL]  TestSearch.test_empty_query - ValueError: Empty search not handled
[2024-01-15 10:30:22] [PASS]  TestSearch.test_basic_search
[2024-01-15 10:30:25] [SKIP]  TestAdmin.test_delete_user - Skipped: requires admin role
[2024-01-15 10:30:27] [PASS]  TestUser.test_delete_user
""".strip()


def parse_log_lines(log_text: str) -> list:
    """
    Parse raw log text into a list of structured records.
    Returns list of dicts: {timestamp, status, test_name, message}
    """
    pattern = r'\[(.+?)\]\s+\[(\w+)\]\s+([\w.]+)(?:\s+-\s+(.+))?'
    records = []

    for line in log_text.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        match = re.match(pattern, line)
        if match:
            records.append({
                "timestamp": match.group(1),
                "status":    match.group(2),
                "test_name": match.group(3),
                "message":   match.group(4) or ""
            })

    return records


def generate_test_summary(records: list) -> dict:
    """
    Generate a summary report from parsed log records.
    """
    status_counts = Counter(r["status"] for r in records)
    total = len(records)

    failed_tests  = [r for r in records if r["status"] == "FAIL"]
    errored_tests = [r for r in records if r["status"] == "ERROR"]
    skipped_tests = [r for r in records if r["status"] == "SKIP"]

    passed = status_counts.get("PASS", 0)
    pass_rate = round((passed / total * 100), 1) if total > 0 else 0

    return {
        "total":         total,
        "passed":        passed,
        "failed":        status_counts.get("FAIL", 0),
        "skipped":       status_counts.get("SKIP", 0),
        "errored":       status_counts.get("ERROR", 0),
        "pass_rate":     pass_rate,
        "failed_tests":  failed_tests,
        "errored_tests": errored_tests,
        "skipped_tests": skipped_tests,
    }


def print_summary_report(summary: dict):
    """Print a human-readable test summary report."""
    print("\n" + "=" * 50)
    print("TEST EXECUTION SUMMARY")
    print("=" * 50)
    print(f"Total Tests  : {summary['total']}")
    print(f"Passed       : {summary['passed']} ✓")
    print(f"Failed       : {summary['failed']} ✗")
    print(f"Errors       : {summary['errored']} ⚠")
    print(f"Skipped      : {summary['skipped']} ○")
    print(f"Pass Rate    : {summary['pass_rate']}%")

    if summary["failed_tests"]:
        print("\nFAILED TESTS:")
        for t in summary["failed_tests"]:
            print(f"  ✗ {t['test_name']}")
            if t["message"]:
                print(f"    └── {t['message']}")

    if summary["errored_tests"]:
        print("\nERROR TESTS:")
        for t in summary["errored_tests"]:
            print(f"  ⚠ {t['test_name']}")
            if t["message"]:
                print(f"    └── {t['message']}")

    # Alert if pass rate is below threshold
    if summary["pass_rate"] < 80:
        print(f"\n⚠️  ALERT: Pass rate {summary['pass_rate']}% is below 80% threshold!")


if __name__ == "__main__":
    print("SDET: Parse Automation Log File")
    records = parse_log_lines(SAMPLE_LOG)
    summary = generate_test_summary(records)
    print_summary_report(summary)
