import pytest

from advent_2023_02 import (
    sum_of_possible,
    process_game_data,
    check_hypothesis,
    sum_powers,
)


SAMPLE_GAMESTRING = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

SAMPLE_HYPOTHESIS = {"red": 12, "green": 13, "blue": 14}


def test_sum_of_possible():
    bag_hypothesis = {"red": 12, "green": 13, "blue": 14}
    assert sum_of_possible(SAMPLE_GAMESTRING, bag_hypothesis) == 8


def test_process_game_data():
    assert process_game_data("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {
        "blue": 6,
        "red": 4,
        "green": 2,
    }


@pytest.mark.parametrize(
    "hypothesis,game_max_colors,expected_bool",
    [
        (SAMPLE_HYPOTHESIS, {"blue": 6, "red": 4, "green": 2}, True),
        (SAMPLE_HYPOTHESIS, {"red": 20, "blue": 6, "green": 13}, False),
    ],
)
def test_check_hypothesis(hypothesis, game_max_colors, expected_bool):
    assert (
        check_hypothesis(hypothesis=SAMPLE_HYPOTHESIS, color_values=game_max_colors)
        == expected_bool
    )


def test_sum_powers():
    assert sum_powers(SAMPLE_GAMESTRING) == 2286
