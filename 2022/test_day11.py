import pytest
from day11 import Monkey, MonkeyTest, process_monkey_file

@pytest.fixture(autouse=True, scope='function')
def cleanup_monkey():
    yield
    Monkey.monkeys = []

def test_process_a_monkey():
    with open('day11_single_monkey.txt', 'r') as infile:
        single_monkey = infile.read()

    expected = Monkey.from_monkey_block(single_monkey)

    assert expected.items == [79, 98]
    assert expected.modify_worry(current_worry=10) == 190
    assert expected.test.divisor == 23
    assert expected.test.true == 2
    assert expected.test.false == 3

def test_monkey_takes_turn():
    throwing_monkey = Monkey(items=[79, 98], operator=('*', 19), test=MonkeyTest(23, 1, 2))

    buffer_monkey = Monkey(items=[], operator=None, test=None)
    receiving_monkey = Monkey(items=[], operator=None, test=None)

    throwing_monkey.take_turn()

    assert throwing_monkey.items == []
    assert buffer_monkey.items == []
    assert receiving_monkey.items == [500, 620]


def test_process_example_monkey_file():

    assert process_monkey_file('test_day11_input.txt') == 10605
