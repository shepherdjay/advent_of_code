import re
from typing import List

PUZZLE_STATE = [
    ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
    ['D', 'N', 'T', 'S', 'B', 'Z'],
    ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
    ['G', 'R', 'Z'],
    ['Z', 'N', 'R', 'H'],
    ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
    ['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
    ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
    ['S', 'Q', 'P', 'W', 'N']
]


def split_instruction(instruction_string: str) -> List:
    """
    >>> split_instruction('move 1 from 2 to 5')
    [1, 2, 5]
    """
    ins_regex = re.compile(r'move (\d+) from (\d+) to (\d+)')
    return [int(_) for _ in ins_regex.findall(instruction_string)[0]]


def process_instruction(instruction_string: str, state=PUZZLE_STATE) -> None:
    """
    >>> puz_state = [['Z','N'],['M','C','D'],['P']]
    >>> process_instruction('move 1 from 2 to 1', state=puz_state)
    >>> print(puz_state)
    [['Z', 'N', 'D'], ['M', 'C'], ['P']]
    """

    times, from_row, to_row = split_instruction(instruction_string)

    for _ in range(times):
        box = state[from_row - 1].pop()
        state[to_row - 1].append(box)


if __name__ == '__main__':
    with open('advent_05_input.txt', 'r') as infile:
        for line in infile:
            if line.startswith('move'):
                process_instruction(line.strip())
    for row in PUZZLE_STATE:
        print(row[-1], end='')
