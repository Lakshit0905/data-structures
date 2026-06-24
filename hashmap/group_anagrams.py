"""
Problem: Group Anagrams
========================
Given a list of strings, group the anagrams together.

Interview Explanation:
    Key insight: anagrams all have the same sorted string as a "signature".
    Use the sorted string as a HashMap key. Group all original strings
    under their signature. O(n * k log k) where k = max string length.

Example:
    Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Time Complexity:  O(n * k log k) — sorting each of n strings of length k
Space Complexity: O(n * k) — storing all strings in the HashMap
"""

from collections import defaultdict


def group_anagrams(strs: list) -> list:
    """
    Sort-based grouping using HashMap.
    """
    anagram_map = defaultdict(list)

    for s in strs:
        # Sorted string is the canonical key for all anagrams
        key = "".join(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())


def group_anagrams_char_count(strs: list) -> list:
    """
    Alternative: use character count tuple as key (no sorting).
    O(n * k) time — slightly faster for large strings.
    """
    anagram_map = defaultdict(list)

    for s in strs:
        # Create a 26-element tuple representing character counts
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        anagram_map[key].append(s)

    return list(anagram_map.values())


if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["listen", "silent", "hello", "world", "enlist"],
        ["a"],
        ["", ""],
    ]

    print("=" * 50)
    print("Group Anagrams")
    print("=" * 50)

    for strs in test_cases:
        result = group_anagrams(strs)
        print(f"Input:  {strs}")
        print(f"Groups: {result}")
        print("-" * 30)
