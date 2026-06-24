"""
Problem: Maximum Sum Subarray of Size K
=========================================
Given an array of integers and a number k, find the maximum sum of
any contiguous subarray of size k.

Interview Explanation:
    Brute force recalculates the sum for every window — O(n*k).
    Sliding window maintains a running sum: subtract the element going
    out of the window, add the new element coming in. O(n) time, O(1) space.
    This "slide" technique is the core pattern for all sliding window problems.

Example:
    Input:  arr = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9  (subarray [5, 1, 3])

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def max_sum_subarray(arr: list, k: int) -> int:
    """
    Sliding window approach.
    Build the first window, then slide it across.
    """
    if not arr or k > len(arr):
        return 0

    # Build the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window: remove leftmost, add rightmost
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def max_sum_subarray_with_indices(arr: list, k: int) -> tuple:
    """
    Extended version: returns max sum AND the start/end indices.
    Useful for reporting which subarray produced the max.
    """
    if not arr or k > len(arr):
        return (0, -1, -1)

    window_sum = sum(arr[:k])
    max_sum = window_sum
    max_start = 0

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
            max_start = i - k + 1

    return (max_sum, max_start, max_start + k - 1)


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 1, 3, 2], 3),
        ([2, 3, 4, 1, 5], 2),
        ([1, 4, 2, 10, 23, 3, 1, 0, 20], 4),
        ([-1, -2, -3, -4], 2),
    ]

    print("=" * 50)
    print("Max Sum Subarray of Size K (Sliding Window)")
    print("=" * 50)

    for arr, k in test_cases:
        max_s, start, end = max_sum_subarray_with_indices(arr, k)
        print(f"Array: {arr}, k={k}")
        print(f"Max sum: {max_s}, subarray: {arr[start:end+1]} (indices {start}–{end})")
        print("-" * 30)
