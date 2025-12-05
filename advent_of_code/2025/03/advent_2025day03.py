from pathlib import Path

BASEPATH = Path(__file__).parent.resolve()


def get_next_largest_digit(battery_bank: str, num_of_characters: int):
    left_idx = 0
    while True:
        possible_chars = battery_bank[left_idx : len(battery_bank) - num_of_characters + 1]
        largest_char = max(possible_chars, key=int)
        yield largest_char
        left_idx += possible_chars.index(largest_char) + 1
        num_of_characters -= 1
        if num_of_characters <= 0:
            break


def find_largest_joltage(battery_bank: str, banks_to_turn_on: int = 2) -> int:
    batteries = [
        char for char in get_next_largest_digit(battery_bank, num_of_characters=banks_to_turn_on)
    ]
    return int("".join(batteries))


def solve_puzzle(puzzle_input, part2=False):
    if part2:
        return sum(
            find_largest_joltage(battery_bank, banks_to_turn_on=12)
            for battery_bank in puzzle_input.splitlines()
        )
    return sum(find_largest_joltage(battery_bank) for battery_bank in puzzle_input.splitlines())


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
