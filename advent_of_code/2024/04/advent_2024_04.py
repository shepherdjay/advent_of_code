def get_paths(
    coord: tuple[int, int], path_length: int, diagonals_only: bool = False
) -> list[list[tuple[int, int]]]:
    row, col = coord

    left = [(i, col) for i in range(row + 1 - path_length, row + 1)][::-1]
    right = [(i, col) for i in range(row, row + path_length)]
    up = [(row, i) for i in range(col + 1 - path_length, col + 1)][::-1]
    down = [(row, i) for i in range(col, col + path_length)]

    leftup = [(coord[0], up[i][1]) for i, coord in enumerate(left)]
    leftdown = [(coord[0], up[i][1]) for i, coord in enumerate(right)]
    rightup = [(coord[0], down[i][1]) for i, coord in enumerate(left)]
    rightdown = [(coord[0], down[i][1]) for i, coord in enumerate(right)]

    if diagonals_only:
        return [leftup, rightup, rightdown, leftdown]

    return [left, leftup, up, rightup, right, rightdown, down, leftdown]


def on_grid(path: list[tuple[int, int]], grid_length) -> bool:
    for row, col in path:
        if 0 > row or row > grid_length:
            return False
        if 0 > col or col > grid_length:
            return False
    return True


def search(
    target_word: str,
    grid: list,
    paths: list | None = None,
    coord: tuple | None = None,
    return_paths=False,
) -> int:
    results = 0
    result_paths = []

    if paths is None:
        paths = get_paths(coord=coord, path_length=len(target_word))

    for path in paths:
        if on_grid(path, grid_length=len(grid)):
            try:
                word = "".join([grid[row][col] for row, col in path])
                if word == target_word:
                    results += 1
                    result_paths.append(path)
            except IndexError:
                pass
    if return_paths:
        return results, result_paths
    return results


def solve_puzzle(puzzle_str: str) -> int:
    grid = [row for row in puzzle_str.split("\n") if row]

    target_word = "XMAS"
    successes = 0
    for r_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char == target_word[0]:
                coord = (r_index, col_index)
                available_paths = get_paths(coord=coord, path_length=len(target_word))
                result = search(paths=available_paths, grid=grid, target_word=target_word)
                successes += result

    return successes


def solve_puzzle_diagonal(puzzle_str) -> int:
    grid = [row for row in puzzle_str.split("\n") if row]
    target_words = ["AS", "AM"]
    successes = 0

    for r_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            coord = (r_index, col_index)
            diagonal_match = 0
            for target_word in target_words:
                if char == target_word[0]:
                    # diagonal must be offset
                    available_paths = get_paths(
                        coord=coord, path_length=len(target_word), diagonals_only=True
                    )
                    word_match, match_paths = search(
                        paths=available_paths, grid=grid, target_word=target_word, return_paths=True
                    )
                    if word_match == 2:
                        interesting_rows = set([match[1][0] for match in match_paths])
                        interesting_cols = set([match[1][1] for match in match_paths])
                        if len(interesting_rows) == 1 or len(interesting_cols) == 1:
                            diagonal_match += 1
            if diagonal_match == 2:
                successes += 1
    return successes


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_04_input.txt", "r") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)
    part_b = solve_puzzle_diagonal(puzzle_input)
    print(part_b)

    submit(part_a, part="a")
    submit(part_b, part="b")
