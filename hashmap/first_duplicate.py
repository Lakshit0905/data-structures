"""
Problem: First Duplicate in an Array
======================================
Given an array, find the first element that appears more than once.
Return the element with the smallest second occurrence index.

Interview Explanation:
    Use a HashSet to track seen elements. As we iterate, if we encounter
    an element already in the set, it's the first duplicate we've seen
    in traversal order. This is O(n) time and O(n) space.

Example:
    Input:  [2, 1, 3, 5, 3, 2]
    Output: 3  (3 appears again at index 4 before 2 appears at index 5)

Time Complexity:  O(n)
Space Complexity: O(n)

SDET Use Case:
    Finding duplicate test case IDs or duplicate API request IDs in a log.
"""


def first_duplicate(arr: list):
    """
    HashSet approach — find first element seen twice.
    """
    seen = set()
    for item in arr:
        if item in seen:
            return item  # First duplicate found
        seen.add(item)
    return None  # No duplicates


def all_duplicates(arr: list) -> list:
    """
    Returns ALL elements that appear more than once.
    Useful for finding all duplicate test IDs.
    """
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return sorted(list(duplicates))


def find_duplicate_indices(arr: list) -> dict:
    """
    Returns a dict mapping each duplicate to all its indices.
    Great for SDET reporting: "which test IDs are duplicated and where?"
    """
    index_map = {}
    for i, item in enumerate(arr):
        if item not in index_map:
            index_map[item] = []
        index_map[item].append(i)

    return {k: v for k, v in index_map.items() if len(v) > 1}


if __name__ == "__main__":
    print("=" * 50)
    print("First Duplicate & Duplicate Finder")
    print("=" * 50)

    arr = [2, 1, 3, 5, 3, 2]
    print(f"Array: {arr}")
    print(f"First duplicate: {first_duplicate(arr)}")
    print(f"All duplicates:  {all_duplicates(arr)}")
    print(f"Duplicate indices: {find_duplicate_indices(arr)}")
    print()

    # SDET use case: duplicate test case IDs
    test_ids = ["TC001", "TC002", "TC003", "TC001", "TC004", "TC002"]
    print("SDET Use Case — Duplicate Test Case IDs:")
    print(f"Test IDs: {test_ids}")
    print(f"Duplicates found: {all_duplicates(test_ids)}")
    print(f"Duplicate detail: {find_duplicate_indices(test_ids)}")
