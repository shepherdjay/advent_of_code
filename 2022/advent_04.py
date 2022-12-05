from typing import List


def range_section(sections: str) -> range:
    integers = [int(_) for _ in sections.split('-')]
    min, max = integers
    return range(min, max + 1)


def check_fully_contained(single_pair: List[str]) -> bool:
    a, b = single_pair
    a_range = range_section(a)
    b_range = range_section(b)

    for section in a_range:
        if section in b_range:
            continue
        else:
            break
    else:
        return True

    for section in b_range:
        if section in a_range:
            continue
        else:
            break
    else:
        return True

    return False


def find_overlaps(pairs_list: List[List]) -> int:
    overlaps = 0
    for single_pair in pairs_list:
        if check_fully_contained(single_pair):
            overlaps += 1
    return overlaps


if __name__ == '__main__':
    with open('advent_04_input.txt', 'r') as infile:
        pairs = [line.strip().split(',') for line in infile]
    print(find_overlaps(pairs))
