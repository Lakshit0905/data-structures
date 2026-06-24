"""
SDET Problem: Compare Two Lists
==================================
Given two lists (e.g., expected test data vs actual API response list),
find items only in list1, only in list2, and items in both.

Also find differences in values for matching items (useful for
comparing DB records vs API response records by ID).

Interview Explanation:
    Use set operations for O(n) comparison.
    For record-level comparison (list of dicts), match by a key field
    (like "id") and compare field-by-field.

SDET Use Case:
    Compare DB query results with API response data to validate
    data consistency in integration tests.
"""


def compare_simple_lists(list1: list, list2: list, label1: str = "List1", label2: str = "List2") -> dict:
    """
    Compare two flat lists. Returns sets of added/removed/common items.
    """
    set1 = set(list1)
    set2 = set(list2)

    return {
        "only_in_list1": sorted(set1 - set2),
        "only_in_list2": sorted(set2 - set1),
        "in_both": sorted(set1 & set2),
        "label1": label1,
        "label2": label2
    }


def compare_record_lists(list1: list, list2: list, key_field: str) -> dict:
    """
    Compare two lists of dicts by a key field (e.g., "id").
    Returns:
      - records only in list1 (deleted)
      - records only in list2 (added)
      - records with field-level differences
    """
    map1 = {r[key_field]: r for r in list1}
    map2 = {r[key_field]: r for r in list2}

    keys1 = set(map1.keys())
    keys2 = set(map2.keys())

    only_in_1 = [map1[k] for k in keys1 - keys2]
    only_in_2 = [map2[k] for k in keys2 - keys1]

    mismatches = []
    for key in keys1 & keys2:
        rec1, rec2 = map1[key], map2[key]
        diffs = {}
        for field in set(rec1.keys()) | set(rec2.keys()):
            v1 = rec1.get(field)
            v2 = rec2.get(field)
            if v1 != v2:
                diffs[field] = {"expected": v1, "actual": v2}
        if diffs:
            mismatches.append({key_field: key, "differences": diffs})

    return {
        "only_in_source": only_in_1,
        "only_in_target": only_in_2,
        "mismatches": mismatches
    }


def print_comparison_report(result: dict):
    """Pretty-print a comparison report."""
    if "label1" in result:
        print(f"Only in {result['label1']}: {result['only_in_list1']}")
        print(f"Only in {result['label2']}: {result['only_in_list2']}")
        print(f"In both: {result['in_both']}")
    else:
        if result["only_in_source"]:
            print(f"  Missing from target ({len(result['only_in_source'])} records):")
            for r in result["only_in_source"]:
                print(f"    {r}")
        if result["only_in_target"]:
            print(f"  Extra in target ({len(result['only_in_target'])} records):")
            for r in result["only_in_target"]:
                print(f"    {r}")
        if result["mismatches"]:
            print(f"  Field mismatches ({len(result['mismatches'])} records):")
            for m in result["mismatches"]:
                print(f"    ID={m['id']}: {m['differences']}")
        if not any([result["only_in_source"], result["only_in_target"], result["mismatches"]]):
            print("  ✓ All records match!")


if __name__ == "__main__":
    print("=" * 60)
    print("SDET: Compare Two Lists")
    print("=" * 60)

    # Test 1: Simple list comparison (e.g., test case IDs)
    db_test_ids = ["TC001", "TC002", "TC003", "TC004", "TC005"]
    api_test_ids = ["TC001", "TC002", "TC004", "TC006"]

    print("\nTest 1: Compare Test Case ID lists")
    result = compare_simple_lists(db_test_ids, api_test_ids, "DB", "API")
    print_comparison_report(result)

    # Test 2: Record-level comparison (DB vs API response)
    db_records = [
        {"id": 1, "name": "Alice", "status": "ACTIVE",   "score": 95},
        {"id": 2, "name": "Bob",   "status": "INACTIVE", "score": 80},
        {"id": 3, "name": "Carol", "status": "ACTIVE",   "score": 88},
        {"id": 4, "name": "David", "status": "ACTIVE",   "score": 72},
    ]
    api_records = [
        {"id": 1, "name": "Alice", "status": "ACTIVE",   "score": 95},
        {"id": 2, "name": "Bob",   "status": "ACTIVE",   "score": 80},  # status changed!
        {"id": 3, "name": "Carol", "status": "ACTIVE",   "score": 90},  # score changed!
        # id=4 missing from API!
        {"id": 5, "name": "Eve",   "status": "ACTIVE",   "score": 65},  # extra in API!
    ]

    print("\nTest 2: DB vs API Record Comparison")
    result2 = compare_record_lists(db_records, api_records, key_field="id")
    print_comparison_report(result2)
