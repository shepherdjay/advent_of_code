from pathlib import Path
from collections import deque
from copy import deepcopy

BASEPATH = Path(__file__).parent.resolve()


def create_grid(grid_str: str) -> list[list[int]]:
    grid = []
    for line in grid_str.splitlines():
        n_row = list()
        for char in line:
            if char.isdigit():
                n_row.append(int(char))
            else:
                n_row.append(-1)
        grid.append(n_row)
    return grid


def get_neighbors(origin):
    n_row, n_col = origin
    up = n_row - 1, n_col
    down = n_row + 1, n_col
    left = n_row, n_col - 1
    right = n_row, n_col + 1
    return [up, down, left, right]


def distinct_paths(origin: tuple, grid: list[list[int]]) -> int:
    queue = deque([(origin, [origin])])
    paths = []

    while queue:
        node, path = queue.pop()
        row, col = node
        my_value = grid[row][col]

        if my_value == 9:
            paths.append(path)
            continue

        for neighbor in get_neighbors(node):
            n_row, n_col = neighbor
            if (
                0 <= n_row < len(grid)
                and 0 <= n_col < len(grid[0])
                and neighbor not in path
                and grid[n_row][n_col] == my_value + 1
            ):
                queue.append((neighbor, path + [neighbor]))
    return len(paths)


def calculate_path(origin: tuple, grid: list[list[int]], positions=None) -> int:
    neighbors = get_neighbors(origin)
    canidates = []
    my_value = grid[origin[0]][origin[1]]

    if positions is None:
        positions = set()
    for neighbor in neighbors:
        n_row, n_col = neighbor

        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
            n_value = grid[n_row][n_col]
            if n_value == 9 and my_value == 8:
                positions.add((n_row, n_col))
            elif n_value == my_value + 1 and my_value < 8:
                canidates.append(neighbor)

    for canidate in canidates:
        calculate_path(canidate, grid, positions)
    return len(positions)


def solve_puzzle(puzzle_input, part2=False):
    grid = create_grid(puzzle_input)

    ultimate_total = 0
    part2_ultimate_total = 0
    for r_idx, n_row in enumerate(grid):
        for c_idx, value in enumerate(n_row):
            if value == 0:
                ultimate_total += calculate_path((r_idx, c_idx), grid)
                part2_ultimate_total += distinct_paths((r_idx, c_idx), grid)
    return ultimate_total, part2_ultimate_total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        grid_str = infile.read().strip("\n")

    part_a, part_b = solve_puzzle(grid_str)
    print(part_a)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
