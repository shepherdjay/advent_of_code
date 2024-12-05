import pytest

from advent_2024_02 import (
    check_level_safety,
    safe_level_count,
    analyze_row,
    generate_subrows,
)


@pytest.mark.parametrize(
    "level,safe_result",
    [
        # PROVIDED EXAMPLES
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True),
        # CUSTOM
        ([10, 11, 10, 9, 8], False),
    ],
)
def test_check_level_safety(level, safe_result):
    assert check_level_safety(level) == safe_result


@pytest.mark.parametrize(
    "level,dampen_result",
    [
        # PROVIDED EXAMPLES
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
        # CUSTOM
        ([10, 11, 10, 9, 8], True),
        ([11, 10, 9, 8, 9], True),
    ],
)
def test_check_level_safety_dampen(level, dampen_result):
    assert check_level_safety(level, dampen=True) == dampen_result


def test_analyze_row_constrained():
    row = [7, 6, 4, 2, 1]

    assert analyze_row(row, increasing=True) is False
    assert analyze_row(row, increasing=False) is True


def test_generate_subrows():
    row = [7, 6, 4, 2, 1]

    assert generate_subrows(row) == [
        [6, 4, 2, 1],
        [7, 4, 2, 1],
        [7, 6, 2, 1],
        [7, 6, 4, 1],
        [7, 6, 4, 2],
    ]


def test_check_full_example_report():
    example = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

    assert safe_level_count(example) == 2
