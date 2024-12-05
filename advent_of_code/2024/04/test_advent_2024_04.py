from advent_2024_04 import get_paths, search, solve_puzzle

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

    assert search(coord=initial_coord, grid=SIMPLE_EXAMPLE_AS_GRID, target_word="XMAS") == 1


def test_must_be_straight():
    row = 3
    col = 0
    initial_coord = (row, col)

    assert search(coord=initial_coord, grid=SIMPLE_EXAMPLE_AS_GRID, target_word="XMAS") == 1


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


def test_get_paths():
    paths = get_paths((10, 10), 4)
    assert len(paths) == 8
