from day12 import (
    process_elev_map,
    process_elev_map_v2,
    find_index,
    get_candidate_neighbors,
    traverse_path,
    transform_elev_map,
)
import pytest
import os

SUPER_SIMPLE_MAP = [["S", "a"], ["a", "E"], ["b", "c"]]

EXAMPLE_ELEV_MAP = []
with open(
    os.path.join(os.path.dirname(__file__), "test_day12_input.txt"), "r"
) as infile:
    rows = [line.strip() for line in infile]
    for row in rows:
        EXAMPLE_ELEV_MAP.append([char for char in row])


def test_transform_elev_map():
    expected = [[0, 0], [0, 2], [1, 2]]

    assert transform_elev_map(SUPER_SIMPLE_MAP) == expected


def test_find_index():
    assert find_index(EXAMPLE_ELEV_MAP, "S") == (0, 0)


def test_get_candidate_neighbors():
    height_map = transform_elev_map(EXAMPLE_ELEV_MAP)
    current_idx = (4, 1)
    expected_neighbors = [(4, 0), (3, 1)]

    actual = get_candidate_neighbors(
        elev_map=height_map, current_idx=current_idx, visited=[]
    )

    assert set(actual) == set(expected_neighbors)


@pytest.mark.parametrize(
    "elev_map,possible_paths",
    [
        (SUPER_SIMPLE_MAP, [[(0, 0), (1, 0), (2, 0), (2, 1), (1, 1)]]),
        (
            [["S", "a"], ["a", "E"]],
            [[(0, 0), (0, 1), (1, 1)], [(0, 0), (1, 0), (1, 1)]],
        ),
    ],
)
def test_traverse_paths(elev_map, possible_paths):
    height_map = transform_elev_map(elev_map)

    actual_path = traverse_path(
        elev_map=height_map, starting_index=(0, 0), goal_index=(1, 1)
    ).result()

    assert actual_path in possible_paths


def test_process_simple_map():
    assert process_elev_map(SUPER_SIMPLE_MAP) == 4


def test_process_example_map():
    assert process_elev_map(EXAMPLE_ELEV_MAP) == 31


def test_process_example_map_v2():
    assert process_elev_map_v2(EXAMPLE_ELEV_MAP)[0] == 29
