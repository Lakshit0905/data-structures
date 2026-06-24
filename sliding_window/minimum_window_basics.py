"""
Problem: Minimum Window Substring (Basics)
===========================================
Given strings s and t, return the minimum window substring of s
that contains all characters of t. Return "" if no such window exists.

Interview Explanation:
    Use a sliding window with two frequency maps: one for t's requirements,
    one for the current window. Track how many characters are "satisfied"
    (have enough frequency). Expand right to find a valid window, then
    contract left to minimize it.
    O(n + m) time, O(n + m) space.

Example:
    Input:  s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Time Complexity:  O(n + m) where n=len(s), m=len(t)
Space Complexity: O(n + m)
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    Sliding window with two frequency counters.
    """
    if not t or not s:
        return ""

    # What we need
    need = Counter(t)
    required = len(need)  # Number of unique chars we need

    left = 0
    formed = 0  # How many unique chars currently satisfied
    window_counts = {}

    # Result: (window length, left, right)
    result = float("inf"), None, None

    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if this char's requirement is now satisfied
        if char in need and window_counts[char] == need[char]:
            formed += 1

        # Try to contract the window while it's valid
        while left <= right and formed == required:
            # Update result if this window is smaller
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)

            # Remove leftmost character from window
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in need and window_counts[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return "" if result[0] == float("inf") else s[result[1]: result[2] + 1]


if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
    ]

    print("=" * 50)
    print("Minimum Window Substring (Basics)")
    print("=" * 50)

    for s, t, expected in test_cases:
        result = min_window(s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}', t='{t}' → '{result}' (expected: '{expected}')")
