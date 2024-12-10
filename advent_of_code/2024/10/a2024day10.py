from pathlib import Path

BASEPATH = Path(__file__).parent.resolve()

def create_grid(grid_str: str) -> list[list[int]]:
    grid = []
    for line in grid_str.splitlines():
        row = list()
        for char in line:
            if char.isdigit():
                row.append(int(char))
            else:
                row.append(-1)
        grid.append(row)
    return grid

def get_neighbors(origin):
    row, col = origin
    up = row - 1, col
    down = row + 1, col
    left = row, col - 1
    right = row, col + 1
    return [up, down, left, right]


def calculate_path(origin: tuple, grid: list[list[int]]) -> int:
    neighbors = get_neighbors(origin)
    canidates = []
    total_found = 0
    for neighbor in neighbors:
        row, col = neighbor
        if row < 0 or row >= len(grid):
            continue
        if col < 0 or col >= len(grid[0]):
            continue
        if grid[row][col] == 9:
            total_found += 1
        elif grid[row][col] == grid[origin[0]][origin[1]] + 1:
            canidates.append(neighbor)
    
    return total_found + sum([calculate_path(neighbor, grid) for neighbor in canidates])

def solve_puzzle(puzzle_input, part2=False):
    grid = create_grid(puzzle_input)

    ultimate_total = 0
    for r_idx, row in enumerate(grid):
        for c_idx, value in enumerate(row):
            if value == 0:
                ultimate_total += calculate_path((r_idx, c_idx), grid)
    return ultimate_total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        grid_str = infile.read().strip("\n")

    part_a = solve_puzzle(grid_str)
    print(part_a)

    part_b = solve_puzzle(grid_str, part2=True)
    print(part_b)

    try:
        submit(part_a, part="a")
        submit(part_b, part="b")
    except AocdError as e:
        pass
