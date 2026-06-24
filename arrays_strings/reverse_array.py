"""
Problem: Reverse an Array
========================
Given a list of elements, return the list in reverse order.

Interview Explanation:
    This is a foundational problem testing your knowledge of list manipulation.
    Two common approaches: using Python slicing (O(n) space) or in-place
    two-pointer swap (O(1) space). Interviewers often ask for the in-place version.

Example:
    Input:  [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Time Complexity:  O(n) - we visit each element once
Space Complexity: O(1) - in-place reversal uses no extra space
"""


def reverse_array_inplace(arr: list) -> list:
    """
    Reverses an array in place using two pointers.
    Modifies the original list.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        # Swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def reverse_array_slicing(arr: list) -> list:
    """
    Reverses an array using Python slicing.
    Returns a new list (does NOT modify the original).
    """
    return arr[::-1]


def reverse_array_builtin(arr: list) -> list:
    """
    Reverses using Python's built-in reversed().
    Clean and Pythonic.
    """
    return list(reversed(arr))


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        ["a", "b", "c"],
        [42],
        [],
        [1, 2],
    ]

    print("=" * 50)
    print("Reverse Array - All Approaches")
    print("=" * 50)

    for arr in test_cases:
        original = arr.copy()
        result_inplace = reverse_array_inplace(arr.copy())
        result_slice = reverse_array_slicing(original)
        print(f"Input:    {original}")
        print(f"In-place: {result_inplace}")
        print(f"Slicing:  {result_slice}")
        print("-" * 30)
