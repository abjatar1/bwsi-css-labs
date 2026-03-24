"""
tests_1d.py

Unit tests for lab_1d.py
"""

from labs.lab_1.lab_1d import two_sum


def test_two_sum_finds_matching_pair():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_handles_duplicate_values():
    assert two_sum([3, 3], 6) == [0, 1]
