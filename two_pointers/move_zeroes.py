"""
Problem: Move Zeroes
======================
Given an integer array, move all zeroes to the end while maintaining
the relative order of the non-zero elements. Do it in-place.

Interview Explanation:
    Use a slow pointer (write position) and fast pointer (reader).
    When fast finds a non-zero, write it to the slow position and advance slow.
    After the loop, fill remaining positions with 0s.
    O(n) time, O(1) space.

Example:
    Input:  [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def move_zeroes(nums: list) -> list:
    """
    Two-pointer in-place approach.
    slow = next write position for non-zero values.
    """
    slow = 0  # Write position

    # Phase 1: copy all non-zero elements to the front
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1

    # Phase 2: fill the rest with zeroes
    while slow < len(nums):
        nums[slow] = 0
        slow += 1

    return nums


if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3],
        [0, 0, 0, 1],
        [4, 2, 0, 1, 0, 7],
    ]

    print("=" * 50)
    print("Move Zeroes to End")
    print("=" * 50)

    for nums in test_cases:
        original = nums.copy()
        result = move_zeroes(nums)
        print(f"Input:  {original}")
        print(f"Output: {result}")
        print("-" * 30)
