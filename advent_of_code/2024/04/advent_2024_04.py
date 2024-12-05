def get_neighbor_coord(row, col):
    possibilities = set()
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            possibilities.add((r, c))
    possibilities.remove((row, col))

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
        neighbors.add((neighbor, (row, col)))
    return neighbors


def get_paths(coord: tuple[int, int], path_length: int) -> list[list[tuple[int, int]]]:
    row, col = coord

    left = [(i, col) for i in range(row + 1 - path_length, row + 1)][::-1]
    right = [(i, col) for i in range(row, row + path_length)]
    up = [(row, i) for i in range(col + 1 - path_length, col + 1)][::-1]
    down = [(row, i) for i in range(col, col + path_length)]

    leftup = [(coord[0], up[i][1]) for i, coord in enumerate(left)]
    rightup = [(coord[0], up[i][1]) for i, coord in enumerate(right)]
    leftdown = [(coord[0], down[i][1]) for i, coord in enumerate(left)]
    rightdown = [(coord[0], down[i][1]) for i, coord in enumerate(right)]

    return [left, leftup, up, rightup, right, rightdown, down, leftdown]


def on_grid(path: list[tuple[int, int]], grid_length) -> bool:
    for row, col in path:
        if 0 > row or row > grid_length:
            return False
        if 0 > col or col > grid_length:
            return False
    return True


def search(coord, target_word, grid):
    available_paths = get_paths(coord=coord, path_length=len(target_word))

    results = 0

    for path in available_paths:
        if on_grid(path, grid_length=len(grid)):
            try:
                word = "".join([grid[row][col] for row, col in path])
                if word == target_word:
                    results += 1
            except IndexError:
                pass
    return results


def solve_puzzle(puzzle_str: str) -> int:
    grid = [row for row in puzzle_str.split("\n") if row]

    target_word = "XMAS"
    successes = 0
    for r_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == target_word[0]:
                result = search(
                    (r_index, col_index), grid=grid, target_word=target_word
                )
                successes += result

    return successes


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_04_input.txt", "r") as infile:
        puzzle_input = infile.read()

    submit(solve_puzzle(puzzle_input))
