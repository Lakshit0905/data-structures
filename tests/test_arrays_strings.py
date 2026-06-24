"""
Pytest Tests: Arrays & Strings
================================
Unit tests for all arrays_strings/ modules.
Run with: pytest tests/test_arrays_strings.py -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from arrays_strings.reverse_array import reverse_array_inplace, reverse_array_slicing
from arrays_strings.two_sum import two_sum, two_sum_brute_force
from arrays_strings.valid_anagram import is_anagram, is_anagram_counter
from arrays_strings.first_unique_character import first_unique_char
from arrays_strings.remove_duplicates import remove_duplicates


# ── reverse_array ──────────────────────────────────────────────

class TestReverseArray:
    def test_odd_length(self):
        assert reverse_array_inplace([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    def test_even_length(self):
        assert reverse_array_inplace([1, 2, 3, 4]) == [4, 3, 2, 1]

    def test_single_element(self):
        assert reverse_array_inplace([42]) == [42]

    def test_empty(self):
        assert reverse_array_inplace([]) == []

    def test_strings(self):
        assert reverse_array_inplace(["a", "b", "c"]) == ["c", "b", "a"]

    def test_slicing_returns_new_list(self):
        original = [1, 2, 3]
        result = reverse_array_slicing(original)
        assert result == [3, 2, 1]
        assert original == [1, 2, 3]  # Original unchanged


# ── two_sum ────────────────────────────────────────────────────

class TestTwoSum:
    def test_basic(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_non_adjacent(self):
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_same_element(self):
        assert two_sum([3, 3], 6) == [0, 1]

    def test_negative_numbers(self):
        result = two_sum([-3, 4, 3, 90], 0)
        assert result == [0, 2]

    def test_brute_force_matches(self):
        nums, target = [2, 7, 11, 15], 9
        assert two_sum(nums, target) == two_sum_brute_force(nums, target)

    def test_empty_returns_empty(self):
        assert two_sum([], 5) == []


# ── valid_anagram ──────────────────────────────────────────────

class TestValidAnagram:
    def test_anagram(self):
        assert is_anagram("anagram", "nagaram") is True

    def test_not_anagram(self):
        assert is_anagram("rat", "car") is False

    def test_classic_anagram(self):
        assert is_anagram("listen", "silent") is True

    def test_different_lengths(self):
        assert is_anagram("ab", "a") is False

    def test_empty_strings(self):
        assert is_anagram("", "") is True

    def test_single_chars_match(self):
        assert is_anagram("a", "a") is True

    def test_single_chars_no_match(self):
        assert is_anagram("a", "b") is False

    def test_counter_version(self):
        assert is_anagram_counter("listen", "silent") is True
        assert is_anagram_counter("hello", "world") is False


# ── first_unique_character ────────────────────────────────────

class TestFirstUniqueChar:
    def test_first_char(self):
        assert first_unique_char("leetcode") == 0

    def test_middle_char(self):
        assert first_unique_char("loveleetcode") == 2

    def test_no_unique(self):
        assert first_unique_char("aabb") == -1

    def test_single_char(self):
        assert first_unique_char("z") == 0

    def test_empty_string(self):
        assert first_unique_char("") == -1

    def test_last_char_unique(self):
        assert first_unique_char("aabbc") == 4


# ── remove_duplicates ─────────────────────────────────────────

class TestRemoveDuplicates:
    def test_basic(self):
        nums = [1, 1, 2, 3, 3, 4]
        count = remove_duplicates(nums)
        assert count == 4
        assert nums[:count] == [1, 2, 3, 4]

    def test_all_same(self):
        nums = [1, 1, 1]
        count = remove_duplicates(nums)
        assert count == 1
        assert nums[:count] == [1]

    def test_no_duplicates(self):
        nums = [1, 2, 3]
        count = remove_duplicates(nums)
        assert count == 3

    def test_empty(self):
        assert remove_duplicates([]) == 0

    def test_single(self):
        nums = [1]
        assert remove_duplicates(nums) == 1

    def test_longer_array(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        count = remove_duplicates(nums)
        assert count == 5
        assert nums[:count] == [0, 1, 2, 3, 4]
