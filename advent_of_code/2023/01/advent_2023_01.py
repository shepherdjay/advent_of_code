import re

NUMBERED_WORDS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def parse_line(line):
    """
    >>> parse_line('123')
    13
    """
    first = False
    for char in line:
        if char.isnumeric() and first is False:
            first_num = char
            last_num = char
            first = True
        elif char.isnumeric():
            last_num = char

    return int(f'{first_num}{last_num}')


def parse_line_v2(line):
    """
    >>> parse_line_v2('aone23')
    13
    """
    index_map = {}

    re_number_words = [re.compile(word) for word in NUMBERED_WORDS.keys()]
    for regex in re_number_words:
        for match in regex.finditer(line):
            index_map[match.start()] = NUMBERED_WORDS[match.group()]

    re_numbers = [re.compile(word) for word in NUMBERED_WORDS.values()]
    for regex in re_numbers:
        for match in regex.finditer(line):
            index_map[match.start()] = match.group()

    first, last = index_map[min(index_map.keys())], index_map[max(index_map.keys())]
    return int(f'{first}{last}')


def parse_string(string, part2=False):
    lines = string.split()

    if part2 is False:
        return sum([parse_line(line) for line in lines])
    return sum([parse_line_v2(line) for line in lines])


if __name__ == '__main__':
    test_string = """
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    """
    print(parse_string(test_string))

    test_string_v2 = """
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    """

    print(parse_string(test_string_v2, part2=True))

    with open('advent_01_input.txt', 'r') as infile:
        data = infile.read()
        print(parse_string(data))
        print(parse_string(data, part2=True))
