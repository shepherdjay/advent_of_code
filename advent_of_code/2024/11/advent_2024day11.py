from pathlib import Path

BASEPATH = Path(__file__).parent.resolve()

def blink(input_list: list[int]) -> list:
    """
    If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
"""
    new_list = []
    for value in input_list:
        val_len = len(str(value))
        if value == 0:
            new_list.append(1)
        elif val_len % 2 == 0:
            left, right = int(str(value)[0:val_len // 2]),   int(str(value)[val_len // 2::])
            new_list += [left, right]
        else:
            new_list.append(value * 2024)
    return new_list

def solve_puzzle(puzzle_input, part2=False):
    initial = [int(i) for i in puzzle_input.strip().split()]
    blink_count = 25

    if part2:
        blink_count = 75

    for _ in range(blink_count):
        initial = blink(initial)

    return len(initial)

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