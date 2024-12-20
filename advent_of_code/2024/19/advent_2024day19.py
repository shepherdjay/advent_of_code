from pathlib import Path
import re
import tqdm
from functools import cache
from queue import PriorityQueue
#
# import sys
# sys.setrecursionlimit(1500)

BASEPATH = Path(__file__).parent.resolve()


def parse(puzzle_input):
    towels_str, patterns_str = puzzle_input.split("\n\n")
    towels = set(towels_str.replace(" ", "").split(","))
    patterns = [line for line in patterns_str.split("\n")]

    return towels, patterns

@cache
def try_combinations(towels: set, pattern):
    if pattern.replace(" ", "") == "":
        return True

    towels = frozenset({towel for towel in towels if towel in pattern})
    if not towels:
        return False

    print(pattern, towels)

    return any([try_combinations(towels, pattern.replace(towel, " ")) for towel in towels])

# def try_combinations(towels: set[str], pattern: str) -> bool:
#     trimmed_towels = {towel for towel in towels if towel in pattern}
#     if len(trimmed_towels) == 0:
#         return False
#
#     stack = PriorityQueue()
#     stack.put((0, pattern, trimmed_towels, list()))
#     visited = set()
#
#     while not stack.empty():
#         removed_char, cur_pattern, avail_towels, used_towels = stack.get()
#         avail_towels = {towel for towel in avail_towels if towel in cur_pattern}
#
#         if cur_pattern in visited:
#             continue
#
#         visited.add(cur_pattern)
#
#         for towel in avail_towels:
#             possible_count = cur_pattern.count(towel)
#             new_towels = set(avail_towels)
#             new_towels.remove(towel)
#             for i in range(possible_count + 1):
#                 if i == 0:
#                     continue
#                 neighbor_string = cur_pattern.replace(towel, " ", count=i)
#                 if neighbor_string.strip() == "":
#                     return True
#
#                 new_used = [used for used in used_towels]
#                 new_used.append((towel, i))
#                 updated_char_count = removed_char - (i * len(towel))
#                 stack.put((updated_char_count, neighbor_string, new_towels, new_used))
#     return False


def solve_puzzle(puzzle_input, part2=False):
    towels, patterns = parse(puzzle_input)
    count = 0
    for pattern in patterns:
        trimmed_towels = frozenset({towel for towel in towels if towel in pattern})
        count += try_combinations(trimmed_towels, pattern)
    return count


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    # part_b = solve_puzzle(puzzle_input, part2=True)
    # print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        # submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
