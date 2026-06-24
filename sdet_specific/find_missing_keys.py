"""
SDET Problem: Find Missing Keys in API Response
=================================================
Given an expected set of keys and an actual JSON/dict response,
find which required keys are missing.

Interview Explanation:
    Use set difference: expected_keys - actual_keys = missing keys.
    Support both flat and nested (dot-notation) key checking.
    Return clear error messages per missing key.

SDET Use Case:
    After hitting a GET /user endpoint, assert all mandatory
    fields like user_id, email, status are in the response.
"""


def find_missing_keys(response: dict, required_keys: list) -> list:
    """
    Flat key check: find required keys missing from response.
    Returns list of missing key names.
    """
    return [key for key in required_keys if key not in response]


def find_missing_keys_nested(response: dict, required_paths: list) -> list:
    """
    Nested key check using dot notation paths.
    e.g., "data.user.email" checks response["data"]["user"]["email"]

    Returns list of missing dot-notation paths.
    """
    missing = []
    for path in required_paths:
        keys = path.split(".")
        current = response
        found = True
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                found = False
                break
            current = current[key]
        if not found:
            missing.append(path)
    return missing


def validate_required_fields(response: dict, required_keys: list) -> bool:
    """
    Validate and print report. Returns True if all keys present.
    """
    missing = find_missing_keys(response, required_keys)
    if not missing:
        print(f"✓ All {len(required_keys)} required keys present")
        return True
    else:
        print(f"✗ {len(missing)} required key(s) missing:")
        for key in missing:
            print(f"   → '{key}'")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("SDET: Find Missing Keys in API Response")
    print("=" * 60)

    # Test 1: Flat key validation
    api_response = {
        "user_id": 101,
        "username": "alice",
        "is_active": True
        # "email" and "role" are missing!
    }
    required = ["user_id", "username", "email", "is_active", "role"]

    print("\nTest 1: Flat key check")
    print(f"Response keys: {list(api_response.keys())}")
    print(f"Required keys: {required}")
    validate_required_fields(api_response, required)

    # Test 2: Nested key validation (dot notation)
    nested_response = {
        "status": "success",
        "data": {
            "user": {
                "id": 42,
                "name": "Bob"
                # "email" missing at data.user.email
            }
        }
        # "meta.page" path missing entirely
    }
    required_paths = [
        "status",
        "data.user.id",
        "data.user.name",
        "data.user.email",  # MISSING
        "meta.page"         # MISSING
    ]

    print("\nTest 2: Nested dot-notation check")
    missing_nested = find_missing_keys_nested(nested_response, required_paths)
    if missing_nested:
        print(f"✗ Missing nested paths: {missing_nested}")
    else:
        print("✓ All nested paths present")
