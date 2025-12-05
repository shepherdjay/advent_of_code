def parse_grid(grid_str):
    grid = []
    for row in grid_str.split("\n"):
        new_row = [char for char in row]
        grid.append(new_row)
    return grid


def get_neighbors(origin, diagonals=False):
    n_row, n_col = origin
    # adjacent neighbors
    up = n_row - 1, n_col
    down = n_row + 1, n_col
    left = n_row, n_col - 1
    right = n_row, n_col + 1
    # diagonal neighbors
    up_left = n_row - 1, n_col - 1
    up_right = n_row - 1, n_col + 1
    down_left = n_row + 1, n_col - 1
    down_right = n_row + 1, n_col + 1

    if diagonals:
        return [up, down, left, right, up_left, up_right, down_left, down_right]
    else:
        return [up, down, left, right]


def get_inbounds_neighbors(origin, grid_width, grid_height, diagonals=False):
    neighbors = get_neighbors(origin, diagonals)
    inbound_neighbors = []
    for neighbor in neighbors:
        n_row, n_col = neighbor
        if 0 <= n_row < grid_width and 0 <= n_col < grid_height:
            inbound_neighbors.append(neighbor)
    return inbound_neighbors
