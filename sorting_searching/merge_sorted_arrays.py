"""
Problem: Merge Two Sorted Arrays
==================================
Given two sorted arrays, merge them into one sorted array.

Interview Explanation:
    Use two pointers — one for each array. Compare elements at both pointers,
    pick the smaller one, and advance that pointer. Continue until one array
    is exhausted, then append the remaining elements.
    O(n + m) time, O(n + m) space.

Example:
    Input:  arr1 = [1, 3, 5], arr2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]

Time Complexity:  O(n + m)
Space Complexity: O(n + m)
"""


def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    """
    Two-pointer merge approach.
    """
    result = []
    i, j = 0, 0

    # Compare and merge while both arrays have elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Append remaining elements from either array
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2, 3], [4, 5, 6]),
        ([], [1, 2, 3]),
        ([1], []),
        ([1, 3], [2]),
    ]

    print("=" * 50)
    print("Merge Two Sorted Arrays")
    print("=" * 50)

    for arr1, arr2 in test_cases:
        result = merge_sorted_arrays(arr1, arr2)
        print(f"arr1={arr1}, arr2={arr2}")
        print(f"Merged: {result}")
        print("-" * 30)
