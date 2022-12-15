from day12 import process_elev_map, find_index, get_candidate_neighbors, traverse_path


EXAMPLE_ELEV_MAP = []
with open('test_day12_input.txt', 'r') as infile:
    rows = [line.strip() for line in infile]
    for row in rows:
        EXAMPLE_ELEV_MAP.append([char for char in row])


def test_find_index():
    assert find_index(EXAMPLE_ELEV_MAP, 'S') == (0,0)

def test_process_file():
    assert process_elev_map(EXAMPLE_ELEV_MAP)

def test_get_candidate_neighbors():
    elev_map = EXAMPLE_ELEV_MAP
    current_idx = (2, 1)
    expected_neighbors = [(2, 0), (1, 1 ), (3,1), (2,2)]

    actual = get_candidate_neighbors(elev_map=elev_map, current_idx=current_idx)

    assert set(actual) == set(expected_neighbors)

def test_traverse_paths():
    super_simple = [
        ['S', 'a'],
        ['a', 'E']
    ]

    expected_paths = [
        [(0,0), (0, 1), (1, 1)],
        [(0,0), (1, 0), (1, 1)]
    ]

    assert traverse_path(elev_map=super_simple, starting_index=(0,0), goal_index=(1,1)) == expected_paths
