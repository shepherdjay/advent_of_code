import re


def uncorrupt_string(
    corrupted_string: str, enable_parsing: bool = False
) -> list[tuple[int, int] | bool]:
    """
    >>> example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    >>> uncorrupt_string(example)
    [(2, 4), (5, 5), (11, 8), (8, 5)]
    >>> uncorrupt_string(example, enable_parsing=True)
    [(2, 4), (8, 5)]
    """
    mul_re = re.compile(r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)|(do\(\)|don't\(\))")

    enabled = True
    valid_instructions = []
    for x, y, enable_flag in mul_re.findall(corrupted_string):
        if enable_parsing is True:
            if enable_flag == "do()":
                enabled = True
            elif enable_flag == "don't()":
                enabled = False
        if x and enabled:
            valid_instructions.append((int(x), int(y)))

    return valid_instructions


def multiply_and_add(corrupted_string, enable_parsing=False):
    """
    >>> example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    >>> multiply_and_add(example)
    161
    >>> multiply_and_add(example, enable_parsing=True)
    48
    """
    mul_pairs = uncorrupt_string(corrupted_string, enable_parsing)

    running_total = 0
    for x, y in mul_pairs:
        running_total += x * y
    return running_total


if __name__ == "__main__":  # pragma: no cover
    with open("advent_2024_03_input.txt", "r") as infile:
        puzzle_string = infile.read()

    print(multiply_and_add(puzzle_string))
    print(multiply_and_add(puzzle_string, enable_parsing=True))
