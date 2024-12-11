from advent_2024day11 import solve_puzzle, blink, blink_value
from itertools import islice
import pytest

EXAMPLE = "125 17"

@pytest.mark.parametrize('value,expected',[
    (0, [1]),
    (2024, [20,24]),
    (20, [2,0]),
    (1, [2024])
])
def test_blink_value(value, expected):
    assert blink_value(value) == expected


@pytest.mark.parametrize('blink_count,expected', [
    (1,3),
    (4,9),
    (5,13),
    (6,22)
])
def test_blink_example(blink_count, expected):
    result = blink([125, 17], blink_count=blink_count)
    assert result == expected

def test_solve_puzzle(benchmark):
    assert benchmark(solve_puzzle,EXAMPLE) == 55312