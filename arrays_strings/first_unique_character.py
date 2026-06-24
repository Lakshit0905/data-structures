"""
Problem: First Unique Character in a String
============================================
Given a string s, find the first non-repeating character and return its index.
If it doesn't exist, return -1.

Interview Explanation:
    Use a frequency HashMap (two-pass approach):
    Pass 1 — count all character frequencies.
    Pass 2 — find the first character with frequency == 1.
    This is O(n) time and O(1) space (bounded by 26 lowercase letters).

Example:
    Input:  s = "leetcode"
    Output: 0  (l appears only once, at index 0)

    Input:  s = "aabb"
    Output: -1  (no unique character)

Time Complexity:  O(n) - two passes through the string
Space Complexity: O(1) - at most 26 keys in the HashMap
"""

from collections import Counter


def first_unique_char(s: str) -> int:
    """
    Two-pass HashMap approach.
    Pass 1: build frequency map.
    Pass 2: find first char with count == 1.
    """
    # Pass 1: count character frequencies
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Pass 2: find first unique character
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i

    return -1  # No unique character found


def first_unique_char_counter(s: str) -> int:
    """
    Pythonic version using Counter.
    """
    freq = Counter(s)
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    return -1


if __name__ == "__main__":
    test_cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("z", 0),
        ("aabbc", 4),
        ("", -1),
    ]

    print("=" * 50)
    print("First Unique Character in a String")
    print("=" * 50)

    for s, expected in test_cases:
        result = first_unique_char(s)
        status = "✓" if result == expected else "✗"
        char_display = f"(char='{s[result]}')" if result != -1 and s else ""
        print(f"{status} s='{s}' → index {result} {char_display} (expected: {expected})")
