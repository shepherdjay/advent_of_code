from collections import defaultdict
import random
import functools


def split_input(puzzle_input: str) -> tuple[dict[int : list[int]], list[list[int]]]:
    rules = defaultdict(list)
    pages_to_produce = []

    for line in puzzle_input.splitlines():
        rules_string = line.split("|")
        page_string = line.split(",")

        if len(rules_string) == 2:
            page, before = [int(x) for x in line.split("|")]
            rules[page].append(before)
        if len(page_string) > 2:
            pages_to_produce.append([int(x) for x in line.split(",")])
    return rules, pages_to_produce


def check_printjob(printjob: list[int], rules: dict[int : list[int]]):
    checked_values = []

    for value in printjob:
        value_rules = rules.get(value, list())
        for following_page in value_rules:
            if following_page in checked_values:
                return False
        checked_values.append(value)

    return True


def rulesort(rules, a, b):
    if a not in rules:
        return 0
    if b in rules[a]:
        return -1
    else:
        return 1


def correct_printjob(printjob: list, rules: dict):
    printjob.sort(key=functools.cmp_to_key(functools.partial(rulesort, rules)))

    return printjob


def solve_puzzle(puzzle_input, partb=False):
    rules, pages_to_produce = split_input(puzzle_input=puzzle_input)

    correct_order = []
    incorrect_order = []

    for printjob in pages_to_produce:
        if check_printjob(printjob, rules):
            correct_order.append(printjob)
        else:
            incorrect_order.append(printjob)

    if partb:
        corrected = [correct_printjob(printjob, rules) for printjob in incorrect_order]
        return sum([pages[(len(pages) - 1) // 2] for pages in corrected])

    return sum([pages[(len(pages) - 1) // 2] for pages in correct_order])


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_05_input.txt", "r") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)
    part_b = solve_puzzle(puzzle_input, partb=True)
    print(part_b)

    submit(part_a, part="a")
    submit(part_b, part="b")
