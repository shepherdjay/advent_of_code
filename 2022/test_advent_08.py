import pytest

from advent_08 import extract_neighbors, is_visible, find_visible_trees

EXAMPLE_FOREST_MAP = [[3, 0, 3, 7, 3],
                      [2, 5, 5, 1, 2],
                      [6, 5, 3, 3, 2],
                      [3, 3, 5, 4, 9],
                      [3, 5, 3, 9, 0]]


def test_extract_neighbors():
    expected = {'left': [3], 'right': [3, 7, 3], 'up': [], 'down': [5, 5, 3, 5]}

    assert expected == extract_neighbors(EXAMPLE_FOREST_MAP, (0, 1))


@pytest.mark.parametrize('value,neighbors,expected_result', [
    (5, {"up": [7], "down": [3], "left": [10], "right": [20]}, True),
    (0, {"up": [7], "down": [], "left": [10], "right": [20]}, True),
    (3, {"up": [7], "down": [5], "left": [10], "right": [20]}, False)
])
def test_is_visible(value, neighbors, expected_result):
    assert is_visible(height=value, neighbor_map=neighbors) == expected_result

def test_find_visible_trees():
    assert 21 == len(find_visible_trees(EXAMPLE_FOREST_MAP))