import pytest
from day11 import Monkey, MonkeyTest, process_monkey_file


@pytest.fixture(autouse=True, scope="function")
def cleanup_monkey():
    yield
    Monkey.monkeys = []


def test_process_a_monkey():
    with open("day11_single_monkey.txt", "r") as infile:
        single_monkey = infile.read()

    actual = Monkey.from_monkey_block(single_monkey)

    assert actual.items == [79, 98]
    assert actual.modify_worry(current_worry=10) == 190 % 23
    assert actual.test.divisor == 23
    assert actual.test.true == 2
    assert actual.test.false == 3


def test_monkey_takes_turn():
    throwing_monkey = Monkey(
        items=[79, 98], operator=("*", 19), test=MonkeyTest(23, 1, 2)
    )

    buffer_monkey = Monkey(items=[], operator=None, test=MonkeyTest(23, 1, 2))
    receiving_monkey = Monkey(items=[], operator=None, test=MonkeyTest(23, 1, 2))

    throwing_monkey.take_turn()

    assert throwing_monkey.items == []
    assert buffer_monkey.items == []
    assert receiving_monkey.items == [500, 620]


def test_process_example_monkey_file():
    assert process_monkey_file("test_day11_input.txt") == 10605


def test_process_example_monkey_file_lots_of_rounds():
    process_monkey_file("test_day11_input.txt", num_rounds=5_000, worry_divisor=1)

    assert Monkey.monkeys[0].items_inspected == 26075
    assert Monkey.monkeys[1].items_inspected == 23921
    assert Monkey.monkeys[2].items_inspected == 974
    assert Monkey.monkeys[3].items_inspected == 26000
