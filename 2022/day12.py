from typing import List, Tuple
from string import ascii_letters
from copy import deepcopy

Elev = List[List[str]]

def find_index(elev_map: Elev, search: str) -> Tuple[int, int]:
    for row_idx, row  in enumerate(elev_map):
        for col_idx, char in enumerate(row):
            if char == search:
                return row_idx, col_idx

def get_candidate_neighbors(elev_map: Elev, current_idx):
    row_idx, col_idx = current_idx
    
    up_idx = row_idx - 1, col_idx
    down_idx = row_idx + 1, col_idx
    left_idx = row_idx, col_idx - 1
    right_idx = row_idx, col_idx + 1

    neighbor_indexes = [(a, b) for (a, b) in [up_idx, down_idx, left_idx, right_idx] if a >= 0 and a < len(elev_map[0]) and b >= 0 and b < len(elev_map[0])]

    cur_char_value = ascii_letters.find(elev_map[row_idx][col_idx])
    candidates = []
    for neighbor in neighbor_indexes:
        neigh_row_idx, neigh_col_idx = neighbor
        if elev_map[neigh_row_idx][neigh_col_idx].islower():
            neigh_char_value = ascii_letters.find(elev_map[neigh_row_idx][neigh_col_idx])
            if neigh_char_value <= cur_char_value + 1:
                candidates.append(neighbor)

    return candidates


def traverse_path(elev_map, starting_index, goal_index, visited=None) -> List[Tuple[int, int]]:
    if visited is None:
        visited = [starting_index]
    else:
        visited = deepcopy(visited)

    neighbors = [x for x in get_candidate_neighbors(elev_map, starting_index) if x not in visited]

    for neighbor in neighbors:
        neigh_row_idx, neigh_col_idx = neighbor
        if elev_map[neigh_row_idx][neigh_col_idx] == goal_index:
            visited.append(neighbor)
            return visited
        else:
            return traverse_path(elev_map, neighbor, goal_index, visited=visited)

    


def process_elev_map(elev_map: Elev):
    starting_index = find_index(elev_map, 'S')
    ending_index = find_index(elev_map, 'E')