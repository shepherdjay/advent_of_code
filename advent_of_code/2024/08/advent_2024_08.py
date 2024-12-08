from collections import defaultdict
from itertools import combinations


def grid_dist(coord_a, coord_b):
    distance = sum(abs(val1 - val2) for val1, val2 in zip(coord_a, coord_b))
    return distance


def calculate_slopes(antennas_map: dict[str : list[tuple]]) -> dict[tuple : set[float]]:
    slopes = {}
    for _, points in antennas_map.items():
        if len(points) > 1:
            for orig_point, dest_point in combinations(points, 2):
                slopes[orig_point] = set()
                x1, y1 = orig_point[1], orig_point[0]
                x2, y2 = dest_point[1], dest_point[0]
                distance = grid_dist(orig_point, dest_point)
                try:
                    slope = (y2 - y1) / (x2 - x1)
                except ZeroDivisionError:
                    slope = "undefined"
                slopes[orig_point].add((slope, distance))
    return slopes


def on_a_slope(origin, slopes_dict):
    if origin in slopes_dict:
        return True
    for point, slopes in slopes_dict.items():
        distance = grid_dist(origin, point)
        for slope, slope_dist in slopes:
            if distance % slope_dist == 0:
                x, y = origin[1], origin[0]
                x1, y1 = point[1], point[0]
                if slope == "undefined":
                    if x == x1:
                        return True
                if y - y1 == slope * (x - x1):
                    return True
    return False


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


def solve_puzzle_two(puzzle_input):
    grid = [[char for char in line] for line in puzzle_input.split()]
    antennas = map_antennas(grid)
    slopes = calculate_slopes(antennas)

    total = 0
    for r_idx, row in enumerate(grid):
        for c_idx, _ in enumerate(row):
            if on_a_slope((r_idx, c_idx), slopes_dict=slopes):
                total += 1
    return total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_08_input.txt") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    part_b = solve_puzzle_two(puzzle_input)
    print(part_b)

    try:
        submit(part_a, part="a")
        submit(part_b, part="b")
    except:
        pass
