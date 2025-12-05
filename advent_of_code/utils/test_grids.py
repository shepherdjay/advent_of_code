from advent_of_code.utils.grids import parse_grid, get_neighbors, get_inbounds_neighbors


def test_parse_grid():
    grid_str = """..@\n..@"""

    grid = parse_grid(grid_str)

    assert grid == [[".", ".", "@"], [".", ".", "@"]]


def test_get_neighbors():
    origin = (0, 0)
    neighbors = get_neighbors(origin)
    assert neighbors == [(-1, 0), (1, 0), (0, -1), (0, 1)]


def test_get_neighbors_inbounds():
    origin = (0, 0)
    neighbors = get_inbounds_neighbors(origin, grid_width=3, grid_height=3)
    assert neighbors == [(1, 0), (0, 1)]
