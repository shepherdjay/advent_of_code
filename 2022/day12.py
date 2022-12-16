from typing import List, Tuple
from string import ascii_letters
from copy import deepcopy
import itertools

Elev = List[List[str]]
HeightMap = List[List[int]]


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


def get_candidate_neighbors(elev_map: HeightMap, current_idx, visited):
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

    return candidates


def flatten_paths(super_nests):
    items = []

    for x in super_nests:
        if isinstance(x, list):
            items.extend(flatten_paths(x))
        else:
            items.append(x)

    return items


def traverse_path(elev_map, starting_index, goal_index) -> List:
    stack = [(starting_index, [starting_index])]
    min_path = None

    while stack:
        current_index, path = stack.pop()
        if current_index == goal_index:
            if not min_path or len(path) < len(min_path):
                min_path = path
        else:
            neighbors = get_candidate_neighbors(elev_map, current_index, path)
            for neighbor in neighbors:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

    return min_path


def process_elev_map(elev_map: Elev):
    starting_index = find_index(elev_map, 'S')
    ending_index = find_index(elev_map, 'E')

    height_map = transform_elev_map(elev_map)

    paths = traverse_path(height_map, starting_index=starting_index, goal_index=ending_index)
    paths = flatten_paths(paths)

    unflatten = []
    for k, g in itertools.groupby(paths, lambda x: x == ending_index):
        if not k:
            g_list = list(g)
            g_list.append(ending_index)
            unflatten.append(g_list)

    by_length = sorted(unflatten, key=len)
    print(by_length[0])
    return len(by_length[0]) - 1


if __name__ == '__main__':
    problem_input = []
    with open('day12_input.txt', 'r') as infile:
        rows = [line.strip() for line in infile]
        for row in rows:
            problem_input.append([char for char in row])

    # part1
    num_of_steps = process_elev_map(problem_input)
    print(num_of_steps)
