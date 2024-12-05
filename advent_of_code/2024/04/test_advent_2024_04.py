import pytest

from advent_2024_04 import solve_puzzle, get_neighbor_coord, get_neighbors, search

SIMPLE_EXAMPLE = """
..X...
.SAMX.
.A..A.
XMAS.S
.X....
"""
SIMPLE_EXAMPLE_AS_GRID = [row for row in SIMPLE_EXAMPLE.split("\n") if row]

EXAMPLE = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

EXAMPLE_AS_GRID = [row for row in EXAMPLE.split("\n") if row]


def test_search_simple():
    row = 3
    col = 0
    initial_coord = (row, col)

    assert (
        search(
            initial_coord=initial_coord,
            grid=SIMPLE_EXAMPLE_AS_GRID,
            original=initial_coord,
        )
        == 1
    )


def test_must_be_straight():
    row = 3
    col = 0
    initial_coord = (row, col)

    assert (
        search(
            initial_coord=initial_coord,
            grid=SIMPLE_EXAMPLE_AS_GRID,
            original=initial_coord,
        )
        == 1
    )


@pytest.mark.parametrize(
    "coord,expected", [((0, 0), set([(".", (0, 1)), (".", (1, 0)), ("S", (1, 1))]))]
)
def test_get_neighbors(coord, expected):
    assert get_neighbors(coord, SIMPLE_EXAMPLE_AS_GRID) == expected


def test_solve_puzzle_simple():
    assert solve_puzzle(SIMPLE_EXAMPLE) == 4


def test_solve_puzzle():
    assert solve_puzzle(EXAMPLE) == 18


def test_solve_puzzle_only_straight():
    bad_example = """
XVCS
VMAC
"""
    assert solve_puzzle(bad_example) == 0
