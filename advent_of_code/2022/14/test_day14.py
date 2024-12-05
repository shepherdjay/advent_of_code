import pytest
from hypothesis import given
import hypothesis.strategies as st
from day14 import (
    can_fall,
    expand_coordinates,
    between_two_slates,
    simulate_sand,
    cave_in,
)


@st.composite
def xbound_coord(draw):
    """Returns two tuples where only the y coord varies"""
    x_value = draw(st.integers(min_value=0))
    a_coord = (x_value, draw(st.integers(min_value=0, max_value=500)))
    b_coord = (x_value, draw(st.integers(min_value=0, max_value=500)))
    return [a_coord, b_coord]


@st.composite
def ybound_coord(draw):
    """Returns two tuples where only the x coord varies"""
    y_value = draw(st.integers(min_value=0))
    a_coord = (draw(st.integers(min_value=0, max_value=500)), y_value)
    b_coord = (draw(st.integers(min_value=0, max_value=500)), y_value)
    return [a_coord, b_coord]


@pytest.mark.parametrize("a,b,expected", [((498, 6), (496, 6), {(498, 6), (497, 6), (496, 6)})])
def test_between_two_slates(a, b, expected):
    assert between_two_slates(a, b) == expected


@given(xbound_coord())
def test_property_between_two_slates_xbound(xbound_coords):
    """
    Given two (x,y) coordinates where only y varies assert
    between_two_slates returns a set of length n where n is
    the number of whole numbers between y1,y2 and themselves
    """
    assert (
        len(between_two_slates(*xbound_coords))
        == abs(xbound_coords[0][1] - xbound_coords[1][1]) + 1
    )


@given(ybound_coord())
def test_property_between_two_slates_ybound(ybound_coords):
    """
    Same as test_property_between_two_slates_xbound but where x varies
    """
    assert (
        len(between_two_slates(*ybound_coords))
        == abs(ybound_coords[0][0] - ybound_coords[1][0]) + 1
    )


@pytest.mark.parametrize(
    "rock_str,expected",
    [("498,4 -> 498,6 -> 496,6", {(498, 4), (498, 5), (498, 6), (497, 6), (496, 6)})],
)
def test_expand_positions(rock_str, expected):
    assert expand_coordinates(rock_str) == expected


def test_can_fall():
    rock_positions = expand_coordinates("498,4 -> 498,6 -> 496,6") | expand_coordinates(
        "503,4 -> 502,4 -> 502,9 -> 494,9"
    )

    assert can_fall((500, 0), rock_positions=rock_positions)
    assert can_fall((500, 8), rock_positions=rock_positions) is None


def test_simulate_sand():
    rock_positions = expand_coordinates("498,4 -> 498,6 -> 496,6") | expand_coordinates(
        "503,4 -> 502,4 -> 502,9 -> 494,9"
    )

    max_y = max([y for _, y in rock_positions])
    assert simulate_sand(rock_positions, max_y=max_y) == (500, 8)


@pytest.mark.parametrize("floor,expected", [(False, 24), (True, 93)])
def test_cave_in(floor, expected):
    rock_positions = expand_coordinates("498,4 -> 498,6 -> 496,6") | expand_coordinates(
        "503,4 -> 502,4 -> 502,9 -> 494,9"
    )

    assert cave_in(rock_positions, floor) == expected
