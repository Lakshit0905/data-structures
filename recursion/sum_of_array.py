"""
Problem: Sum of Array Using Recursion
======================================
Given a list of numbers, return their sum using recursion.

Interview Explanation:
    Base case: empty list → 0.
    Recursive case: first element + sum of the rest.
    O(n) time, O(n) space (call stack). Shows you understand
    how recursion maps to iteration.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: 15

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def sum_of_array(arr: list) -> int:
    """
    Recursive sum.
    """
    if not arr:  # Base case: empty list
        return 0
    return arr[0] + sum_of_array(arr[1:])  # First + sum of rest


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([], 0),
        ([10], 10),
        ([-1, -2, 3], 0),
    ]

    print("=" * 50)
    print("Sum of Array (Recursion)")
    print("=" * 50)

    for arr, expected in test_cases:
        result = sum_of_array(arr)
        status = "✓" if result == expected else "✗"
        print(f"{status} sum({arr}) = {result} (expected: {expected})")
