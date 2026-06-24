"""
Problem: Next Greater Element
==============================
Given an array, for each element find the next greater element to its right.
If no greater element exists, output -1 for that position.

Interview Explanation:
    Brute force: for each element, scan right → O(n^2).
    Optimal: use a monotonic stack. Traverse right-to-left.
    Maintain a stack of candidates. For each element, pop all stack
    elements that are ≤ current (they can't be "next greater" for anything
    to the left). The top of stack is the next greater element.
    O(n) time, O(n) space.

Example:
    Input:  [4, 5, 2, 10, 8]
    Output: [5, 10, 10, -1, -1]

Time Complexity:  O(n)
Space Complexity: O(n)
"""


def next_greater_element(nums: list) -> list:
    """
    Monotonic stack approach — traverse left to right.
    Stack holds indices of elements waiting for their next greater.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Stack of indices

    for i in range(n):
        # Pop elements from stack that are smaller than current element
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]  # Current element is the next greater

        stack.append(i)

    # Remaining elements in stack have no next greater → stay -1
    return result


if __name__ == "__main__":
    test_cases = [
        ([4, 5, 2, 10, 8], [5, 10, 10, -1, -1]),
        ([1, 3, 2, 4], [3, 4, 4, -1]),
        ([5, 4, 3, 2, 1], [-1, -1, -1, -1, -1]),
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),
    ]

    print("=" * 50)
    print("Next Greater Element (Monotonic Stack)")
    print("=" * 50)

    for nums, expected in test_cases:
        result = next_greater_element(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums}")
        print(f"   Result:   {result}")
        print(f"   Expected: {expected}")
        print("-" * 30)
