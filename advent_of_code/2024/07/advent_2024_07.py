from collections import deque


def solve_layer(target, values: deque, cur_number=0):
    if not values or cur_number > target:
        return False
    n1 = values.popleft()

    add = n1 + cur_number
    multi = n1 * cur_number

    if add == target:
        return True
    elif multi == target:
        return True
    else:
        return any(
            [solve_layer(target, values.copy(), cur_number=operation) for operation in [add, multi]]
        )


def solve_puzzle(puzzle_input: str) -> int:
    total = 0

    lines = puzzle_input.splitlines()
    for line in lines:
        if line:
            target_number, values = line.strip().split(":")
            target_number = int(target_number)
            values = deque([int(value) for value in values.split()])
            if solve_layer(target=target_number, values=values):
                total += target_number

    return total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_07_input.txt") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    submit(part_a, part="a")
