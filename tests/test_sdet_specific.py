"""
Pytest Tests: SDET-Specific Coding Problems
=============================================
Unit tests for all sdet_specific/ modules.
Run with: pytest tests/test_sdet_specific.py -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from sdet_specific.compare_api_response import compare_api_response
from sdet_specific.validate_json_schema import validate_json_schema
from sdet_specific.find_missing_keys import find_missing_keys, find_missing_keys_nested
from sdet_specific.compare_two_lists import compare_simple_lists, compare_record_lists
from sdet_specific.parse_log_file import parse_log_lines, generate_test_summary
from sdet_specific.test_data_generator import (
    generate_user, generate_users, generate_test_case_ids,
    generate_email, generate_phone
)


# ── compare_api_response ──────────────────────────────────────

class TestCompareApiResponse:
    def test_identical_responses(self):
        expected = {"status": "success", "code": 200}
        actual   = {"status": "success", "code": 200}
        assert compare_api_response(expected, actual) == []

    def test_value_mismatch(self):
        expected = {"status": "success", "code": 200}
        actual   = {"status": "error",   "code": 500}
        diffs = compare_api_response(expected, actual)
        assert len(diffs) == 2
        assert any("status" in d for d in diffs)
        assert any("code" in d for d in diffs)

    def test_missing_key_in_actual(self):
        expected = {"status": "success", "data": {"user_id": 1}}
        actual   = {"status": "success"}
        diffs = compare_api_response(expected, actual)
        assert any("MISSING" in d for d in diffs)

    def test_extra_key_in_actual(self):
        expected = {"status": "success"}
        actual   = {"status": "success", "extra_field": "unexpected"}
        diffs = compare_api_response(expected, actual)
        assert any("EXTRA" in d for d in diffs)

    def test_nested_mismatch(self):
        expected = {"data": {"user": {"role": "admin"}}}
        actual   = {"data": {"user": {"role": "user"}}}
        diffs = compare_api_response(expected, actual)
        assert len(diffs) == 1
        assert "role" in diffs[0]

    def test_nested_identical(self):
        payload = {"data": {"user": {"id": 1, "name": "Alice"}}}
        assert compare_api_response(payload, payload) == []


# ── validate_json_schema ──────────────────────────────────────

class TestValidateJsonSchema:
    def setup_method(self):
        self.schema = {
            "user_id":   {"type": int,  "required": True,  "nullable": False},
            "username":  {"type": str,  "required": True,  "nullable": False, "min_length": 3},
            "email":     {"type": str,  "required": True,  "nullable": False},
            "is_active": {"type": bool, "required": True,  "nullable": False},
            "age":       {"type": int,  "required": False, "nullable": True},
        }

    def test_valid_payload(self):
        payload = {
            "user_id": 1, "username": "alice", "email": "alice@test.com", "is_active": True
        }
        assert validate_json_schema(payload, self.schema) == []

    def test_missing_required_field(self):
        payload = {"user_id": 1, "email": "alice@test.com", "is_active": True}
        errors = validate_json_schema(payload, self.schema)
        assert any("username" in e for e in errors)

    def test_type_mismatch(self):
        payload = {
            "user_id": "not_an_int", "username": "alice",
            "email": "alice@test.com", "is_active": True
        }
        errors = validate_json_schema(payload, self.schema)
        assert any("TYPE MISMATCH" in e for e in errors)

    def test_null_not_allowed(self):
        payload = {
            "user_id": 1, "username": "alice",
            "email": "alice@test.com", "is_active": None
        }
        errors = validate_json_schema(payload, self.schema)
        assert any("NULL NOT ALLOWED" in e for e in errors)

    def test_min_length_violation(self):
        payload = {
            "user_id": 1, "username": "ab",  # too short
            "email": "alice@test.com", "is_active": True
        }
        errors = validate_json_schema(payload, self.schema)
        assert any("MIN LENGTH" in e for e in errors)

    def test_nullable_field_can_be_none(self):
        payload = {
            "user_id": 1, "username": "alice",
            "email": "alice@test.com", "is_active": True,
            "age": None  # nullable=True → allowed
        }
        errors = validate_json_schema(payload, self.schema)
        assert not any("age" in e for e in errors)


# ── find_missing_keys ─────────────────────────────────────────

class TestFindMissingKeys:
    def test_no_missing(self):
        response = {"id": 1, "name": "Alice", "email": "a@test.com"}
        required = ["id", "name", "email"]
        assert find_missing_keys(response, required) == []

    def test_some_missing(self):
        response = {"id": 1, "name": "Alice"}
        required = ["id", "name", "email", "status"]
        missing = find_missing_keys(response, required)
        assert "email" in missing
        assert "status" in missing
        assert "id" not in missing

    def test_all_missing(self):
        response = {}
        required = ["id", "name"]
        assert set(find_missing_keys(response, required)) == {"id", "name"}

    def test_nested_no_missing(self):
        response = {"data": {"user": {"id": 1, "name": "Alice"}}}
        required = ["data.user.id", "data.user.name"]
        assert find_missing_keys_nested(response, required) == []

    def test_nested_some_missing(self):
        response = {"data": {"user": {"id": 1}}}
        required = ["data.user.id", "data.user.email"]
        missing = find_missing_keys_nested(response, required)
        assert "data.user.email" in missing
        assert "data.user.id" not in missing

    def test_nested_path_not_exist(self):
        response = {"status": "ok"}
        required = ["data.user.id"]
        assert "data.user.id" in find_missing_keys_nested(response, required)


# ── compare_two_lists ─────────────────────────────────────────

class TestCompareTwoLists:
    def test_identical_lists(self):
        result = compare_simple_lists([1, 2, 3], [1, 2, 3])
        assert result["only_in_list1"] == []
        assert result["only_in_list2"] == []
        assert sorted(result["in_both"]) == [1, 2, 3]

    def test_disjoint_lists(self):
        result = compare_simple_lists([1, 2], [3, 4])
        assert sorted(result["only_in_list1"]) == [1, 2]
        assert sorted(result["only_in_list2"]) == [3, 4]
        assert result["in_both"] == []

    def test_partial_overlap(self):
        result = compare_simple_lists([1, 2, 3], [2, 3, 4])
        assert result["only_in_list1"] == [1]
        assert result["only_in_list2"] == [4]
        assert sorted(result["in_both"]) == [2, 3]

    def test_record_comparison_identical(self):
        records = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        result = compare_record_lists(records, records, "id")
        assert result["only_in_source"] == []
        assert result["only_in_target"] == []
        assert result["mismatches"] == []

    def test_record_comparison_mismatch(self):
        source = [{"id": 1, "status": "ACTIVE"}]
        target = [{"id": 1, "status": "INACTIVE"}]
        result = compare_record_lists(source, target, "id")
        assert len(result["mismatches"]) == 1
        assert "status" in result["mismatches"][0]["differences"]

    def test_record_missing_from_target(self):
        source = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        target = [{"id": 1, "name": "Alice"}]
        result = compare_record_lists(source, target, "id")
        assert len(result["only_in_source"]) == 1
        assert result["only_in_source"][0]["id"] == 2


# ── parse_log_file ────────────────────────────────────────────

class TestParseLogFile:
    def setup_method(self):
        self.log_text = """
[2024-01-15 10:30:01] [PASS]  TestLogin.test_valid
[2024-01-15 10:30:03] [PASS]  TestLogin.test_remember
[2024-01-15 10:30:05] [FAIL]  TestLogin.test_invalid - AssertionError: Expected 401
[2024-01-15 10:30:10] [SKIP]  TestPayment.test_credit - Skipped: flag disabled
[2024-01-15 10:30:12] [ERROR] TestAPI.test_timeout - ConnectionError: timed out
""".strip()

    def test_parse_count(self):
        records = parse_log_lines(self.log_text)
        assert len(records) == 5

    def test_status_parsing(self):
        records = parse_log_lines(self.log_text)
        statuses = [r["status"] for r in records]
        assert statuses.count("PASS") == 2
        assert statuses.count("FAIL") == 1
        assert statuses.count("SKIP") == 1
        assert statuses.count("ERROR") == 1

    def test_summary_totals(self):
        records = parse_log_lines(self.log_text)
        summary = generate_test_summary(records)
        assert summary["total"] == 5
        assert summary["passed"] == 2
        assert summary["failed"] == 1
        assert summary["skipped"] == 1
        assert summary["errored"] == 1

    def test_pass_rate(self):
        records = parse_log_lines(self.log_text)
        summary = generate_test_summary(records)
        assert summary["pass_rate"] == 40.0

    def test_failed_tests_list(self):
        records = parse_log_lines(self.log_text)
        summary = generate_test_summary(records)
        assert len(summary["failed_tests"]) == 1
        assert "TestLogin.test_invalid" in summary["failed_tests"][0]["test_name"]

    def test_empty_log(self):
        records = parse_log_lines("")
        summary = generate_test_summary(records)
        assert summary["total"] == 0
        assert summary["pass_rate"] == 0


# ── test_data_generator ───────────────────────────────────────

class TestTestDataGenerator:
    def test_user_has_required_fields(self):
        user = generate_user(1)
        required = ["user_id", "first_name", "last_name", "email", "phone", "status"]
        for field in required:
            assert field in user, f"Missing field: {field}"

    def test_user_id_correct(self):
        user = generate_user(42)
        assert user["user_id"] == 42

    def test_generate_multiple_users(self):
        users = generate_users(10)
        assert len(users) == 10
        # All user IDs should be unique
        ids = [u["user_id"] for u in users]
        assert len(set(ids)) == 10

    def test_email_format(self):
        email = generate_email("Alice", "Smith")
        assert "@" in email
        assert "." in email.split("@")[1]

    def test_phone_format(self):
        phone = generate_phone()
        parts = phone.split("-")
        assert len(parts) == 3

    def test_test_case_ids(self):
        ids = generate_test_case_ids("TC", 5)
        assert ids == ["TC001", "TC002", "TC003", "TC004", "TC005"]

    def test_test_case_ids_custom_prefix(self):
        ids = generate_test_case_ids("REG", 3)
        assert ids[0] == "REG001"
        assert ids[2] == "REG003"

    def test_user_status_valid(self):
        valid_statuses = {"ACTIVE", "INACTIVE", "PENDING", "SUSPENDED"}
        for _ in range(20):
            user = generate_user()
            assert user["status"] in valid_statuses
