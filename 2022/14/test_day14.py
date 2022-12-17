import pytest
from day14 import can_fall, expand_coordinates, between_two_slates, simulate_sand, cave_in


@pytest.mark.parametrize('a,b,expected', [
    ((498, 6), (496, 6), {(498, 6), (497, 6), (496, 6)})
])
def test_between_two_slates(a, b, expected):
    assert between_two_slates(a, b) == expected


@pytest.mark.parametrize('rock_str,expected', [
    ("498,4 -> 498,6 -> 496,6", {(498, 4),
     (498, 5), (498, 6), (497, 6), (496, 6)})
])
def test_expand_positions(rock_str, expected):
    assert expand_coordinates(rock_str) == expected


def test_can_fall():
    rock_positions = expand_coordinates(
        "498,4 -> 498,6 -> 496,6") | expand_coordinates("503,4 -> 502,4 -> 502,9 -> 494,9")

    assert can_fall((500, 0), rock_positions=rock_positions)
    assert can_fall((500, 8), rock_positions=rock_positions) is None


def test_simulate_sand():
    rock_positions = expand_coordinates(
        "498,4 -> 498,6 -> 496,6") | expand_coordinates("503,4 -> 502,4 -> 502,9 -> 494,9")

    assert simulate_sand(rock_positions) == (500, 8)


def test_cave_in():
    rock_positions = expand_coordinates(
        "498,4 -> 498,6 -> 496,6") | expand_coordinates("503,4 -> 502,4 -> 502,9 -> 494,9")

    assert cave_in(rock_positions) == 24
    assert cave_in(rock_positions, floor=True) == 93