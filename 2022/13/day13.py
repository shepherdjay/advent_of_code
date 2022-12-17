from typing import List, Union
import itertools

Packet = List[Union[List, int]]


class Comparable:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        if not isinstance(other, Comparable):
            raise TypeError

        return comparator(self.x, other.x)

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return f'Comparable(x={self.x}'


def comparator(a: Packet, b: Packet):
    for pair in itertools.zip_longest(a, b):
        match pair:
            case list(), list():
                sub_search = comparator(*pair)
                if sub_search is not None:
                    return sub_search
            case int(), int():
                if pair[0] == pair[1]:
                    continue
                return pair[0] < pair[1]
            case None, _:
                return True
            case _, None:
                return False
            case left, right:
                if isinstance(left, int):
                    left = [left]
                else:
                    right = [right]
                sub_search = comparator(left, right)
                if sub_search is not None:
                    return sub_search


def sum_correct(pairs):
    # TODO: Replace eval with tokenizer to be input safe
    results = (comparator(eval(a), eval(b)) for a, b in pairs)
    return sum(count for count, result in enumerate(results, start=1) if result is True)


def process_file(filename):
    with open(filename, 'r') as elf_file:
        pairs = [pair.split('\n') for pair in elf_file.read().split('\n\n')]

    return sum_correct(pairs)


def process_file_v2(filename):
    with open(filename, 'r') as elf_file:
        raw_lines = [line.strip() for line in elf_file if line]

    divider_a = Comparable([[2]])
    divider_b = Comparable([[6]])

    comparable = [Comparable(eval(x)) for x in raw_lines if x != '']
    comparable.extend([divider_a, divider_b])
    comparable.sort()

    decode_a, decode_b = map(lambda x: comparable.index(x) + 1, [divider_a, divider_b])

    return decode_a * decode_b


if __name__ == '__main__':
    print(process_file('day13_input.txt'))
    print(process_file_v2('day13_input.txt'))
