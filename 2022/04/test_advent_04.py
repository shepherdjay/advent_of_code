import pytest
from advent_04 import (
    range_section,
    check_fully_contained,
    find_overlaps,
    check_overlaps,
)


def test_range_section():
    assert range(2, 5) == range_section("2-4")
    assert range(15, 26) == range_section("15-25")
    assert [1, 2, 3, 4, 5] == list(range_section("1-5"))


@pytest.mark.parametrize(
    "input, result",
    [
        (["16-72", "16-34"], True),
        (["5-7", "7-9"], False),
        (["2-4", "6-8"], False),
        (["2-8", "3-7"], True),
        (["3-7", "2-8"], True),
        (["2-5", "1-4"], False),
        (["1-4", "2-5"], False),
        (["62-85", "62-85"], True),
        (["1-2", "3-3"], False),
    ],
)
def test_fully_contained(input, result):
    assert result == check_fully_contained(input)


def test_find_overlaps():
    assert (2, 4) == find_overlaps(
        [
            ["2-4", "6-8"],
            ["2-3", "4-5"],
            ["5-7", "7-9"],
            ["2-8", "3-7"],
            ["6-6", "4-6"],
            ["2-6", "4-8"],
        ]
    )


@pytest.mark.parametrize("input,expected", [(["5-7", "7-9"], True)])
def test_check_overlaps(input, expected):
    assert check_overlaps(input) == expected
