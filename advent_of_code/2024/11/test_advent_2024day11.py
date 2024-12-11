from advent_2024day11 import solve_puzzle, blink
from itertools import islice

EXAMPLE = "125 17"

def test_blink():
    blink_gen = blink([125, 17])
    for _ in range(6):
        result = next(blink_gen)
    assert result == 22
    assert False

def test_solve_puzzle():
    assert solve_puzzle(EXAMPLE) == 55312