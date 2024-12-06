import itertools


class Loop(Exception):
    pass


class Guard:
    def __init__(self, coord):
        self.coord = coord

        self.directions = itertools.cycle(["N", "E", "S", "W"])
        self.path = [coord]

    @property
    def visited(self):
        return set(self.path)

    def walk(self, obstructions):
        direction = next(self.directions)
        obstructions_hit = set()

        while True:
            row, col = self.coord
            match direction:
                case "N":
                    next_coord = row - 1, col
                case "E":
                    next_coord = row, col + 1
                case "S":
                    next_coord = row + 1, col
                case "W":
                    next_coord = row, col - 1
            if next_coord in obstructions:
                if (direction, next_coord) in obstructions_hit:
                    raise Loop
                obstructions_hit.add((direction, next_coord))
                direction = next(self.directions)
                continue
            else:
                self.coord = next_coord
                self.path.append(self.coord)
                yield (self.coord)


def string_to_grid(the_string):
    return [[char for char in line] for line in the_string.split()]


def map_grid(grid):
    obstructions = set()

    for r_idx, row in enumerate(grid):
        for c_idx, value in enumerate(row):
            coord = (r_idx, c_idx)
            if value == "#":
                obstructions.add(coord)
            if value == "^":
                guard_coord = coord
    return obstructions, guard_coord


def solve_puzzle_loop(puzzle_input):
    grid = string_to_grid(puzzle_input)

    new_obstruction_possibilities = []

    for r_idx, row in enumerate(grid):
        for c_idx, value in enumerate(row):
            if value == "#" or value == "^":
                continue
            else:
                grid[r_idx][c_idx] = "#"
                obstructions, guard_coord = map_grid(grid)
                guard = Guard(guard_coord)
                try:
                    for row, col in guard.walk(obstructions):
                        if 0 > row or row >= len(grid):
                            break
                        if 0 > col or col >= len(grid):
                            break
                except Loop:
                    new_obstruction_possibilities.append((r_idx, c_idx))
                grid[r_idx][c_idx] = "."

    return len(new_obstruction_possibilities)


def solve_puzzle(puzzle_input):
    grid = string_to_grid(puzzle_input)
    obstructions, guard_coord = map_grid(grid)

    guard = Guard(guard_coord)

    for row, col in guard.walk(obstructions):
        if 0 > row or row >= len(grid):
            break
        if 0 > col or col >= len(grid):
            break
    guard.path.pop()

    return len(guard.visited)


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit

    with open("advent_2024_06_input.txt", "r") as infile:
        puzzle_input = infile.read()

    part_a = solve_puzzle(puzzle_input)
    print(part_a)
    part_b = solve_puzzle_loop(puzzle_input)
    print(part_b)

    submit(part_a, part="a")
    submit(part_b, part="b")
