from itertools import product

SEARCH_WORD = 'XMAS'

def get_neighbor_coord(row, col):
    possibilities = set()
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            possibilities.add((r,c))
    possibilities.remove((row,col))

    return possibilities

def get_neighbors(coord: tuple[int, int], grid: list[list[str]]):
    max_row = len(grid)
    max_col = len(grid[0])

    neighbors_coord = get_neighbor_coord(*coord)

    neighbors = set()
    for row, col in neighbors_coord:
        if 0 > row or row >= max_row:
            continue
        if 0 > col or col >= max_col:
            continue
        neighbor = grid[row][col]
        neighbors.add(
            (neighbor,(row,col))
        )
    return neighbors

def search(initial_coord: tuple[int,int], grid: list[list[str]], word='XMAS') -> bool:
    try:
        target_letter = word[1]
    except IndexError: #hit the end
        return 1
    
    neighbors = get_neighbors(coord=initial_coord, grid=grid)
    candidates = []

    for char, char_coord in neighbors:
        if char == target_letter:
            candidates.append(char_coord)
    if not candidates:
        return 0
    else:
        return sum(
            [search(initial_coord=coord, grid=grid, word=word[1::]) for coord in candidates]
        )


def solve_puzzle(puzzle_str: str) -> int:
    grid = [row for row in puzzle_str.split('\n') if row]

    successes = 0
    for r_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == 'X':
                successes += search((r_index,col_index), grid=grid)

    return successes