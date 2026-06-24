"""
SDET Problem: Compare Expected vs Actual API Response
======================================================
Given an expected API response dict and an actual API response dict,
identify all differences: mismatched values, missing keys, extra keys.

Interview Explanation:
    This is a core SDET skill — API response validation.
    Compare expected vs actual key-by-key. Report:
    - Keys in expected but missing from actual (missing keys)
    - Keys in actual but not in expected (extra/unexpected keys)
    - Keys present in both but with different values (mismatches)
    Recurse for nested dicts.

SDET Use Case:
    After an API call, assert the response matches the contract.
    This utility generates a human-readable diff report.
"""


def compare_api_response(expected: dict, actual: dict, path: str = "") -> list:
    """
    Recursively compare expected vs actual API response dicts.
    Returns a list of difference strings.
    """
    differences = []

    expected_keys = set(expected.keys())
    actual_keys = set(actual.keys())

    # Keys missing from actual
    for key in expected_keys - actual_keys:
        full_path = f"{path}.{key}" if path else key
        differences.append(f"MISSING KEY:   '{full_path}' not found in actual response")

    # Unexpected keys in actual
    for key in actual_keys - expected_keys:
        full_path = f"{path}.{key}" if path else key
        differences.append(f"EXTRA KEY:     '{full_path}' found in actual but not in expected")

    # Compare values for keys present in both
    for key in expected_keys & actual_keys:
        full_path = f"{path}.{key}" if path else key
        exp_val = expected[key]
        act_val = actual[key]

        if isinstance(exp_val, dict) and isinstance(act_val, dict):
            # Recurse into nested dicts
            differences.extend(compare_api_response(exp_val, act_val, full_path))
        elif exp_val != act_val:
            differences.append(
                f"VALUE MISMATCH: '{full_path}' → expected={repr(exp_val)}, actual={repr(act_val)}"
            )

    return differences


def assert_api_response(expected: dict, actual: dict) -> bool:
    """
    Wrapper that prints a validation report and returns True if no differences.
    """
    diffs = compare_api_response(expected, actual)

    if not diffs:
        print("✓ API Response PASSED — All fields match")
        return True
    else:
        print(f"✗ API Response FAILED — {len(diffs)} difference(s) found:")
        for diff in diffs:
            print(f"  → {diff}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("SDET: Compare API Expected vs Actual Response")
    print("=" * 60)

    # Test Case 1: Matching responses
    expected_1 = {
        "status": "success",
        "code": 200,
        "data": {
            "user_id": 42,
            "name": "Alice Smith",
            "role": "admin"
        }
    }
    actual_1 = {
        "status": "success",
        "code": 200,
        "data": {
            "user_id": 42,
            "name": "Alice Smith",
            "role": "admin"
        }
    }
    print("\nTest 1: Matching responses")
    assert_api_response(expected_1, actual_1)

    # Test Case 2: Mismatches and missing keys
    expected_2 = {
        "status": "success",
        "code": 200,
        "data": {
            "user_id": 42,
            "name": "Alice Smith",
            "role": "admin",
            "email": "alice@test.com"
        }
    }
    actual_2 = {
        "status": "error",           # Value mismatch
        "code": 500,                 # Value mismatch
        "data": {
            "user_id": 42,
            "name": "Alice Smith",
            "role": "user",          # Value mismatch
            # email is MISSING
        },
        "timestamp": "2024-01-01"   # Extra key
    }
    print("\nTest 2: Multiple differences")
    assert_api_response(expected_2, actual_2)
