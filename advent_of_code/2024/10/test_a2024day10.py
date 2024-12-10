from a2024day10 import solve_puzzle, calculate_path, create_grid, get_neighbors, distinct_paths
import pytest

EXAMPLE = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

SIMPLE = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

SIMPLE_TWO = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

DISTINCT = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""

DISTINCT2 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987....
"""


def test_solve_puzzle_example():
    assert solve_puzzle(EXAMPLE) == (36, 81)


def test_create_grid():
    grid_str = ".1.\n..."
    expected = [
        [-1, 1, -1],
        [
            -1,
            -1,
            -1,
        ],
    ]
    assert create_grid(grid_str) == expected


@pytest.mark.parametrize(
    "str,origin,value",
    [
        (SIMPLE, (0, 3), 2),
        (SIMPLE_TWO, (0, 3), 4),
    ],
    ids=["SIMPLE", "SIMPLE2"],
)
def test_calculate_path(str, origin, value):
    grid = create_grid(str)
    assert calculate_path(origin, grid) == value


@pytest.mark.parametrize(
    "str,origin,value",
    [
        (DISTINCT, (0, 5), 3),
        (DISTINCT2, (0, 3), 13),
    ],
    ids=["DISTINCT", "DISTINCT2"],
)
def test_distinct_paths(str, origin, value):
    grid = create_grid(str)
    assert distinct_paths(origin, grid) == value


def test_get_neighbors():
    origin = (4, 4)
    neighbors = [(3, 4), (5, 4), (4, 3), (4, 5)]
    assert get_neighbors(origin) == neighbors
