from advent_2025day02 import solve_puzzle, find_invalids, is_invalid_p2
import pytest

EXAMPLE = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
EXAMPLE_SOLUTION = 1227775554
EXAMPLE_SOLUTION_P2 = 4174379265


def test_solve_puzzle():
    assert solve_puzzle(EXAMPLE) == EXAMPLE_SOLUTION

def test_solve_puzzle_part2():
    assert solve_puzzle(EXAMPLE, part2=True) == EXAMPLE_SOLUTION_P2

@pytest.mark.parametrize("start,stop,expected", [
    (11,22,[11,22]),
    (95,115,[99]),
    (998,1012,[1010]),])
def test_find_invalids(start, stop, expected):
    assert find_invalids(start, stop) == expected

@pytest.mark.parametrize("n,expected", [
    (123123123, True),
    (1111111, True)])
def test_is_invalid_part2(n, expected):
    assert is_invalid_p2(n) == expected
