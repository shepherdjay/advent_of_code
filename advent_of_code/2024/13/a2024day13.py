from pathlib import Path
from queue import PriorityQueue
import re
from tqdm import tqdm
import numpy as np

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

    for a, b, p in zip(a_buttons, b_buttons, prizes):
        dx_a = int(a.group(1)), int(a.group(2))
        dx_b = int(b.group(1)), int(b.group(2))
        prize = int(p.group(1)), int(p.group(2))
        machines.append((dx_a, dx_b, prize))
    return machines


# def solver(dx_a, dx_b, prize):
#     origin = 0, 0
#     moves = [
#         (3, dx_a),
#         (1, dx_b),
#     ]
#     distances = {origin: 0}

#     queue = PriorityQueue()
#     queue.put((0, origin))

#     while not queue.empty():
#         cur_distance, current_node = queue.get()

#         if current_node == prize:
#             break

#         for cost, dx in moves:
#             neighbor = calculate_node(current_node, dx)
#             new_dist = cur_distance + cost
#             if new_dist < distances.get(neighbor, float("inf")) and new_dist <= 300:
#                 distances[neighbor] = new_dist
#                 queue.put((new_dist, neighbor))

#     return distances.get(prize, float("inf"))

def solver(dx_a, dx_b, prize):
    for m in range(0,100):
        for n in range(0, 100):
            result1 = n * dx_a[0] + m * dx_b[0]
            result2 = n * dx_a[1] + m * dx_b[1]

            if result1 == prize[0] and result2 == prize[1]:
                return n * 3 + m
    else:
        return float('inf')

def solve_puzzle(puzzle_input, part2=False):
    machines = parse(puzzle_input)

    total = 0
    for machine in tqdm(machines):
        result = solver(*machine)
        if result <= 300:
            total += result

    return total


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    machines = parse(puzzle_input)

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
