"""
Problem: Reverse a String Using Recursion
==========================================
Reverse a string using a recursive approach.

Interview Explanation:
    Base case: empty string or single character → return as-is.
    Recursive case: reverse(s) = reverse(s[1:]) + s[0]
    We peel off the first character and append it to the end of
    the reversed rest. O(n) time, O(n) call stack space.

Example:
    Input:  "hello"
    Output: "olleh"

Time Complexity:  O(n)
Space Complexity: O(n) - call stack
"""


def reverse_string_recursive(s: str) -> str:
    """
    Recursive string reversal.
    """
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    # Recursive case: reverse the rest, append the first character at end
    return reverse_string_recursive(s[1:]) + s[0]


if __name__ == "__main__":
    test_cases = ["hello", "python", "a", "", "racecar", "SDET"]

    print("=" * 50)
    print("Reverse String (Recursion)")
    print("=" * 50)

    for s in test_cases:
        result = reverse_string_recursive(s)
        verify = result == s[::-1]
        print(f"'{s}' → '{result}' {'✓' if verify else '✗'}")
