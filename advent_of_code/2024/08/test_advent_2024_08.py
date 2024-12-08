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


def test_map_antennas():
    grid = [
        [".", ".", ".", "C", "."],
        [".", "A", "A", ".", "."],
    ]
    assert advent.map_antennas(grid) == {"C": [(0, 3)], "A": [(1, 1), (1, 2)]}


@pytest.mark.parametrize(
    "antennas,expected",
    [({"A": [(1, 1), (1, 2)]}, {(1, 1): {0}}), ({"A": [(1, 1), (2, 1)]}, {(1, 1): {"undefined"}})],
)
def test_calculate_slopes(antennas, expected):
    assert advent.calculate_slopes(antennas) == expected


@pytest.mark.parametrize(
    "origin,slopes,result",
    [
        ((1, 0), {(1, 1): {0}}, True),
        ((1, 3), {(1, 1): {0}}, True),
        ((2, 3), {(1, 1): {0}}, False),
        [(5, 0), {(3, 0): {"undefined"}}, True],
        [(1, 0), {(3, 0): {"undefined"}}, True],
    ],
)
def test_on_a_slope(origin, slopes, result):
    assert advent.on_a_slope(origin, slopes) is result


@pytest.mark.parametrize(
    "puzzle_input,expected",
    [
        ("...C.\n.AA..", 5),
        ("...C.\n.....", 0),
        ("...\n.A.\n.A.\n...", 4),
    ],
)
def test_solve_puzzle_two_simple(puzzle_input, expected):
    assert advent.solve_puzzle_two(puzzle_input) == expected


def test_solve_puzzle_example():
    assert advent.solve_puzzle(EXAMPLE) == 14
