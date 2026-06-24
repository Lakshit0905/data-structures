"""
Problem: Longest Substring Without Repeating Characters
=========================================================
Given a string, find the length of the longest substring without
repeating characters.

Interview Explanation:
    Variable-size sliding window with a HashSet.
    Use two pointers (left, right) to define the window.
    Expand right — if character already in window, shrink from left until
    the duplicate is removed. Track the max window size seen.
    O(n) time, O(min(n,m)) space where m = charset size.

Example:
    Input:  "abcabcbb"
    Output: 3  (substring "abc")

    Input:  "pwwkew"
    Output: 3  (substring "wke")

Time Complexity:  O(n)
Space Complexity: O(min(n, m)) where m is charset size
"""


def length_of_longest_substring(s: str) -> int:
    """
    Sliding window with HashSet.
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink window from left until no duplicate at s[right]
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current character to window
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


def longest_substring_with_value(s: str) -> tuple:
    """
    Extended: returns both the length AND the actual substring.
    """
    char_set = set()
    left = 0
    max_length = 0
    best_start = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            best_start = left

    return (max_length, s[best_start:best_start + max_length])


if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
        ("dvdf", 3),
    ]

    print("=" * 50)
    print("Longest Substring Without Repeating Characters")
    print("=" * 50)

    for s, expected in test_cases:
        length, substr = longest_substring_with_value(s)
        status = "✓" if length == expected else "✗"
        print(f"{status} '{s}' → length={length}, substring='{substr}' (expected={expected})")
