from collections import defaultdict


def calculate_double(orig_coord, target_coord):
    distance_row = target_coord[0] - orig_coord[0]
    new_row = orig_coord[0] + (distance_row * 2)

    distance_col = target_coord[1] - orig_coord[1]
    new_col = orig_coord[1] + (distance_col * 2)
    return (new_row, new_col)


def map_antennas(grid: list[list[str]]) -> dict[str : list[tuple[int, int]]]:
    antennas = defaultdict(list)
    for r_idx, row in enumerate(grid):
        for c_idx, symbol in enumerate(row):
            if symbol == ".":
                continue
            antennas[symbol].append((r_idx, c_idx))
    return antennas


def at_anninode(coord, antenna_map):
    for _, a_coords in antenna_map.items():
        for a_coord in a_coords:
            if coord == a_coord:
                continue
            double = calculate_double(orig_coord=coord, target_coord=a_coord)
            if double in a_coords:
                return True
    return False


def solve_puzzle(puzzle_input: str):
    grid = [[char for char in line] for line in puzzle_input.split()]
    antennas = map_antennas(grid)
    total = 0
    for r_idx, row in enumerate(grid):
        for c_idx, _ in enumerate(row):
            coord = (r_idx, c_idx)
            if at_anninode(coord, antennas):
                total += 1
    return total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_08_input.txt") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    submit(part_a, part="a")
