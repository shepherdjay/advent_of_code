from pathlib import Path
from tqdm import tqdm
from typing import Generator
from functools import cache, lru_cache

BASEPATH = Path(__file__).parent.resolve()

@cache
def blink_value(value: int) -> list[int]:
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    val_len = len(str(value))
    if value == 0:
        return [1]
    elif val_len % 2 == 0:
        left, right = int(str(value)[0:val_len // 2]),   int(str(value)[val_len // 2::])
        return [left, right]
    else:
        return [value * 2024]

@cache
def blink_recurse(stone,  blink_count=1, depth=0):
    total = 0
    if depth == blink_count:
        total += 1
    else:
        for new_stone in blink_value(stone):
            total += blink_recurse(new_stone, blink_count, depth + 1)
    return total

def blink_fifo(input_list: list[int], blink_count=1) -> int:
    queue = [(v, 0) for v in input_list]
    memo = {}
    leafs = 0

    while queue:
        stone, depth = queue.pop()
        if depth == blink_count:
            leafs += 1
            continue
        for new_stone in blink_value(stone):
            queue.append((new_stone, depth + 1))
    
    return leafs

def blink(input_list: list[int], blink_count=1) -> int:
    stones_map = {i:1 for i in input_list}
    for _ in range(blink_count):
        stones = [k for k,v in stones_map.items() if v >= 1 for _ in range(v)]
        for stone in stones:
            stones_map[stone] -= 1
            for new_stone in blink_value(stone):
                stones_map[new_stone] = stones_map.get(new_stone, 0) + 1
            
    return sum(stones_map.values())


def solve_puzzle(puzzle_input, part2=False):
    initial = [int(i) for i in puzzle_input.strip().split()]
    blink_count = 25
    if part2:
        blink_count = 75

    result = sum( [blink_recurse(stone, blink_count) for stone in initial] )

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