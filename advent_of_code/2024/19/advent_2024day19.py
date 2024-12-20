from functools import cache
from pathlib import Path

import tqdm

#
# import sys
# sys.setrecursionlimit(1500)

BASEPATH = Path(__file__).parent.resolve()


def parse(puzzle_input):
    towels_str, patterns_str = puzzle_input.split("\n\n")
    towels = set(towels_str.replace(" ", "").split(","))
    patterns = [line for line in patterns_str.split("\n")]

    return towels, patterns


def solve_puzzle(puzzle_input, part2=False):
    towels, patterns = parse(puzzle_input)
    count = 0
    for pattern in tqdm.tqdm(patterns):
        trimmed_towels = frozenset({towel for towel in towels if towel in pattern})
        if not part2:
            count += try_combinations(trimmed_towels, pattern)
        else:
            count += try_combinations(trimmed_towels, pattern, part2=True)
    return count


@cache
def try_combinations(towels, pattern: str, total=0, part2=False):
    if pattern == "":
        return True

    results = []
    for towel in towels:
        if pattern.startswith(towel):
            results.append(
                try_combinations(towels, pattern.removeprefix(towel), total=total, part2=part2)
            )

    if part2:
        total += sum(results)
        return total
    return any(results)


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read()

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
