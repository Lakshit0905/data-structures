"""
Problem: Binary Search
=======================
Given a sorted array and a target value, return the index of the target.
If not found, return -1.

Interview Explanation:
    Binary search cuts the search space in half each iteration.
    Key: always work with SORTED arrays. Three pointers: low, high, mid.
    Compare target with mid: if less → search left half, if greater → right half.
    O(log n) time, O(1) space. Mention edge cases: empty array, target not found.

Example:
    Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4

Time Complexity:  O(log n)
Space Complexity: O(1) iterative, O(log n) recursive
"""


def binary_search(nums: list, target: int) -> int:
    """
    Iterative binary search. Preferred in interviews — no stack overhead.
    """
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Avoid overflow (safe even in Python)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1   # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found


def binary_search_recursive(nums: list, target: int, low: int = 0, high: int = None) -> int:
    """
    Recursive binary search. Good to know, but iterative is preferred.
    """
    if high is None:
        high = len(nums) - 1

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, high)
    else:
        return binary_search_recursive(nums, target, low, mid - 1)


def search_insert_position(nums: list, target: int) -> int:
    """
    Variant: if target not found, return where it would be inserted.
    Common follow-up question!
    """
    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]

    print("=" * 50)
    print("Binary Search")
    print("=" * 50)
    print(f"Array: {nums}")
    print()

    test_cases = [
        (9, 4),
        (-1, 0),
        (2, -1),
        (12, 5),
    ]

    for target, expected in test_cases:
        result = binary_search(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} target={target} → index {result} (expected: {expected})")

    print()
    print("Search Insert Position:")
    for target in [0, 1, 7, 13]:
        pos = search_insert_position(nums, target)
        print(f"  target={target} → insert at index {pos}")
