from typing import List, Tuple
from string import ascii_letters
import itertools
from os import system
from colorama import Fore, Back, Style
import math
from collections import deque

Elev = List[List[str]]
HeightMap = List[List[int]]


class Terminal:
    def __init__(self, starting_map):
        self.starting_map = starting_map

    def draw(self, coordinates):
        system('cls')
        print()
        print()
        for row_idx, row in enumerate(self.starting_map):
            for col_idx, char in enumerate(row):
                if (row_idx, col_idx) in coordinates:
                    print(Fore.RED + char, end='')
                else:
                    print(Fore.LIGHTWHITE_EX + char, end='')
            print()
        print()
        print(f'Path Length: {len(coordinates)}')


def find_index(elev_map: Elev, search: str) -> Tuple[int, int]:
    for row_idx, row in enumerate(elev_map):
        for col_idx, char in enumerate(row):
            if char == search:
                return row_idx, col_idx


def transform_elev_map(elev_map: Elev):
    """
    Returns an elevation map with the letters replaced by integer values.
    'S' is set to 0
    'E' is set to the maximum integer of all other characters
    """

    flatten_list = list(itertools.chain.from_iterable(elev_map))
    largest_lower_case_letter = sorted(list(set(flatten_list)), reverse=True)[0]
    e_value = ascii_letters.find(largest_lower_case_letter)

    new_elev_map = []
    for row in elev_map:
        new_row = []
        for char in row:
            match char:
                case 'S':
                    char_value = 0
                case 'E':
                    char_value = e_value
                case other:
                    char_value = ascii_letters.find(char)
            new_row.append(char_value)
        new_elev_map.append(new_row)

    return new_elev_map


def distance_to_goal(coordinate, goal):
    x1, y1 = coordinate
    x2, y2 = goal
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def get_candidate_neighbors(elev_map: HeightMap, current_idx, visited, goal=None):
    row_idx, col_idx = current_idx

    up_idx = row_idx - 1, col_idx
    down_idx = row_idx + 1, col_idx
    left_idx = row_idx, col_idx - 1
    right_idx = row_idx, col_idx + 1

    neighbor_indexes = []

    for a, b in [up_idx, down_idx, left_idx, right_idx]:
        if 0 <= a < len(elev_map) and 0 <= b < len(elev_map[0]):
            neighbor_indexes.append((a, b))

    candidates = []
    cur_value = elev_map[row_idx][col_idx]
    for neighbor in neighbor_indexes:
        if neighbor in visited:
            continue
        neigh_row_idx, neigh_col_idx = neighbor
        neigh_value = elev_map[neigh_row_idx][neigh_col_idx]

        if neigh_value <= cur_value + 1:
            candidates.append(neighbor)

    if goal is not None:
        candidates.sort(key=lambda x: distance_to_goal(x, goal), reverse=True)

    return candidates


def traverse_path(elev_map, starting_index, goal_index, terminal=None) -> List:
    stack = deque()
    stack.append((starting_index, [starting_index]))
    min_path = None
    min_successful_path_length = float('inf')

    while stack:
        current_index, path = stack.pop()
        if terminal:
            terminal.draw(path)
        if len(path) >= min_successful_path_length:
            continue
        if current_index == goal_index:
            print(f'Found a path of length {len(path)}')
            if not min_path or len(path) < len(min_path):
                min_path = path
                min_successful_path_length = len(path)
        else:
            neighbors = get_candidate_neighbors(elev_map, current_index, visited=path, goal=goal_index)
            for neighbor in neighbors:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

    return min_path


def process_elev_map(elev_map: Elev, terminal=None):
    starting_index = find_index(elev_map, 'S')
    ending_index = find_index(elev_map, 'E')

    height_map = transform_elev_map(elev_map)

    path = traverse_path(height_map, starting_index=starting_index, goal_index=ending_index, terminal=terminal)

    return len(path) - 1


if __name__ == '__main__':
    problem_input = []
    with open('day12_input.txt', 'r') as infile:
        rows = [line.strip() for line in infile]
        for row in rows:
            problem_input.append([char for char in row])

    # part1
    terminal = Terminal(problem_input)
    terminal = None
    num_of_steps = process_elev_map(problem_input, terminal=terminal)
    print(num_of_steps)
