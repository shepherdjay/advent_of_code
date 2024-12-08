import pytest
from hypothesis import given, strategies as st

import advent_2024_08 as advent

EXAMPLE = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


@st.composite
def aninode_diagonal(draw):
    initial = draw(st.tuples(st.integers(min_value=0), st.integers(min_value=0)))
    aninode = (initial[0] * 2, initial[1] * 2)

    return initial, aninode


@given(aninode_diagonal())
def test_calculate_double_property(sample):
    initial, aninode = sample
    orig_coord = (0, 0)  # zzero index for hypothesis

    advent.calculate_double(orig_coord, initial) == aninode


@pytest.mark.parametrize(
    "orig_coord, target_coord, expected",
    [
        ((1, 1), (3, 3), (5, 5)),
        ((1, 0), (3, 3), (5, 6)),
        ((5, 5), (4, 4), (3, 3)),
    ],
)
def test_calculate_double(orig_coord, target_coord, expected):
    assert advent.calculate_double(orig_coord, target_coord) == expected


def test_at_anninode():
    antenna_map = {"A": {(3, 3), (5, 5)}}
    assert advent.at_anninode((1, 1), antenna_map)
    assert not advent.at_anninode((1, 0), antenna_map)


def test_solve_puzzle_simple():
    puzzle_input = """
    ....
    .AA.
    """

    assert advent.solve_puzzle(puzzle_input) == 2

@pytest.mark.xfail("not yet started")
def test_solve_puzzle_two_simple():
    puzzle_input = """
    ...C.
    .AA..
    """
    assert advent.solve_puzzle_two(puzzle_input) == 5


def test_solve_puzzle_example():
    assert advent.solve_puzzle(EXAMPLE) == 14
