from typing import Tuple, NamedTuple
import re


class MonkeyTest(NamedTuple):
    divisor: int
    true: int
    false: int


class Monkey:
    monkeys = []

    def __init__(self, items, operator: Tuple[str, int], test: MonkeyTest) -> None:
        self.items = items
        self.operator = operator
        self.test = test
        self.items_inspected = 0

        self.monkey_ops = {
            '+': self.add,
            '*': self.multiply,
        }

        self.monkeys.append(self)

    def receive_item(self, item: int):
        self.items.append(item)

    def take_turn(self):
        for item in self.items:
            self.items_inspected += 1
            new_worry = self.modify_worry(item) // 3

            if new_worry % self.test.divisor == 0:
                new_monkey = self.test.true
            else:
                new_monkey = self.test.false

            self.monkeys[new_monkey].receive_item(new_worry)
        self.items = []

    def modify_worry(self, current_worry):
        operation, modifier = self.operator
        return self.monkey_ops[operation](current_worry, modifier)

    @staticmethod
    def add(a, b):
        if b == 'old':
            return a + a
        return a + b

    @staticmethod
    def multiply(a, b):
        if b == 'old':
            return a * a
        return a * b

    @classmethod
    def from_monkey_block(cls, monkeystring):
        stripped_data = monkeystring.splitlines()
        re_num = re.compile(r'\d+')

        starting_items = [int(x) for x in re_num.findall(stripped_data[1])]

        try:
            operator_raw = re.findall(r'old ([+*]) (\d+)', stripped_data[2])[0]
            operation, modifier = operator_raw[0], int(operator_raw[1])

        except IndexError:
            operator_raw = re.findall(r'old ([+*]) (old)', stripped_data[2])[0]
            operation, modifier = operator_raw[0], operator_raw[1]

        test_raw = [line for line in stripped_data[3::]]

        divisor = int(re_num.findall(test_raw[0])[0])
        true_idx = int(re_num.findall(test_raw[1])[0])
        false_idx = int(re_num.findall(test_raw[2])[0])

        monkey_test = MonkeyTest(divisor=divisor, true=true_idx, false=false_idx)

        return Monkey(
            items=starting_items,
            operator=(operation, modifier),
            test=monkey_test
        )


def process_monkey_file(filename):
    with open(filename, 'r') as monkeyfile:
        monkey_blocks = monkeyfile.read().split('\n\n')

    for monkey_block in monkey_blocks:
        Monkey.from_monkey_block(monkey_block)

    assert len(Monkey.monkeys) > 0

    for _ in range(20):
        for monkey in Monkey.monkeys:
            monkey.take_turn()

    top_performers = sorted(Monkey.monkeys, key=lambda x: x.items_inspected, reverse=True)

    return top_performers[0].items_inspected * top_performers[1].items_inspected


if __name__ == '__main__':
    monkey_business = process_monkey_file('day11_input.txt')

    print(f'{len(Monkey.monkeys)} monkeys caused {monkey_business} worth of monkey business.')
