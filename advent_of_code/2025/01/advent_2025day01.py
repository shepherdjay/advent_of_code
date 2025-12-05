from pathlib import Path

BASEPATH = Path(__file__).parent.resolve()


def solve_puzzle_part1(puzzle_input):
    combo_value = 50
    modular = 100
    zero_count = 0
    for line in puzzle_input.splitlines():
        direction, amount = line[0], int(line[1::])
        if direction == "L":
            combo_value = (combo_value - amount) % modular
        else:
            combo_value = (combo_value + amount) % modular
        if combo_value == 0:
            zero_count += 1
    return zero_count


def rotate(direction, amount, start_value):
    zero_count = 0
    modular = 100
    combo_value = start_value
    for _ in range(amount):
        if direction == "L":
            combo_value = (combo_value - 1) % modular
        else:
            combo_value = (combo_value + 1) % modular
        if combo_value == 0:
            zero_count += 1
    return zero_count, combo_value


def solve_puzzle(puzzle_input, part2=False):
    if not part2:
        return solve_puzzle_part1(puzzle_input)
    else:
        start_value = 50
        total = 0
        for line in puzzle_input.splitlines():
            zero_count, new_start = rotate(
                direction=line[0], amount=int(line[1::]), start_value=start_value
            )
            total += zero_count
            start_value = new_start
    return total


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
