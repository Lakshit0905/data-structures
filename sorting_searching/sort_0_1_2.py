"""
Problem: Sort Array of 0s, 1s, and 2s (Dutch National Flag)
=============================================================
Given an array containing only 0s, 1s, and 2s, sort it in-place
in one pass without using any sorting function.

Interview Explanation:
    Dutch National Flag algorithm by Dijkstra. Three pointers:
    - low: boundary of 0s (everything before low is 0)
    - mid: current element being examined
    - high: boundary of 2s (everything after high is 2)
    Move mid across; swap with low or high depending on value.
    O(n) time, O(1) space — single pass.

Example:
    Input:  [2, 0, 2, 1, 1, 0]
    Output: [0, 0, 1, 1, 2, 2]

Time Complexity:  O(n) — single pass
Space Complexity: O(1) — in-place
"""


def sort_colors(nums: list) -> list:
    """
    Dutch National Flag algorithm.
    low = next position for 0, high = next position for 2.
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1  # 1 is already in the right zone
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Don't increment mid — the swapped element needs to be examined

    return nums


if __name__ == "__main__":
    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1, 2, 0],
        [0, 0, 0],
        [2, 2, 2],
    ]

    print("=" * 50)
    print("Sort 0s, 1s, 2s (Dutch National Flag)")
    print("=" * 50)

    for nums in test_cases:
        original = nums.copy()
        result = sort_colors(nums)
        print(f"Input:  {original}")
        print(f"Output: {result}")
        print("-" * 30)
