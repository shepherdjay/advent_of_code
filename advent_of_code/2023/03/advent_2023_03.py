from typing import Tuple
import re


def extract_numbers_start_end(row_string: str) -> list[tuple[int, int, int]]:
    number_re = re.compile("\d+")

    values = []
    for match in number_re.finditer(row_string):
        values.append((int(match.group()), match.start(), match.end()))
    return values


def find_neighbors(coord: Tuple) -> set[Tuple]:
    neighbors = set()
    row_orig, col_orig = coord
    for row in range(row_orig - 1, row_orig + 2):
        if row < 0:
            continue
        for col in range(col_orig - 1, col_orig + 2):
            if col < 0:
                continue
            neighbors.add((row, col))
    neighbors.remove(coord)
    return neighbors


def process_schematic(schematic: list[str]) -> int:
    part_coord_set = set()

    all_values = []
    for row_id, row in enumerate(schematic):
        all_values.append(extract_numbers_start_end(row))
        for col_id, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue
            char_neighbors = find_neighbors((row_id, col_id))
            part_coord_set.update(char_neighbors)

    total = 0
    for row_id, values in enumerate(all_values):
        for value, start_pos, end_pos in values:
            for col_value in range(start_pos, end_pos):
                if (row_id, col_value) in part_coord_set:
                    total += value
                    break
    return total


if __name__ == "__main__":  # pragma: no cover
    with open("advent_2023_03_input.txt", "r") as infile:
        schematic = infile.readlines()
    print(process_schematic(schematic))
