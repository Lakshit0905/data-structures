"""
SDET Problem: Validate JSON Schema
=====================================
Given a JSON response and a required schema definition, validate:
1. Required fields are present
2. Field types match expectations
3. Fields are not null when they shouldn't be
4. String fields meet minimum length requirements

Interview Explanation:
    JSON schema validation is critical in SDET API testing.
    A schema defines the contract — what fields must exist,
    their types, and constraints. This utility validates a
    JSON payload against that contract and reports violations.

SDET Use Case:
    After every API call in automated tests, validate the
    response schema before checking business logic values.
"""


def validate_json_schema(payload: dict, schema: dict) -> list:
    """
    Validate a JSON payload against a schema definition.

    Schema format:
    {
        "field_name": {
            "type": str/int/float/bool/list/dict,
            "required": True/False,
            "nullable": True/False,
            "min_length": int  (for strings)
        }
    }

    Returns a list of validation error messages.
    """
    errors = []

    for field, rules in schema.items():
        required = rules.get("required", True)
        nullable = rules.get("nullable", False)
        expected_type = rules.get("type")
        min_length = rules.get("min_length", 0)

        # Check required fields
        if field not in payload:
            if required:
                errors.append(f"MISSING REQUIRED FIELD: '{field}'")
            continue  # Skip further checks if field absent

        value = payload[field]

        # Check null values
        if value is None:
            if not nullable:
                errors.append(f"NULL NOT ALLOWED: '{field}' is null/None")
            continue  # No further checks on None

        # Check type
        if expected_type and not isinstance(value, expected_type):
            errors.append(
                f"TYPE MISMATCH: '{field}' expected {expected_type.__name__}, "
                f"got {type(value).__name__} (value={repr(value)})"
            )
            continue

        # Check string minimum length
        if expected_type == str and len(value) < min_length:
            errors.append(
                f"MIN LENGTH VIOLATION: '{field}' must be at least {min_length} chars "
                f"(got {len(value)}: '{value}')"
            )

    # Check for unexpected extra fields (optional — depends on your API contract)
    for field in payload:
        if field not in schema:
            errors.append(f"UNEXPECTED FIELD: '{field}' not in schema definition")

    return errors


def run_validation(payload: dict, schema: dict, test_name: str = "") -> bool:
    """Print validation results and return True if valid."""
    errors = validate_json_schema(payload, schema)
    label = f" [{test_name}]" if test_name else ""
    if not errors:
        print(f"✓ VALID{label}")
        return True
    else:
        print(f"✗ INVALID{label} — {len(errors)} error(s):")
        for e in errors:
            print(f"   → {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("SDET: JSON Schema Validation")
    print("=" * 60)

    # Define API response schema
    user_schema = {
        "user_id":    {"type": int,  "required": True,  "nullable": False},
        "username":   {"type": str,  "required": True,  "nullable": False, "min_length": 3},
        "email":      {"type": str,  "required": True,  "nullable": False, "min_length": 5},
        "age":        {"type": int,  "required": False, "nullable": True},
        "is_active":  {"type": bool, "required": True,  "nullable": False},
        "scores":     {"type": list, "required": False, "nullable": True},
    }

    # Test 1: Valid payload
    valid_payload = {
        "user_id": 1001,
        "username": "alice_smith",
        "email": "alice@test.com",
        "age": 30,
        "is_active": True,
        "scores": [95, 87, 92]
    }
    print()
    run_validation(valid_payload, user_schema, "Valid Payload")

    # Test 2: Missing required field
    missing_field = {
        "user_id": 1002,
        "email": "bob@test.com",
        "is_active": True
        # username is missing!
    }
    print()
    run_validation(missing_field, user_schema, "Missing 'username'")

    # Test 3: Type mismatch and null violation
    bad_types = {
        "user_id": "1003",     # should be int
        "username": "ca",       # too short (min_length=3)
        "email": "x@y.com",
        "is_active": None,      # nullable=False violation
    }
    print()
    run_validation(bad_types, user_schema, "Type Mismatches")
