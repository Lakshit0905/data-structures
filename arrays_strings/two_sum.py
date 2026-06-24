"""
Problem: Two Sum
================
Given a list of integers and a target integer, return the indices of the
two numbers that add up to the target. Assume exactly one solution exists.

Interview Explanation:
    The brute force O(n^2) approach uses nested loops. The optimal approach
    uses a HashMap to store "what number do I need?" as we iterate. For each
    number, we check if its complement (target - num) is already in the map.
    This reduces time to O(n) with O(n) space.

Example:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]  (because nums[0] + nums[1] = 2 + 7 = 9)

Time Complexity:  O(n) - single pass through the array
Space Complexity: O(n) - HashMap stores up to n elements
"""


def two_sum(nums: list, target: int) -> list:
    """
    Optimal HashMap solution.
    Key insight: for each number, we need (target - number).
    Store each number's index in a dict as we go.
    """
    seen = {}  # {value: index}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            # Found the pair! Return both indices
            return [seen[complement], i]

        # Store current number and its index for future lookups
        seen[num] = i

    return []  # No solution found


def two_sum_brute_force(nums: list, target: int) -> list:
    """
    Brute force O(n^2) - shown for comparison.
    Check every pair of numbers.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),    # Expected: [0, 1]
        ([3, 2, 4], 6),          # Expected: [1, 2]
        ([3, 3], 6),             # Expected: [0, 1]
        ([1, 5, 3, 7, 2], 10),  # Expected: [1, 3]
    ]

    print("=" * 50)
    print("Two Sum - HashMap Approach")
    print("=" * 50)

    for nums, target in test_cases:
        result = two_sum(nums, target)
        print(f"nums={nums}, target={target}")
        print(f"Result: indices={result}", end="")
        if result:
            print(f" → values: {nums[result[0]]} + {nums[result[1]]} = {target}")
        else:
            print(" (no solution)")
        print("-" * 30)
