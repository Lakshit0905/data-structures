"""
Problem: Contains Duplicate
============================
Given an integer array, return True if any value appears at least twice.

Interview Explanation:
    Use a HashSet. Add each element; if it's already in the set, return True.
    Alternatively, compare len(set(nums)) with len(nums).
    This is O(n) time and O(n) space.

Example:
    Input:  [1, 2, 3, 1]
    Output: True

    Input:  [1, 2, 3, 4]
    Output: False

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def contains_duplicate(nums: list) -> bool:
    """
    HashSet approach — O(n) time, O(n) space.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_pythonic(nums: list) -> bool:
    """
    Pythonic one-liner.
    """
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
    ]

    print("=" * 50)
    print("Contains Duplicate")
    print("=" * 50)

    for nums, expected in test_cases:
        result = contains_duplicate(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} → {result} (expected: {expected})")
