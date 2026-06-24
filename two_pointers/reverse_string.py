"""
Problem: Reverse String
========================
Reverse a string in place (given as a character array).

Interview Explanation:
    Classic two-pointer swap: left starts at 0, right at end.
    Swap characters and move pointers inward. O(n) time, O(1) space.

Example:
    Input:  ['h','e','l','l','o']
    Output: ['o','l','l','e','h']

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def reverse_string(s: list) -> list:
    """
    In-place two-pointer swap.
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


if __name__ == "__main__":
    test_cases = [
        ['h', 'e', 'l', 'l', 'o'],
        ['H', 'a', 'n', 'n', 'a', 'h'],
        ['a'],
        [],
    ]

    print("=" * 50)
    print("Reverse String (Two Pointers)")
    print("=" * 50)

    for s in test_cases:
        original = s.copy()
        result = reverse_string(s)
        print(f"Input:  {original}")
        print(f"Output: {result}")
        print("-" * 30)
