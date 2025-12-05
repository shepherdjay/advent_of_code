from pathlib import Path
from advent_of_code.utils.grids import parse_grid, get_inbounds_neighbors

BASEPATH = Path(__file__).parent.resolve()

def solve_puzzle_part1(grid):
    count = 0
    removable = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '@':
                like_neighbors = 0
                neighbors = get_inbounds_neighbors((i, j), grid_height=len(grid), grid_width=len(grid[0]), diagonals=True)
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