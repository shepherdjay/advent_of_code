from advent_2025day03 import find_largest_joltage, solve_puzzle, get_next_largest_digit
import pytest

EXAMPLE = """987654321111111
811111111111119
234234234234278
818181911112111"""


@pytest.mark.parametrize(
    "battery_bank, banks_to_turn_on, expected",
    [
        ("987654321111111", 2, 98),
        ("811111111111119", 2, 89),
        ("818181911112111", 2, 92),
        ("987654321111111", 12, 987654321111),
        ("818181911112111", 12, 888911112111),
    ],
)
def test_find_largest_joltage(battery_bank, banks_to_turn_on, expected):
    assert find_largest_joltage(battery_bank, banks_to_turn_on) == expected


def test_get_next_largest_digit():
    larg_digit_example = "123456789"
    larg_digit_gen = get_next_largest_digit("123456789", num_of_characters=len(larg_digit_example))
    for char in larg_digit_example:
        assert next(larg_digit_gen) == char


def test_solve_puzzle_p1():
    assert solve_puzzle(EXAMPLE) == 357


def test_solve_puzzle_p2():
    assert solve_puzzle(EXAMPLE, part2=True) == 3121910778619
