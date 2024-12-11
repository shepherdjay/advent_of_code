from advent_2024day11 import solve_puzzle, blink

EXAMPLE = "125 17"

def test_blink():
    assert blink([125, 17]) == [253000, 1, 7]

def test_solve_puzzle():
    assert solve_puzzle(EXAMPLE) == 55312