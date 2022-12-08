import pytest

from advent_08 import extract_neighbors, is_visible, find_visible_trees, scenic_score, score_every_tree

EXAMPLE_FOREST_MAP = [[3, 0, 3, 7, 3],
                      [2, 5, 5, 1, 2],
                      [6, 5, 3, 3, 2],
                      [3, 3, 5, 4, 9],
                      [3, 5, 3, 9, 0]]


def test_extract_neighbors():
    expected = {'left': [5, 6], 'right': [3, 2], 'up': [5, 3], 'down': [5, 3]}

    assert extract_neighbors(EXAMPLE_FOREST_MAP, (2, 2)) == expected


@pytest.mark.parametrize('value,neighbors,expected_result', [
    (5, {"up": [7], "down": [3], "left": [10], "right": [20]}, True),
    (0, {"up": [7], "down": [], "left": [10], "right": [20]}, True),
    (3, {"up": [7], "down": [5], "left": [10], "right": [20]}, False)
])
def test_is_visible(value, neighbors, expected_result):
    assert is_visible(height=value, neighbor_map=neighbors) == expected_result

def test_find_visible_trees():
    assert len(find_visible_trees(EXAMPLE_FOREST_MAP)) == 21

@pytest.mark.parametrize('height,neighbors,expected_result', [
    (5, {"up": [3], "down": [3, 5, 3], "left": [5, 2], "right": [1, 2]}, 4)
])
def test_scenic_score(height, neighbors, expected_result):
    assert scenic_score(height, neighbors) == expected_result

def test_score_every_tree():
    assert max(score_every_tree(EXAMPLE_FOREST_MAP)) == 8