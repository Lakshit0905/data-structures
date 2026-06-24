"""
Problem: Find the Missing Number
==================================
Given an array containing n distinct numbers taken from 0 to n,
find the one number missing from the array.

Interview Explanation:
    The sum of 0..n = n*(n+1)/2. Subtract the actual sum from expected sum.
    The difference is the missing number. O(n) time, O(1) space.
    Alternatively use XOR — but sum approach is easier to explain clearly.

Example:
    Input:  [3, 0, 1]
    Output: 2  (n=3, expected sum=6, actual sum=4, missing=2)

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def find_missing_number(nums: list) -> int:
    """
    Sum formula approach: expected_sum - actual_sum = missing number.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def find_missing_number_xor(nums: list) -> int:
    """
    XOR approach: XOR all indices and all values.
    Pairs cancel out, leaving the missing number.
    """
    n = len(nums)
    xor = 0
    for i in range(n + 1):
        xor ^= i
    for num in nums:
        xor ^= num
    return xor


if __name__ == "__main__":
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
    ]

    print("=" * 50)
    print("Find Missing Number")
    print("=" * 50)

    for nums, expected in test_cases:
        result = find_missing_number(nums)
        result_xor = find_missing_number_xor(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} → Sum method: {result}, XOR method: {result_xor} (expected: {expected})")
