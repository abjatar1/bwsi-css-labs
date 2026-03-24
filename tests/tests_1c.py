"""
tests_1c.py

Unit tests for lab_1c.py
"""

import pytest

from labs.lab_1.lab_1c import max_subarray_sum


def test_max_subarray_sum_standard_case():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_sum_all_negative():
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2


def test_max_subarray_sum_single_element():
    assert max_subarray_sum([7]) == 7


def test_max_subarray_sum_empty_list():
    with pytest.raises(ValueError, match="Integer subarray cannot be empty."):
        max_subarray_sum([])
