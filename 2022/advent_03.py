import string

LETTERS = string.ascii_letters



def process_rucksack(rucksack):
    """
    >>> process_rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    16
    >>> process_rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    38
    """

    middle_index = len(rucksack)//2

    first_half = rucksack[:middle_index]
    second_half = rucksack[middle_index:]

    for char in first_half:
        if char in second_half:
            return LETTERS.index(char) + 1

def find_badge(group):
    a, b, c = group
    for char in a:
        if char in b and char in c:
            return char

def chunk(l, n=3):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':
    with open('input.txt', 'r') as infile:
        rucksacks = [line.strip() for line in infile]

    print(sum(process_rucksack(rucksack) for rucksack in rucksacks))

    groups = [x for x in chunk(rucksacks)]

    priorities = []
    for group in groups:
        priorities.append(LETTERS.index(find_badge(group)) + 1)

    print(sum(priorities))