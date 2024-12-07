from collections import deque


def solve_layer(
    target: int, queue: deque, cur_number: int | None = None, concat: bool = False
) -> bool:
    if len(queue) == 0 and cur_number == target:
        return True
    if len(queue) == 0:
        return False

    if cur_number is None:
        cur_number = queue.popleft()

    n1 = queue.popleft()

    # ADD
    if solve_layer(target, queue.copy(), cur_number=cur_number + n1, concat=concat):
        return True

    # MULTIPLY
    if solve_layer(target, queue.copy(), cur_number=cur_number * n1, concat=concat):
        return True

    # CONCAT
    if concat:
        if solve_layer(target, queue.copy(), cur_number=int(f"{cur_number}{n1}"), concat=concat):
            return True

    return False


def solve_puzzle(puzzle_input: str, concat=False) -> int:
    total = 0

    lines = puzzle_input.splitlines()
    for line in lines:
        if line:
            target_number, values = line.strip().split(":")
            target_number = int(target_number)
            values = deque([int(value) for value in values.split()])
            if solve_layer(target=target_number, queue=values, concat=concat):
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
