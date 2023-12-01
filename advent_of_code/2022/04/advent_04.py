from typing import List, Tuple


def range_section(sections: str) -> range:
    min, max = map(int, sections.split("-"))
    return range(min, max + 1)


def check_overlaps(single_pair: List[str]) -> bool:
    a, b = single_pair
    a_range = range_section(a)
    b_range = range_section(b)

    for section in a_range:
        if section in b_range:
            return True

    for section in b_range:
        if section in a_range:
            return True

    return False


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


def find_overlaps(pairs_list: List[List]) -> Tuple[int, int]:
    fully_contained = 0
    overlaps = 0
    for single_pair in pairs_list:
        if check_fully_contained(single_pair):
            fully_contained += 1
        if check_overlaps(single_pair):
            overlaps += 1
    return fully_contained, overlaps


if __name__ == "__main__":
    with open("advent_04_input.txt", "r") as infile:
        pairs = [line.strip().split(",") for line in infile]
    print(find_overlaps(pairs))
