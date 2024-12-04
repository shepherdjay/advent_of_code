import pytest

from advent_2024_02 import check_level_safety, safe_level_count


@pytest.mark.parametrize(
    "level,safe",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([1,3,2,4,5], False),
    ],
)
def test_check_level_safety(level, safe):
    assert check_level_safety(level) == safe

@pytest.mark.parametrize(
    "level,safe",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([1,3,2,4,5], True)
    ],
)
def test_check_level_safety_dampen(level, safe):
    assert check_level_safety(level, dampen=True) == safe


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
