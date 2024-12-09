from pathlib import Path

BASEPATH = Path(__file__).parent.resolve()


def solve_puzzle(puzzle_input, part2=False):
    pass

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
        submit(part_a, part="a")
        submit(part_b, part="b")
    except AocdError as e:
        pass