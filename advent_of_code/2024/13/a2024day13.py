from pathlib import Path
from queue import PriorityQueue
import re
from tqdm import tqdm
from pulp import LpProblem, LpVariable, LpInteger, PULP_CBC_CMD, LpMinimize


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

#         if current_node[0] > prize[0] or current_node[1] > prize[1]:
#             continue

#         for cost, dx in moves:
#             neighbor = calculate_node(current_node, dx)
#             new_dist = cur_distance + cost
#             if new_dist < distances.get(neighbor, float("inf")):
#                 distances[neighbor] = new_dist
#                 queue.put((new_dist, neighbor))

#     return distances.get(prize, 0)

def solver(dx_a, dx_b, prize, factor=0):
# Create problem
    prob = LpProblem("My_Problem", sense=LpMinimize)  # Minimize can be arbitrary here

    # Create variables - LpInteger indicates that we need integer solutions
    n = LpVariable("n", lowBound=0, cat=LpInteger)
    m = LpVariable("m", lowBound=0, cat=LpInteger)

    # Equations
    ax, ay = dx_a
    bx, by = dx_b
    px, py = prize
    px += factor
    py += factor
    prob += ax * n + bx * m == px
    prob += ay * n + by * m == py

    # Dummy objective function
    prob += 0

    # Solve the problem using CBC solver
    prob.solve(PULP_CBC_CMD(msg=0))

    # Check if a valid solution was found
    if prob.status == 1:
        return int(n.value() * 3 + m.value())
    else:
        return 0

def solve_puzzle(puzzle_input, part2=False):
    machines = parse(puzzle_input)
    if part2:
        factor = 10000000000000
    else:
        factor = 0

    total = 0
    for machine in tqdm(machines):
        result = solver(*machine, factor=factor)
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

    part_b = solve_puzzle(puzzle_input, part2=True)
    print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
