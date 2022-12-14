import pytest

from day11 import Monkey

def test_process_a_monkey():
    with open('day11_single_monkey.txt', 'r') as infile:
        single_monkey = infile.read()

    expected = Monkey.from_monkey_block(single_monkey)

    assert expected.starting_items == [79, 98]
    assert expected.modify_worry(current_worry=10) == 190
    assert expected.test(current_worry=23) == (True, 2)
    assert expected.test(current_worry=24) == (False, 3)

