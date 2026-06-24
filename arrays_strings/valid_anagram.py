"""
Problem: Valid Anagram
======================
Given two strings s and t, return True if t is an anagram of s, else False.
An anagram uses all original letters exactly once, just rearranged.

Interview Explanation:
    Sort both strings and compare — simple but O(n log n).
    Better: use a frequency counter (HashMap). Count characters in s,
    then decrement for characters in t. If any count hits non-zero, not anagram.
    This is O(n) time and O(1) space (at most 26 lowercase letters).

Example:
    Input:  s = "anagram", t = "nagaram"
    Output: True

    Input:  s = "rat", t = "car"
    Output: False

Time Complexity:  O(n) where n = length of the strings
Space Complexity: O(1) - at most 26 character keys in the HashMap
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    Optimal HashMap frequency counter approach.
    """
    if len(s) != len(t):
        return False

    # Count frequency of each character in s
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Subtract frequency using characters in t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


def is_anagram_counter(s: str, t: str) -> bool:
    """
    Pythonic version using collections.Counter.
    Great to mention in interviews — shows Python knowledge.
    """
    return Counter(s) == Counter(t)


def is_anagram_sort(s: str, t: str) -> bool:
    """
    Sorting approach — simple but O(n log n).
    Good to mention as a starting point before optimizing.
    """
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("hello", "world", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "a", False),
    ]

    print("=" * 50)
    print("Valid Anagram")
    print("=" * 50)

    for s, t, expected in test_cases:
        result = is_anagram(s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}', t='{t}' → {result} (expected: {expected})")
