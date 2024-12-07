from collections import deque


def solve_layer(
    target: int,
    queue: deque,
    cur_number: int | None = None,
    concat: bool = False,
    memo: dict | None = None,
) -> bool:
    if memo is None:
        memo = {}

    # Base cases
    if len(queue) == 0:
        return cur_number == target

    # Use memoization to avoid recalculating the same state
    state = (tuple(queue), cur_number, concat)
    if state in memo:
        return memo[state]

    if cur_number is None:
        cur_number = queue.popleft()

    n1 = queue.popleft()

    # ADD
    if solve_layer(target, queue.copy(), cur_number + n1, concat, memo):
        memo[state] = True
        return True

    # MULTIPLY
    if solve_layer(target, queue.copy(), cur_number * n1, concat, memo):
        memo[state] = True
        return True

    # CONCAT
    if concat:
        concatenated = int(f"{cur_number}{n1}")
        if solve_layer(target, queue.copy(), concatenated, concat, memo):
            memo[state] = True
            return True

    memo[state] = False
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
