import pytest

from advent_2024_06 import solve_puzzle, string_to_grid, map_grid, Guard, Loop, solve_puzzle_loop

EXAMPLE = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def test_string_to_grid():
    the_string = """
111
222
"""
    expected_grid = [["1", "1", "1"], ["2", "2", "2"]]

    assert string_to_grid(the_string) == expected_grid


def test_map_grid():
    grid = [["#", "^"], [".", "#"]]
    obstructions, guard_coord = map_grid(grid)

    assert obstructions == {(0, 0), (1, 1)}
    assert guard_coord == (0, 1)


def test_solve_example_puzzle():
    assert solve_puzzle(EXAMPLE) == 41


def test_solve_example_puzzle_b():
    assert solve_puzzle_loop(EXAMPLE) == 6


def test_guard_walk():
    grid = [["#", "."], ["^", "#"], [".", "."]]
    obstructions, guard_coord = map_grid(grid)
    guard = Guard(guard_coord)

    expected_guard_position = (2, 0)
    assert guard.walk(obstructions).__next__() == expected_guard_position
    assert guard.visited == {(1, 0), (2, 0)}
    assert guard.path == [(1, 0), (2, 0)]


def test_guard_loop_detect():
    grid = [
        [".", "#", ".", "."],
        [".", ".", ".", "#"],
        ["#", "^", ".", "."],
        [".", ".", "#", "."],
    ]
    obstructions, guard_coord = map_grid(grid)
    guard = Guard(guard_coord)

    with pytest.raises(Loop):
        steps = 0
        for _ in guard.walk(obstructions):
            steps += 1
            if steps == 6:
                print(guard.path)
                break
