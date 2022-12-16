from typing import List, Tuple
from string import ascii_letters
from copy import deepcopy
import itertools

Elev = List[List[str]]


def find_index(elev_map: Elev, search: str) -> Tuple[int, int]:
    for row_idx, row in enumerate(elev_map):
        for col_idx, char in enumerate(row):
            if char == search:
                return row_idx, col_idx


def get_candidate_neighbors(elev_map: Elev, current_idx):
    row_idx, col_idx = current_idx

    up_idx = row_idx - 1, col_idx
    down_idx = row_idx + 1, col_idx
    left_idx = row_idx, col_idx - 1
    right_idx = row_idx, col_idx + 1

    neighbor_indexes = []

    for a, b in [up_idx, down_idx, left_idx, right_idx]:
        if 0 <= a < len(elev_map) and 0 <= b < len(elev_map[0]):
            neighbor_indexes.append((a,b))

    cur_char = elev_map[row_idx][col_idx]
    if cur_char == 'S':
        cur_char_value = 0
    else:
        cur_char_value = ascii_letters.find(cur_char)
    candidates = []
    for neighbor in neighbor_indexes:
        neigh_row_idx, neigh_col_idx = neighbor
        neigh_char = elev_map[neigh_row_idx][neigh_col_idx]
        if neigh_char == 'S':
            neigh_char_value = 0
        elif neigh_char == 'E':
            neigh_char_value = 25
        else:
            neigh_char_value = ascii_letters.find(neigh_char)
        if neigh_char_value in [cur_char_value, cur_char_value - 1, cur_char_value + 1]:
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


def traverse_path(elev_map, starting_index, goal_index, visited=None) -> List[List[Tuple[int, int]]]:
    paths = []
    if visited is None:
        visited = [starting_index]
    else:
        visited = deepcopy(visited)
        visited.append(starting_index)

    neighbors = [x for x in get_candidate_neighbors(elev_map, starting_index) if x not in visited]

    for neighbor in neighbors:
        if neighbor == goal_index:
            visited.append(neighbor)
            return visited
        else:
            paths.append(traverse_path(elev_map, neighbor, goal_index, visited=visited))
    return paths


def process_elev_map(elev_map: Elev):
    starting_index = find_index(elev_map, 'S')
    ending_index = find_index(elev_map, 'E')

    paths = traverse_path(elev_map, starting_index=starting_index, goal_index=ending_index)
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
