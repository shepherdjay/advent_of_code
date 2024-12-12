from advent_2024day11 import solve_puzzle, blink_value, blink_recurse
import pytest

EXAMPLE = "125 17"


@pytest.mark.parametrize("value,expected", [(0, [1]), (2024, [20, 24]), (20, [2, 0]), (1, [2024])])
def test_blink_value(value, expected):
    assert blink_value(value) == expected


@pytest.mark.parametrize("blink_count,expected", [(1, 3), (4, 9), (5, 13), (6, 22)])
def test_blink_recurse(blink_count, expected):
    result = sum([blink_recurse(stone, blink_count=blink_count) for stone in [125, 17]])
    assert result == expected


def test_solve_puzzle():
    assert solve_puzzle(EXAMPLE) == 55312
