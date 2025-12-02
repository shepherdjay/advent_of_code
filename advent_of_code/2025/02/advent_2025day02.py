from pathlib import Path
import textwrap

BASEPATH = Path(__file__).parent.resolve()


def is_invalid(n: int) -> bool:
    n = str(n)
    if len(n) % 2 != 0:
        return False
    first_part, second_part = n[: len(n) // 2], n[len(n) // 2 :]
    return first_part == second_part


def is_invalid_p2(n: int) -> bool:
    n = str(n)
    for i in range(1, len(n)):
        if len(n) % i != 0:
            continue
        chunk = n[:i]
        if n == chunk * (len(n) // i):
            return True
    else:
        return False


def find_invalids(start: int, stop: int, part2: bool = False) -> list[int]:
    invalids = []
    for n in range(start, stop + 1):
        if not part2 and is_invalid(n):
            invalids.append(n)
        elif part2 and is_invalid_p2(n):
            invalids.append(n)
    return invalids


def solve_puzzle(puzzle_input, part2=False):
    sum_of_invalids = 0
    for product_id_range in puzzle_input.split(","):
        start, stop = product_id_range.split("-")
        invalids = find_invalids(int(start), int(stop), part2=part2)
        sum_of_invalids += sum(invalids)
    return sum_of_invalids


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

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
