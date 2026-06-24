"""
Problem: Palindrome Check
==========================
Given a string, return True if it reads the same forwards and backwards.
Consider only alphanumeric characters and ignore case.

Interview Explanation:
    Two-pointer approach: place one pointer at start, one at end.
    Move both inward, comparing characters. If any mismatch, return False.
    Skip non-alphanumeric characters.
    O(n) time, O(1) space — better than reversing the string (O(n) space).

Example:
    Input:  "A man, a plan, a canal: Panama"
    Output: True

    Input:  "race a car"
    Output: False

Time Complexity:  O(n)
Space Complexity: O(1)
"""


def is_palindrome(s: str) -> bool:
    """
    Two-pointer approach with alphanumeric filtering.
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_simple(s: str) -> bool:
    """
    Simplified version for clean strings (no spaces/symbols).
    """
    s = s.lower()
    return s == s[::-1]


if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("racecar", True),
        ("hello", False),
        ("Was it a car or a cat I saw?", True),
    ]

    print("=" * 50)
    print("Palindrome Check")
    print("=" * 50)

    for s, expected in test_cases:
        result = is_palindrome(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s}' → {result}")
