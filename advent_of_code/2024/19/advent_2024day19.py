from pathlib import Path
import re
import tqdm
from functools import cache
from queue import PriorityQueue

BASEPATH = Path(__file__).parent.resolve()


def parse(puzzle_input):
    towels_str, patterns_str = puzzle_input.split("\n\n")
    towels = set(towels_str.replace(" ", "").split(","))
    patterns = [line for line in patterns_str.split("\n")]

    return towels, patterns


# def try_combinations(towels: list[str], pattern: str) -> bool:
#     trimmed_towels = [towel for towel in towels if towel in pattern]
#     or_statement = '|'.join(trimmed_towels)
#     re_pattern = re.compile(fr'(?:{or_statement})+')
#     if re_pattern.fullmatch(pattern):
#         return True
#     return False

# def try_combinations(towels: set[str], pattern: str) -> bool:
#     if not pattern:
#         return True
#
#     trimmed_towels = set([towel for towel in towels if towel in pattern])
#     results = [try_combinations(towels, pattern.replace(towel, '')) for towel in trimmed_towels if towel in pattern]
#
#     return any(results)


def try_combinations(towels: set[str], pattern: str) -> bool:
    trimmed_towels = {towel for towel in towels if towel in pattern}
    if len(trimmed_towels) == 0:
        return False

    stack = PriorityQueue()
    stack.put((0, pattern, trimmed_towels))
    visited = set()

    while not stack.empty():
        removed_char, cur_pattern, avail_towels = stack.get()
        avail_towels = {towel for towel in avail_towels if towel in cur_pattern}

        if cur_pattern in visited:
            continue

        visited.add(cur_pattern)
        for towel in avail_towels:
            possible_count = cur_pattern.count(towel)
            new_towels = set(avail_towels)
            new_towels.remove(towel)
            for i in range(possible_count + 1):
                if i == 0:
                    continue
                neighbor_string = cur_pattern.replace(towel, "", count=i)
                if neighbor_string == "":
                    return True
                updated_char_count = removed_char - (i * len(towel))
                stack.put((updated_char_count, neighbor_string, new_towels))
    return False


def solve_puzzle(puzzle_input, part2=False):
    towels, patterns = parse(puzzle_input)
    count = 0
    for pattern in tqdm.tqdm(patterns):
        count += try_combinations(towels, pattern)
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
