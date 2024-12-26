from pathlib import Path

BASEPATH = Path(__file__).parent.resolve()

def grid_it(input_str):
    rows = []
    for row in input_str.splitlines():
        new_row = []
        for char in row.strip():
            new_row.append(char)
        rows.append(new_row)
    return rows

class Key:
    def __init__(self, heights: list[int]):
        self.heights = heights

    @classmethod
    def from_string(cls, input_str):
        grid = grid_it(input_str)
        grid.reverse()
        num_rows = len(grid)
        num_cols = len(grid[0])

        heights = []
        for col in range(num_cols):
            height = 0
            for row in range(1, num_rows):
                if grid[row][col] == "#":
                    height += 1
                else:
                    heights.append(height)
                    break
        return Key(heights=heights)


class Lock:
    def __init__(self, pins: list[int]):
        self.pins = pins

    @classmethod
    def from_string(cls, input_string: str):
        grid = grid_it(input_string)

        num_rows = len(grid)
        num_cols = len(grid[0])

        pins = []
        for col in range(num_cols):
            height = 0
            for row in range(1, num_rows):
                if grid[row][col] == "#":
                    height += 1
                else:
                    pins.append(height)
                    break
        return Lock(pins=pins)




def parse_individual(input_str: str) -> Key|Lock:
    if input_str.startswith('#'):
        return Lock.from_string(input_str)
    if input_str.startswith('.'):
        return Key.from_string(input_str)


def parse(input_str: str) -> tuple[list[Key],list[Lock]]:
    keys = []
    locks = []

    return keys, locks

def solve_puzzle(puzzle_input, part2=False):
    pass

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