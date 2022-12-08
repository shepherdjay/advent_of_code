from typing import List, Tuple

def extract_neighbors(forest_map: List[List[int]], coordinates: Tuple[int, int]) -> List[int]:
    """
    >>> forest_map = [
    ...    [3, 0, 3, 7, 3],
    ...    [2, 5, 5, 1, 2],
    ...    [6, 5, 3, 3, 2],
    ...    [3, 3, 5, 4, 9],
    ...    [3, 5, 3, 9, 0]]
    >>> extract_neighbors(forest_map, (0, 1))
    [3, 0, 3, 7, 3, 5, 5, 3, 5]
    """
    neighbors = []
    x, y = coordinates
    for row_index, row in enumerate(forest_map):
        for col_index, value in enumerate(row):
            if row_index == x or col_index == y:
                neighbors.append(value)

    return neighbors


def find_visible_trees(forest_map: List[List[int]]) -> List[Tuple]:
    """
    Given a 2-dimensional array, find all 'visible' points on that array and return as a list of (x,y) Tuples
    A point is visible if there are no higher values in its row or column, including no other points.
    >>> forest_map = [
    ...    [3, 0, 3, 7, 3],
    ...    [2, 5, 5, 1, 2],
    ...    [6, 5, 3, 3, 2],
    ...    [3, 3, 5, 4, 9],
    ...    [3, 5, 3, 9, 0]]
    >>> len(find_visible_trees(forest_map))
    21
    """
    visible_int_points = []

    for row_index, row in enumerate(forest_map):
        for col_index, value in enumerate(row):
            point_coord = (row_index, col_index)
            neighbors = extract_neighbors(forest_map, point_coord)
            for neighbor in neighbors:
                if neighbor > value:
                    break
            else:
                visible_int_points.append(point_coord)

    exterior_len = len(forest_map) * len(forest_map[0])

    return visible_int_points + exterior_len


