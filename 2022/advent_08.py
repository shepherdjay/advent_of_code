from typing import List, Tuple, Dict


def extract_neighbors(forest_map: List[List[int]], coordinates: Tuple[int, int]) -> Dict[str, List[int]]:
    neighbors = {
        "left": [],
        "right": [],
        "up": [],
        "down": []
    }
    x, y = coordinates
    for row_index, row in enumerate(forest_map):
        for col_index, value in enumerate(row):
            if row_index == x and col_index == y:
                pass
            elif row_index == x and col_index < y:
                neighbors["left"].append(value)
            elif row_index == x and col_index > y:
                neighbors["right"].append(value)
            elif row_index < x and col_index == y:
                neighbors["up"].append(value)
            elif row_index > x and col_index == y:
                neighbors["down"].append(value)
    return neighbors


def is_visible(height, neighbor_map):
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


def find_visible_trees(forest_map: List[List[int]]) -> List[Tuple]:
    """
    Given a 2-dimensional array, find all 'visible' points on that array and return as a list of (x,y) Tuples
    A point is visible if there are no higher values in its row and column, including no other points.
    """
    visible_int_points = []

    for row_index, row in enumerate(forest_map):
        for col_index, value in enumerate(row):
            point_coord = (row_index, col_index)
            neighbors = extract_neighbors(forest_map, point_coord)
            if is_visible(value, neighbors):
                visible_int_points.append(point_coord)

    print(visible_int_points)
    return visible_int_points

if __name__ == '__main__':
    with open('day_08_input.txt', 'r') as elf_file:
        array = []
        for line in elf_file:
            new_row = [int(char) for char in line.strip()]
            array.append(new_row)

    visible_trees = find_visible_trees(forest_map=array)
    print(len(visible_trees))
