from collections import defaultdict


def split_input(puzzle_input: str) -> tuple[dict[int : list[int]], list[list[int]]]:
    rules = defaultdict(list)
    pages_to_produce = []

    for line in puzzle_input.splitlines():
        rules_string = line.split("|")
        page_string = line.split(",")

        if len(rules_string) == 2:
            print(rules_string)
            page, before = [int(x) for x in line.split("|")]
            rules[page].append(before)
        if len(page_string) > 2:
            pages_to_produce.append([int(x) for x in line.split(",")])
    return rules, pages_to_produce


def solve_puzzle(puzzle_input):
    pass


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_04_input.txt", "r") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)
    # part_b = solve_puzzle(puzzle_input)
    # print(part_b)

    submit(part_a, part="a")
    # submit(part_b, part='b')
