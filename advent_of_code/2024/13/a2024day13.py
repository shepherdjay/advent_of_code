from pathlib import Path
from queue import PriorityQueue
import re
from tqdm import tqdm

BASEPATH = Path(__file__).parent.resolve()

RE_BUTTON_A = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
RE_BUTTON_B = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
RE_PRIZE = re.compile(r"X\=(\d+), Y\=(\d+)")


def calculate_node(origin, d):
    x, y = origin
    dx, dy = d
    return x + dx, y + dy


def parse(input_str):
    machines = []

    a_buttons = RE_BUTTON_A.finditer(input_str)
    b_buttons = RE_BUTTON_B.finditer(input_str)
    prizes = RE_PRIZE.finditer(input_str)

    for a, b, p in zip(a_buttons,b_buttons,prizes):
        dx_a = int(a.group(1)), int(a.group(2))
        dx_b = int(b.group(1)), int(b.group(2))
        prize = int(p.group(1)), int(p.group(2))
        machines.append((dx_a, dx_b, prize))
    return machines


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
    machines = parse(puzzle_input)

    total = 0
    for machine in tqdm(machines):
        result = solver(*machine)
        if result != float("inf"):
            total += result

    return total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    # part_b = solve_puzzle(puzzle_input, part2=True)
    # print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        # submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
