"""
Problem: Remove Duplicates from Sorted Array
=============================================
Given a sorted integer array, remove duplicates in-place such that each
element appears only once. Return the length of the new array.

Interview Explanation:
    Since the array is sorted, duplicates are adjacent. Use a slow pointer
    to track the "write position" and a fast pointer to scan. When fast
    finds a new unique value (different from slow), write it at slow+1.
    This is an O(n) in-place solution with O(1) space.

Example:
    Input:  nums = [1, 1, 2, 3, 3, 4]
    Output: 4, and nums becomes [1, 2, 3, 4, ...]

Time Complexity:  O(n) - single pass
Space Complexity: O(1) - in-place, no extra array
"""


def remove_duplicates(nums: list) -> int:
    """
    Two-pointer in-place approach for sorted array.
    slow = write position, fast = read position.
    """
    if not nums:
        return 0

    slow = 0  # Points to last written unique element

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            # Found a new unique element — advance slow and write it
            slow += 1
            nums[slow] = nums[fast]

    # Return count of unique elements (slow is 0-indexed)
    return slow + 1


def remove_duplicates_with_set(nums: list) -> list:
    """
    Alternative: use a set for unsorted arrays.
    Returns a new list (does not modify in place).
    O(n) time, O(n) space.
    """
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


if __name__ == "__main__":
    test_cases = [
        [1, 1, 2, 3, 3, 4],
        [1, 1, 1],
        [1, 2, 3],
        [],
        [1],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    ]

    print("=" * 50)
    print("Remove Duplicates from Sorted Array")
    print("=" * 50)

    for nums in test_cases:
        original = nums.copy()
        count = remove_duplicates(nums)
        unique_part = nums[:count]
        print(f"Input:  {original}")
        print(f"Result: {unique_part} (count={count})")
        print("-" * 30)
