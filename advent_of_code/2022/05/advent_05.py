import re
from typing import List

PUZZLE_STATE = [
    ["N", "C", "R", "T", "M", "Z", "P"],
    ["D", "N", "T", "S", "B", "Z"],
    ["M", "H", "Q", "R", "F", "C", "T", "G"],
    ["G", "R", "Z"],
    ["Z", "N", "R", "H"],
    ["F", "H", "S", "W", "P", "Z", "L", "D"],
    ["W", "D", "Z", "R", "C", "G", "M"],
    ["S", "J", "F", "L", "H", "W", "Z", "Q"],
    ["S", "Q", "P", "W", "N"],
]


def split_instruction(instruction_string: str) -> List:
    """
    >>> split_instruction('move 1 from 2 to 5')
    [1, 2, 5]
    """
    ins_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
    return [int(_) for _ in ins_regex.findall(instruction_string)[0]]


def process_instruction(instruction_string: str, state=PUZZLE_STATE) -> None:
    """
    >>> puz_state = [['Z','N'],['M','C','D'],['P']]
    >>> process_instruction('move 1 from 2 to 1', state=puz_state)
    >>> print(puz_state)
    [['Z', 'N', 'D'], ['M', 'C'], ['P']]
    """

    times, from_row, to_row = split_instruction(instruction_string)

    # zero_indexing
    from_row = from_row - 1
    to_row = to_row - 1

    for _ in range(times):
        box = state[from_row].pop()
        state[to_row].append(box)


def process_instruction_9001(instruction_string: str, state=PUZZLE_STATE) -> None:
    """
    >>> puz_state = [['Z','N'],['M','C','D'],['P']]
    >>> process_instruction_9001('move 2 from 2 to 1', state=puz_state)
    >>> print(puz_state)
    [['Z', 'N', 'C', 'D'], ['M'], ['P']]
    """

    times, from_row, to_row = split_instruction(instruction_string)

    # zero_indexing
    from_row = from_row - 1
    to_row = to_row - 1

    start_slice = len(state[from_row]) - times
    boxes = state[from_row][start_slice::]
    for _ in range(times):
        state[from_row].pop()
    state[to_row].extend(boxes)


if __name__ == "__main__":
    machine = {"9000": process_instruction, "9001": process_instruction_9001}

    with open("advent_05_input.txt", "r") as infile:
        for line in infile:
            if line.startswith("move"):
                machine["9001"](line.strip())
    for row in PUZZLE_STATE:
        print(row[-1], end="")
