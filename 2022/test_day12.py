from day12 import process_elev_map, find_index, get_candidate_neighbors, traverse_path, transform_elev_map
import pytest

SUPER_SIMPLE_MAP = [
    ['S', 'a'],
    ['a', 'E'],
    ['b', 'c']
]

EXAMPLE_ELEV_MAP = []
with open('test_day12_input.txt', 'r') as infile:
    rows = [line.strip() for line in infile]
    for row in rows:
        EXAMPLE_ELEV_MAP.append([char for char in row])

def test_transform_elev_map():
    expected = [
        [0, 0],
        [0, 2],
        [1, 2]
    ]

    assert transform_elev_map(SUPER_SIMPLE_MAP) == expected


def test_find_index():
    assert find_index(EXAMPLE_ELEV_MAP, 'S') == (0, 0)


def test_get_candidate_neighbors():
    height_map = transform_elev_map(EXAMPLE_ELEV_MAP)
    current_idx = (2, 1)
    expected_neighbors = [(1, 1), (3, 1), (2, 0), (2, 2)]

    actual = get_candidate_neighbors(elev_map=height_map, current_idx=current_idx, visited=[])

    assert set(actual) == set(expected_neighbors)


def test_traverse_paths():
    super_simple = transform_elev_map(SUPER_SIMPLE_MAP)

    expected_paths = [
        [(0, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (1, 1)],
    ]

    actual_paths = traverse_path(elev_map=super_simple, starting_index=(0, 0), goal_index=(1, 1))

    for path in expected_paths:
        assert path in actual_paths

def test_process_simple_map():
    assert process_elev_map(SUPER_SIMPLE_MAP) == 4

def test_process_example_map():
    assert process_elev_map(EXAMPLE_ELEV_MAP) == 31