"""
Pytest Tests: HashMap / Dictionary
=====================================
Unit tests for all hashmap/ modules.
Run with: pytest tests/test_hashmap.py -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from hashmap.frequency_counter import frequency_counter, most_frequent, elements_appearing_more_than_n_times
from hashmap.first_duplicate import first_duplicate, all_duplicates, find_duplicate_indices
from hashmap.group_anagrams import group_anagrams
from hashmap.contains_duplicate import contains_duplicate, contains_duplicate_pythonic


# ── frequency_counter ─────────────────────────────────────────

class TestFrequencyCounter:
    def test_basic(self):
        result = frequency_counter(["a", "b", "a", "c", "b", "a"])
        assert result == {"a": 3, "b": 2, "c": 1}

    def test_empty(self):
        assert frequency_counter([]) == {}

    def test_all_same(self):
        assert frequency_counter([1, 1, 1]) == {1: 3}

    def test_integers(self):
        result = frequency_counter([1, 2, 3, 2, 1])
        assert result[1] == 2
        assert result[2] == 2
        assert result[3] == 1

    def test_most_frequent(self):
        items = ["a", "b", "a", "a", "c"]
        element, count = most_frequent(items)
        assert element == "a"
        assert count == 3

    def test_most_frequent_empty(self):
        assert most_frequent([]) == (None, 0)

    def test_elements_more_than_n(self):
        result = elements_appearing_more_than_n_times([1, 2, 1, 3, 2, 1], 1)
        assert set(result) == {1, 2}


# ── first_duplicate ───────────────────────────────────────────

class TestFirstDuplicate:
    def test_basic(self):
        assert first_duplicate([2, 1, 3, 5, 3, 2]) == 3

    def test_no_duplicate(self):
        assert first_duplicate([1, 2, 3, 4]) is None

    def test_all_duplicates(self):
        assert first_duplicate([1, 1]) == 1

    def test_empty(self):
        assert first_duplicate([]) is None

    def test_all_duplicates_list(self):
        result = all_duplicates([2, 1, 3, 5, 3, 2])
        assert set(result) == {2, 3}

    def test_duplicate_indices(self):
        result = find_duplicate_indices(["TC001", "TC002", "TC001"])
        assert "TC001" in result
        assert result["TC001"] == [0, 2]


# ── group_anagrams ────────────────────────────────────────────

class TestGroupAnagrams:
    def test_basic(self):
        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        # Sort each group and sort the groups for comparison
        result_sorted = sorted([sorted(g) for g in result])
        assert result_sorted == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

    def test_single_word(self):
        result = group_anagrams(["a"])
        assert result == [["a"]]

    def test_empty_strings(self):
        result = group_anagrams(["", ""])
        assert len(result) == 1
        assert len(result[0]) == 2

    def test_no_anagrams(self):
        result = group_anagrams(["abc", "def", "ghi"])
        assert len(result) == 3


# ── contains_duplicate ────────────────────────────────────────

class TestContainsDuplicate:
    def test_has_duplicate(self):
        assert contains_duplicate([1, 2, 3, 1]) is True

    def test_no_duplicate(self):
        assert contains_duplicate([1, 2, 3, 4]) is False

    def test_empty(self):
        assert contains_duplicate([]) is False

    def test_single_element(self):
        assert contains_duplicate([1]) is False

    def test_all_same(self):
        assert contains_duplicate([1, 1, 1]) is True

    def test_pythonic_version(self):
        assert contains_duplicate_pythonic([1, 2, 3, 1]) is True
        assert contains_duplicate_pythonic([1, 2, 3, 4]) is False
