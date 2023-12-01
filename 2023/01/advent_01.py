

def parse_line(line):
    first = False
    for char in line:
        if char.isnumeric() and first is False:
            first_num = char
            last_num = char
            first = True
        elif char.isnumeric():
            last_num = char

    return int(f"{first_num}{last_num}")


def parse_string(string):
    lines = string.split()

    return sum([parse_line(line) for line in lines])

if __name__ == '__main__':
    test_string = '''
    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    '''
    print(parse_string(test_string))

    with open('advent_01_input.txt', 'r') as infile:
        print(parse_string(infile.read()))
