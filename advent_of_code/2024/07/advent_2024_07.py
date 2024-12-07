from collections import deque


def solve_layer(target, values: deque, cur_number=None, concat=False):
    if len(values) == 0 and cur_number == target:
        return True
    if len(values) == 0:
        return False

    results = []
    if cur_number is None:
        cur_number = values.popleft()

    n1 = values.popleft()

    results.append(solve_layer(target, values.copy(), cur_number=cur_number + n1, concat=concat))

    results.append(solve_layer(target, values.copy(), cur_number=cur_number * n1, concat=concat))

    if concat:
        results.append(
            solve_layer(target, values.copy(), cur_number=int(f"{cur_number}{n1}"), concat=concat)
        )

    return any(results)


def solve_puzzle(puzzle_input: str, concat=False) -> int:
    total = 0

    lines = puzzle_input.splitlines()
    for line in lines:
        if line:
            target_number, values = line.strip().split(":")
            target_number = int(target_number)
            values = deque([int(value) for value in values.split()])
            if solve_layer(target=target_number, values=values, concat=concat):
                total += target_number

    return total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_07_input.txt") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    part_b = solve_puzzle(puzzle_input, concat=True)
    print(part_b)

    submit(part_a, part="a")
    submit(part_b, part="b")
