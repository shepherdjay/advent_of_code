from collections import deque
from functools import cache


def solve_layer(
    target: int, queue: deque, cur_number: int | None = None, concat: bool = False
) -> bool:
    @cache
    def helper(target, queue_tuple, cur_number, concat):
        # Base case: if the queue is empty
        if not queue_tuple:
            return cur_number == target

        queue = deque(queue_tuple)  # Convert back to deque for processing
        n1 = queue.popleft()

        # ADD
        if helper(target, tuple(queue), cur_number + n1, concat):
            return True

        # MULTIPLY
        if helper(target, tuple(queue), cur_number * n1, concat):
            return True

        # CONCAT
        if concat:
            concatenated = int(f"{cur_number}{n1}")
            if helper(target, tuple(queue), concatenated, concat):
                return True

        return False

    # Convert queue to tuple for hashing and call the helper
    if cur_number is None:
        cur_number = queue.popleft()
    return helper(target, tuple(queue), cur_number, concat)


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
