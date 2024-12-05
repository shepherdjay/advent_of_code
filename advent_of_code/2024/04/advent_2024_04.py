from itertools import product

def get_neighbor_coord(row, col):
    left, right = col - 1, col + 1
    up, down = row - 1, row + 1

    return set([
        (row, left),
        (row, right),
        (up, col),
        (down, col)]
    )

def get_neighbors(coord: tuple[int, int], grid: list[list[str]]):
    max_row = len(grid)
    max_col = len(grid[0])

    print(grid)

    neighbors_coord = get_neighbor_coord(*coord)

    neighbors = set()
    for row, col in neighbors_coord:
        neighbor = grid[row][col]
        neighbors.add(
            (neighbor,(row,col))
        )
    return neighbors



def solve_puzzle(puzzle_str: str) -> int:
    pass