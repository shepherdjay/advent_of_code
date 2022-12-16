from typing import List, Union
import itertools

Packet = List[Union[List, int]]


class Var:
    pass


var = Var()


def comparator(a: Packet, b: Packet):
    zipped = itertools.zip_longest(a, b)
    for left, right in zipped:
        if left is None:
            return True
        if right is None:
            return False
        if all(map(lambda x: isinstance(x, list), [left, right])):
            sub_search = comparator(left, right)
            if sub_search is not None:
                return sub_search
            else:
                continue
        elif any(map(lambda x: isinstance(x, list), [left, right])):
            if isinstance(left, int):
                left = [left]
            else:
                right = [right]
            sub_search = comparator(left, right)
            if sub_search is not None:
                return sub_search
            else:
                continue
        else:
            if left == right:
                continue
            return left < right


def sum_correct(pairs):
    # TODO: Replace eval with tokenizer to be input safe
    results = (comparator(eval(a), eval(b)) for a, b in pairs)
    return sum(count for count, result in enumerate(results, start=1) if result is True)


def process_file(filename):
    with open(filename, 'r') as elf_file:
        pairs = [pair.split('\n') for pair in elf_file.read().split('\n\n')]

    return sum_correct(pairs)


if __name__ == '__main__':
    print(process_file('day13_input.txt'))
