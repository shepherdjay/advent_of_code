from pathlib import Path
from tqdm import tqdm
from typing import Generator
from collections import deque

BASEPATH = Path(__file__).parent.resolve()

def blink_value(value: int) -> list[int]:
    val_len = len(str(value))
    if value == 0:
        return [1]
    elif val_len % 2 == 0:
        left, right = int(str(value)[0:val_len // 2]),   int(str(value)[val_len // 2::])
        return [left, right]
    else:
        return [value * 2024]

def blink(input_list: list[int]) -> Generator[list]:
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    queue = deque(input_list)
    list_length = len(input_list)
    while True:
        for _ in range(list_length):
            cur_value = queue.popleft()
            result = blink_value(cur_value)
            if len(result) == 2:
                list_length += 1
            for value in result:
                queue.append(value)
        yield list_length
        

    list_length = 0
    processed = 0
    queue = input_list
    length = len(input_list)
    while count != 0:
        cur_value = queue.pop(0)
        result = blink_value(cur_value)
        result.append(queue)
        length += len(result)
        processed += 1
        if processed == to_process:
            count -=1
    return length

def solve_puzzle(puzzle_input, part2=False):
    initial = [int(i) for i in puzzle_input.strip().split()]
    blink_count = 25
    blink_gen = blink(initial)

    if part2:
        blink_count = 75

    for _ in range(blink_count):
        result = next(blink_gen)

    return result

if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip('\n')

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    part_b = solve_puzzle(puzzle_input, part2=True)
    print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        submit(part_b, part="b", session=session)
    except AocdError as e:
        pass