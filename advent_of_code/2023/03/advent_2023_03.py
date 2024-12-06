from typing import Tuple
import re


def extract_numbers_start_end(row_string: str) -> list[tuple[int, int, int]]:
    number_re = re.compile(r'\d+')

    values = []
    for match in number_re.finditer(row_string):
        values.append((int(match.group()), match.start(), match.end()))
    return values


def find_neighbors(coord: Tuple) -> set[Tuple]:
    neighbors = set()
    row_orig, col_orig = coord
    for row in range(row_orig - 1, row_orig + 2):
        for col in range(col_orig - 1, col_orig + 2):
            neighbors.add((row, col))
    neighbors.remove(coord)
    return neighbors


def process_schematic(schematic: list[str]) -> int:
    part_coord_set = set()

    all_values = []
    for row_id, row in enumerate(schematic):
        all_values.append(extract_numbers_start_end(row))
        for col_id, char in enumerate(row):
            if char.isdigit() or char == '.':
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


def process_gears(schematic: list[str]) -> int:
    all_values = []
    for row_id, row in enumerate(schematic):
        all_values.append(extract_numbers_start_end(row))

    total = 0
    for row_id, row in enumerate(schematic):
        for col_id, char in enumerate(row):
            if char == '*':
                star_neighbors = find_neighbors((row_id, col_id))
                count = 0
                gear_one = 0
                gear_two = 0
                for val_row_id, values in enumerate(all_values):
                    for value, start_pos, end_pos in values:
                        for val_col_id in range(start_pos, end_pos):
                            if (val_row_id, val_col_id) in star_neighbors:
                                count += 1
                                if gear_one == 0:
                                    gear_one += value
                                else:
                                    gear_two += value
                                break
                if count == 2:
                    total += gear_one * gear_two
    return total


if __name__ == '__main__':  # pragma: no cover
    with open('advent_2023_03_input.txt', 'r') as infile:
        schematic = infile.read().splitlines()
    print(process_schematic(schematic))
    print(process_gears(schematic))
