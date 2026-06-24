"""
Pytest Tests: Two Pointers
============================
Unit tests for all two_pointers/ modules.
Run with: pytest tests/test_two_pointers.py -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from two_pointers.palindrome_check import is_palindrome
from two_pointers.reverse_string import reverse_string
from two_pointers.pair_sum_sorted_array import pair_sum_sorted
from two_pointers.move_zeroes import move_zeroes


class TestPalindromeCheck:
    def test_classic_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_with_spaces_and_punctuation(self):
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("race a car") is False

    def test_empty_string(self):
        assert is_palindrome("") is True

    def test_single_char(self):
        assert is_palindrome("a") is True

    def test_case_insensitive(self):
        assert is_palindrome("Was it a car or a cat I saw?") is True


class TestReverseString:
    def test_hello(self):
        assert reverse_string(['h', 'e', 'l', 'l', 'o']) == ['o', 'l', 'l', 'e', 'h']

    def test_palindrome(self):
        s = ['h', 'a', 'n', 'n', 'a', 'h']
        assert reverse_string(s) == ['h', 'a', 'n', 'n', 'a', 'h']

    def test_single(self):
        assert reverse_string(['a']) == ['a']

    def test_empty(self):
        assert reverse_string([]) == []


class TestPairSumSortedArray:
    def test_basic(self):
        assert pair_sum_sorted([2, 7, 11, 15], 9) == [1, 2]

    def test_non_adjacent(self):
        assert pair_sum_sorted([2, 3, 4], 6) == [1, 3]

    def test_negative_numbers(self):
        assert pair_sum_sorted([-1, 0], -1) == [1, 2]

    def test_no_pair(self):
        assert pair_sum_sorted([1, 2, 3], 10) == []


class TestMoveZeroes:
    def test_basic(self):
        nums = [0, 1, 0, 3, 12]
        assert move_zeroes(nums) == [1, 3, 12, 0, 0]

    def test_all_zeros(self):
        assert move_zeroes([0, 0, 0]) == [0, 0, 0]

    def test_no_zeros(self):
        assert move_zeroes([1, 2, 3]) == [1, 2, 3]

    def test_single_zero(self):
        assert move_zeroes([0]) == [0]

    def test_zero_at_end(self):
        assert move_zeroes([1, 2, 0]) == [1, 2, 0]

    def test_preserves_order(self):
        result = move_zeroes([4, 2, 0, 1, 0, 7])
        non_zero = [x for x in result if x != 0]
        assert non_zero == [4, 2, 1, 7]
