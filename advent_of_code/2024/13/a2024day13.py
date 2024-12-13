from pathlib import Path
from queue import PriorityQueue

BASEPATH = Path(__file__).parent.resolve()


def calculate_node(origin, d):
    x, y = origin
    dx, dy = d
    return x + dx, y + dy


def solver(dx_a, dx_b, prize):
    origin = 0, 0
    cost_a = 3
    cost_b = 1
    visited = set()
    distances = {origin: 0}

    queue = PriorityQueue()
    queue.put((0, origin))

    while queue:
        cur_distance, current_node = queue.get()
        if min(current_node) > max(prize):
            break
        if current_node in visited:
            continue
        for weight, neighbor in zip(
            [cost_a, cost_b], [calculate_node(current_node, dn) for dn in [dx_a, dx_b]]
        ):
            new_dist = cur_distance + weight
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                queue.put((new_dist, neighbor))

    try:
        return distances[prize]
    except KeyError:
        return float("inf")


def solve_puzzle(puzzle_input, part2=False):
    pass


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    part_b = solve_puzzle(puzzle_input, part2=True)
    print(part_b)

    try:
        submit(part_a, part="a")
        submit(part_b, part="b")
    except AocdError as e:
        pass
