import pytest

import advent_2024_07 as advent

EXAMPLE = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def test_solve_puzzle():
    assert advent.solve_puzzle(EXAMPLE) == 3749

def test_solve_layer_simple():
    target_number = 190
    values = advent.deque([10,19])

    assert advent.solve_layer(target=target_number, values=values)

def test_solve_layer_more():
    target = 3267
    values = advent.deque([81, 40, 27])

    assert advent.solve_layer(target=target, values=values)
