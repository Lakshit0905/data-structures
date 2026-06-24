"""
Problem: Pair Sum in Sorted Array
===================================
Given a sorted array and a target sum, find if there exist two numbers
that add up to the target. Return their indices (1-indexed) or the values.

Interview Explanation:
    Because the array is sorted, use two pointers (left=0, right=end).
    If sum < target → move left right (need bigger number).
    If sum > target → move right left (need smaller number).
    If sum == target → found it!
    O(n) time, O(1) space. Better than HashMap for sorted arrays.

Example:
    Input:  numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]  (1-indexed: numbers[0] + numbers[1] = 9)

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def pair_sum_sorted(numbers: list, target: int) -> list:
    """
    Two-pointer approach for sorted array.
    Returns 1-indexed positions.
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1   # Need a larger sum → move left pointer right
        else:
            right -= 1  # Need a smaller sum → move right pointer left

    return []  # No pair found


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 5], 9, [4, 5]),
    ]

    print("=" * 50)
    print("Pair Sum in Sorted Array (Two Pointers)")
    print("=" * 50)

    for numbers, target, expected in test_cases:
        result = pair_sum_sorted(numbers, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} numbers={numbers}, target={target} → {result}")
