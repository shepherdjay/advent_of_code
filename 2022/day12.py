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

    cur_char_value = ascii_letters.find(elev_map[row_idx][col_idx])
    candidates = []
    for neighbor in neighbor_indexes:
        neigh_row_idx, neigh_col_idx = neighbor
        if elev_map[neigh_row_idx][neigh_col_idx] == 'S' or elev_map[neigh_row_idx][neigh_col_idx] == 'E': # we need to make sure to always include these neighbors
            candidates.append(neighbor)
        else:
            neigh_char_value = ascii_letters.find(elev_map[neigh_row_idx][neigh_col_idx])
            if neigh_char_value <= cur_char_value + 1:
                candidates.append(neighbor)

    return candidates

def flatten_to_lists(super_nested):
    pass



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
    by_length = sorted(paths, key=len)

    return len(by_length[0]) - 1
