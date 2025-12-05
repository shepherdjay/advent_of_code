from advent_2025day04 import solve_puzzle, parse_grid

EXAMPLE_INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def test_solve_puzzle_p1():
    assert solve_puzzle(EXAMPLE_INPUT) == 13

def test_solve_puzzle_p2():
    assert solve_puzzle(EXAMPLE_INPUT, part2=True) == 43

def test_parse_grid():
    grid_str = """..@\n..@"""

    grid = parse_grid(grid_str)

    assert grid == [['.', '.', '@'], ['.', '.', '@']]