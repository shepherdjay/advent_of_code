from advent_2024_04 import get_paths, search, solve_puzzle, solve_puzzle_diagonal

SIMPLE_EXAMPLE = """
..X...
.SAMX.
.A..A.
XMAS.S
.X....
"""

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

DIAG_EXAMPLE = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""


def as_grid(string):
    return [row for row in string.split("\n") if row]


def test_search_simple():
    row = 3
    col = 0
    initial_coord = (row, col)

    assert search(coord=initial_coord, grid=as_grid(SIMPLE_EXAMPLE), target_word="XMAS") == 1


def test_must_be_straight():
    row = 3
    col = 0
    initial_coord = (row, col)

    assert search(coord=initial_coord, grid=as_grid(SIMPLE_EXAMPLE), target_word="XMAS") == 1


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


def test_get_paths_only_diagonals():
    paths = get_paths((10, 10), 2, diagonals_only=True)
    assert len(paths) == 4


def test_solve_puzzle_diagnol():
    assert solve_puzzle_diagonal(DIAG_EXAMPLE) == 9
