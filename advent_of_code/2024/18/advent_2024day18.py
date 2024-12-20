from pathlib import Path
from copy import deepcopy
from collections import deque

BASEPATH = Path(__file__).parent.resolve()


def create_grid(size: int) -> list[list[int]]:
    grid = {(x, y) for x in range(size) for y in range(size)}
    return grid


def get_neighbors(origin):
    x, y = origin
    return [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    ]


def bfs(obstacles: set[tuple[int, int]], max_coord) -> tuple[int, list[tuple[int, int]]]:
    target = (max_coord, max_coord)
    origin = (0, 0)
    grid = create_grid(max_coord + 1)

    stack = deque([(origin, [origin])])
    visited = set()

    while stack:
        cur_node, path = stack.popleft()
        if cur_node == target:
            return len(path) - 1, path
        if cur_node in visited:
            continue

        visited.add(cur_node)
        neighbors = get_neighbors(cur_node)

        for neighbor in neighbors:
            if neighbor not in obstacles and neighbor not in visited and neighbor in grid:
                new_path = deepcopy(path) + [neighbor]
                stack.append((neighbor, new_path))
    return float("inf"), None


def parse(puzzle_input: str) -> list[tuple[int, int]]:
    bytes = []
    for line in puzzle_input.splitlines():
        x, y = line.split(",")
        bytes.append((int(x), int(y)))
    return bytes


def solve_puzzle(puzzle_input: str, bytes_to_fall=1024, max_coord=70, part2=False):
    bytes = parse(puzzle_input)

    if part2:
        _, path = bfs(obstacles=set(), max_coord=max_coord)
        obstacles = []
        for byte in bytes:
            obstacles.append(byte)
            if byte in path:
                # Recalculate
                _, path = bfs(obstacles=set(obstacles), max_coord=max_coord)
                if path is None:
                    return byte

    steps, path = bfs(obstacles=set(bytes[0:bytes_to_fall]), max_coord=max_coord)
    return steps


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    x, y = solve_puzzle(puzzle_input, part2=True)
    part_b = f"{x},{y}"
    print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
