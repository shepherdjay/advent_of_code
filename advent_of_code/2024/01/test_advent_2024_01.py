import pytest
from advent_2024_01 import (
    find_total_distance,
    get_lists,
    calculate_similarity,
    single_similarity,
)
import os


@pytest.mark.parametrize(
    "list_a,list_b,expected",
    [
        ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 11),
        ([1], [1], 0),
    ],
)
def test_find_total_distance(list_a, list_b, expected):
    result = find_total_distance(list_a, list_b)

    assert result == expected


def test_get_lists():
    list_a, list_b = get_lists(
        os.path.join(os.path.dirname(__file__), "advent_2024_01_example.txt")
    )

    assert list_a == [3, 4, 2, 1, 3, 3]
    assert list_b == [4, 3, 5, 3, 9, 3]


@pytest.mark.parametrize(
    "list_a,list_b,expected",
    [
        ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 31),
        ([1], [1], 1),
    ],
)
def test_calculate_similarity(list_a, list_b, expected):
    assert calculate_similarity(list_a, list_b) == expected


def test_single_similarity():
    assert single_similarity(3, [4, 3, 5, 3, 9, 3]) == 9
