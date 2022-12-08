from typing import List, Tuple, Dict
import numpy as np
import math


def extract_neighbors(forest_map: np.ndarray, coordinates: Tuple[int, int]) -> Dict[str, List[int]]:
    neighbors = {
        "left": [],
        "right": [],
        "up": [],
        "down": []
    }
    x, y = coordinates
    # Extract the neighbors in the same row as the current element
    for col_index, value in enumerate(forest_map[x]):
        if col_index == y:
            pass
        elif col_index < y:
            neighbors["left"].insert(0, value)
        elif col_index > y:
            neighbors["right"].append(value)

    # Extract the neighbors in the same column as the current element
    for row_index, row in enumerate(forest_map):
        value = row[y]
        if row_index == x:
            pass
        elif row_index < x:
            neighbors["up"].insert(0, value)
        elif row_index > x:
            neighbors["down"].append(value)
    return neighbors


def is_visible(height: int, neighbor_map: dict):
    """
    Given a height x, and a neighbor map "up, "down, "left", "right" return True if all values of a key are < x
    An empty list is considered 0
    """
    for direction, neighbors in neighbor_map.items():
        if len(neighbors) == 0:
            neighbor_map[direction] = [float('-inf')]

    visible_results = [
        all(x < height for x in neighbor_map["left"]),
        all(x < height for x in neighbor_map["right"]),
        all(x < height for x in neighbor_map["up"]),
        all(x < height for x in neighbor_map["down"]),
    ]
    if any(visible_results):
        return True
    return False


def scenic_score(height: int, neighbor_map: dict) -> int:
    tree_counts = []
    for direction, neighbors in neighbor_map.items():
        trees_visible = 0
        for neighbor in neighbors:
            if neighbor < height:
                trees_visible += 1
            if neighbor >= height:
                trees_visible += 1
                break
        tree_counts.append(trees_visible)

    return math.prod(tree_counts)


def find_visible_trees(forest_map: np.ndarray) -> List[Tuple]:
    """
    Given a 2-dimensional array, find all 'visible' points on that array and return as a list of (x,y) elements
    A point is visible if there are no higher values in its row and column, including no other points.
    """
    visible_int_points = []

    for row_index, row in enumerate(forest_map):
        for col_index, height in enumerate(row):
            point_coord = (row_index, col_index)
            neighbors = extract_neighbors(forest_map, point_coord)
            if is_visible(height, neighbors):
                visible_int_points.append(point_coord)

    return visible_int_points

def score_every_tree(forest_map: np.ndarray) -> List[int]:
    scores = []

    for row_index, row in enumerate(forest_map):
        for col_index, height in enumerate(row):
            point_coord = (row_index, col_index)
            neighbors = extract_neighbors(forest_map, point_coord)

            scores.append(scenic_score(height, neighbors))

    return scores

if __name__ == '__main__':
    with open('day_08_input.txt', 'r') as elf_file:
        array = []
        for line in elf_file:
            new_row = [int(char) for char in line.strip()]
            array.append(new_row)

    forest_map = np.array(array)

    visible_trees = find_visible_trees(forest_map=forest_map)
    print(len(visible_trees))

    print(max(score_every_tree(forest_map=forest_map)))
