from pathlib import Path

BASEPATH = Path(__file__).parent.resolve()


def parse_grid(grid_str):
    grid = []
    for row in grid_str.split('\n'):
        new_row = [char for char in row]
        grid.append(new_row)
    return grid

def get_neighbors(origin):
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
    return [up, down, left, right, up_left, up_right, down_left, down_right]

def get_inbounds_neighbors(origin, grid_width, grid_height):
    neighbors = get_neighbors(origin)
    inbound_neighbors = []
    for neighbor in neighbors:
        n_row, n_col = neighbor
        if 0 <= n_row < grid_width and 0 <= n_col < grid_height:
            inbound_neighbors.append(neighbor)
    return inbound_neighbors

def solve_puzzle_part1(grid):
    count = 0
    removable = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                like_neighbors = 0
                neighbors = get_inbounds_neighbors((i, j), grid_height=len(grid), grid_width=len(grid[0]))
                for neighbor in neighbors:
                    if grid[neighbor[0]][neighbor[1]] == '@':
                        like_neighbors += 1
                if like_neighbors < 4:
                    count += 1
                    removable.append((i, j))
    return count, removable

def solve_puzzle(puzzle_input, part2=False):
    grid = parse_grid(puzzle_input)
    count, removable = solve_puzzle_part1(grid)
    if not part2:
        return count
    else:
        total_count = count
        while count > 0:
            for (i, j) in removable:
                grid[i][j] = '.'
            count, removable = solve_puzzle_part1(grid)
            total_count += count
        return total_count


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip('\n')

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    part_b = solve_puzzle(puzzle_input, part2=True)
    print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        submit(part_b, part="b", session=session)
    except AocdError as e:
        pass