import re


def uncorrupt_string(corrupted_string: str) -> list[(int, int)]:
    """
    >>> uncorrupt_string("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    [(2, 4), (5, 5), (11, 8), (8, 5)]
    """
    mul_re = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    return [(int(x), int(y)) for x, y in mul_re.findall(corrupted_string)]


def multiply_and_add(corrupted_string):
    """
    >>> multiply_and_add("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    161
    """
    mul_pairs = uncorrupt_string(corrupted_string)

    running_total = 0
    for x, y in mul_pairs:
        running_total += x * y
    return running_total


if __name__ == "__main__":  # pragma: no cover
    with open("advent_2024_03_input.txt", "r") as infile:
        puzzle_string = infile.read()

    print(multiply_and_add(puzzle_string))
