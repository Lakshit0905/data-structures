"""
Pytest Tests: Sliding Window
==============================
Unit tests for all sliding_window/ modules.
Run with: pytest tests/test_sliding_window.py -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from sliding_window.max_sum_subarray import max_sum_subarray, max_sum_subarray_with_indices
from sliding_window.longest_substring_without_repeat import length_of_longest_substring
from sliding_window.minimum_window_basics import min_window


class TestMaxSumSubarray:
    def test_basic(self):
        assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9

    def test_k_equals_length(self):
        assert max_sum_subarray([1, 2, 3], 3) == 6

    def test_negative_numbers(self):
        assert max_sum_subarray([-1, -2, -3, -4], 2) == -3

    def test_single_element(self):
        assert max_sum_subarray([5], 1) == 5

    def test_empty(self):
        assert max_sum_subarray([], 3) == 0

    def test_k_larger_than_array(self):
        assert max_sum_subarray([1, 2], 5) == 0

    def test_with_indices(self):
        max_s, start, end = max_sum_subarray_with_indices([2, 1, 5, 1, 3, 2], 3)
        assert max_s == 9
        assert end - start == 2  # Window size is 3

    def test_large_array(self):
        arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
        assert max_sum_subarray(arr, 4) == 39  # [4, 2, 10, 23]


class TestLongestSubstringWithoutRepeat:
    def test_basic(self):
        assert length_of_longest_substring("abcabcbb") == 3

    def test_all_same(self):
        assert length_of_longest_substring("bbbbb") == 1

    def test_mixed(self):
        assert length_of_longest_substring("pwwkew") == 3

    def test_empty(self):
        assert length_of_longest_substring("") == 0

    def test_no_repeats(self):
        assert length_of_longest_substring("abcdef") == 6

    def test_single_char(self):
        assert length_of_longest_substring("a") == 1

    def test_two_chars(self):
        assert length_of_longest_substring("au") == 2

    def test_dvdf(self):
        assert length_of_longest_substring("dvdf") == 3


class TestMinimumWindowSubstring:
    def test_basic(self):
        assert min_window("ADOBECODEBANC", "ABC") == "BANC"

    def test_exact_match(self):
        assert min_window("a", "a") == "a"

    def test_impossible(self):
        assert min_window("a", "aa") == ""

    def test_empty_s(self):
        assert min_window("", "a") == ""

    def test_empty_t(self):
        assert min_window("abc", "") == ""

    def test_same_length(self):
        assert min_window("aa", "aa") == "aa"
