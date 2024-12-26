from sample_2024day25 import EXAMPLE
from advent_2024day25 import solve_puzzle, Key, Lock, parse, parse_individual, grid_it


def test_grid_it():
    input_str = """11
    2"""

    expected = [
        ['1','1'],
        ['2']
    ]
    assert grid_it(input_str) == expected

def test_parse_individual_lock():
    input_str = """#####
.####
.####
.####
.#.#.
.#...
....."""

    result = parse_individual(input_str)
    assert isinstance(result, Lock)
    assert result.pins == [0,5,3,4,3]

def test_parse_individual_key():
    input_str = """.....
#....
#....
#...#
#.#.#
#.###
#####"""

    result = parse_individual(input_str)
    assert isinstance(result, Key)
    assert result.heights == [5,0,2,1,3]

def test_parse():
    input_str = EXAMPLE
    keys, locks = parse(input_str)
    assert len(keys) == 3
    assert len(locks) == 2

def test_solve_puzzle():
    puzzle_input = EXAMPLE
    assert solve_puzzle(puzzle_input) == 3

