from typing import Tuple, NamedTuple
import re

class MonkeyTest(NamedTuple):
    divisor: int
    true: int
    false: int

class Monkey:
    monkeys = []

    def __init__(self, starting_items, operator: Tuple[str, int], test: MonkeyTest) -> None:
        self.starting_items = starting_items
        self.operator = operator
        self.test = test

        self.monkey_ops = {
            '+' : self.add,
            '*' : self.multiply,
        }


    def modify_worry(self, current_worry):
        operation, modifier = self.operator
        return self.monkey_ops[operation](current_worry, modifier)

    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

    @classmethod
    def from_monkey_block(cls, monkeystring):
        stripped_data = monkeystring.splitlines()

        starting_items = [int(x) for x in re.findall(r'\d+', stripped_data[1])]
        operator_raw = re.findall(r'old ([+*]) (\d+)', stripped_data[2])[0]
        operation, modifier = operator_raw[0], int(operator_raw[1])
        print(operator_raw)
        test_raw = stripped_data[3::]

        return Monkey(
            starting_items=starting_items,
            operator = (operation, modifier),
            test = test_raw
        )
