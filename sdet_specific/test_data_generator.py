"""
SDET Problem: Test Data Generator
====================================
Generate realistic test data for users, API payloads, and test cases
without relying on external libraries (pure Python version).

Interview Explanation:
    SDETs often need to generate test data programmatically.
    Key skills: random module, string formatting, list comprehensions.
    In real projects you'd use Faker library — mention that in interviews.

SDET Use Case:
    Generate 100 user records for load testing, create test payloads
    for API fuzz testing, or populate a test database.
"""

import random
import string
import uuid
from datetime import datetime, timedelta


# ── Simple test data generators (no external dependencies) ───

FIRST_NAMES = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace",
               "Henry", "Iris", "Jack", "Karen", "Leo", "Mia", "Noah", "Olivia"]

LAST_NAMES = ["Smith", "Jones", "White", "Brown", "Davis", "Miller", "Wilson",
              "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "Harris"]

DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "test.com", "company.com"]

STATUSES = ["ACTIVE", "INACTIVE", "PENDING", "SUSPENDED"]

DEPARTMENTS = ["Engineering", "QA", "HR", "Finance", "Marketing", "Sales"]


def generate_email(first: str, last: str) -> str:
    """Generate a realistic email address."""
    domain = random.choice(DOMAINS)
    suffix = random.randint(1, 999)
    return f"{first.lower()}.{last.lower()}{suffix}@{domain}"


def generate_phone() -> str:
    """Generate a US-style phone number."""
    area = random.randint(200, 999)
    prefix = random.randint(200, 999)
    line = random.randint(1000, 9999)
    return f"{area}-{prefix}-{line}"


def generate_random_string(length: int = 8) -> str:
    """Generate a random alphanumeric string."""
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_random_date(start_year: int = 2020, end_year: int = 2024) -> str:
    """Generate a random date string."""
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")


def generate_user(user_id: int = None) -> dict:
    """Generate a single realistic user record."""
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    uid = user_id or random.randint(10000, 99999)

    return {
        "user_id":    uid,
        "first_name": first,
        "last_name":  last,
        "email":      generate_email(first, last),
        "phone":      generate_phone(),
        "status":     random.choice(STATUSES),
        "department": random.choice(DEPARTMENTS),
        "salary":     round(random.uniform(50000, 150000), 2),
        "hire_date":  generate_random_date(),
        "uuid":       str(uuid.uuid4()),
    }


def generate_users(count: int) -> list:
    """Generate a list of user records."""
    return [generate_user(user_id=i + 1) for i in range(count)]


def generate_api_payload(endpoint: str) -> dict:
    """Generate a test API request payload for common endpoints."""
    payloads = {
        "create_user": {
            "username":   generate_random_string(8),
            "email":      f"test_{generate_random_string(5)}@test.com",
            "password":   generate_random_string(12),
            "first_name": random.choice(FIRST_NAMES),
            "last_name":  random.choice(LAST_NAMES),
            "role":       random.choice(["admin", "user", "viewer"]),
        },
        "login": {
            "username": generate_random_string(8),
            "password": generate_random_string(12),
        },
        "search": {
            "query":    generate_random_string(5),
            "page":     random.randint(1, 10),
            "per_page": random.choice([10, 20, 50]),
            "sort_by":  random.choice(["name", "date", "relevance"]),
        }
    }
    return payloads.get(endpoint, {})


def generate_test_case_ids(prefix: str, count: int) -> list:
    """Generate sequential test case IDs."""
    return [f"{prefix}{str(i).zfill(3)}" for i in range(1, count + 1)]


if __name__ == "__main__":
    print("=" * 60)
    print("SDET: Test Data Generator")
    print("=" * 60)

    # Generate single user
    print("\n1. Single User Record:")
    user = generate_user(1)
    for k, v in user.items():
        print(f"   {k}: {v}")

    # Generate multiple users
    print(f"\n2. Generated 5 users:")
    users = generate_users(5)
    for u in users:
        print(f"   [{u['user_id']}] {u['first_name']} {u['last_name']} | {u['email']} | {u['status']}")

    # Generate API payloads
    print("\n3. API Payloads:")
    for ep in ["create_user", "login", "search"]:
        print(f"\n   Endpoint: {ep}")
        payload = generate_api_payload(ep)
        for k, v in payload.items():
            print(f"     {k}: {v}")

    # Generate test case IDs
    print("\n4. Test Case IDs:")
    tc_ids = generate_test_case_ids("TC", 10)
    print(f"   {tc_ids}")
