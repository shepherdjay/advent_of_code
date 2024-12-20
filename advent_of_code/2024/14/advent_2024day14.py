from pathlib import Path
import re
import math
import os
import time

BASEPATH = Path(__file__).parent.resolve()


class Robot:
    def __init__(self, position, velocity=(0, 0)):
        self.position = position
        self.velocity = velocity
        self._orig_position = position

    def move(self, ticks=1):
        for i in range(ticks):
            pos_x, pos_y = self.position
            vel_x, vel_y = self.velocity
            self.position = pos_x + vel_x, pos_y + vel_y

    def transpose(self, grid_x, grid_y):
        """
        Returns robot position wrapped by grid boundaries
        """
        pos_x, pos_y = self.position
        return pos_x % grid_x, pos_y % grid_y

    def reset_position(self):
        self.position = self._orig_position


def parse(puzzle_input):
    robots = []
    nums = re.compile(r"(-{0,1}\d+)")
    for line in puzzle_input.splitlines():
        matches = nums.findall(line)
        position = int(matches[0]), int(matches[1])
        velocity = int(matches[2]), int(matches[3])
        robots.append(Robot(position, velocity))
    return robots


def determine_quads(robots, grid_x, grid_y):
    left_value = list(range(0, grid_x // 2))
    right_value = list(range((grid_x // 2) + 1, grid_x))
    top_value = list(range(0, grid_y // 2))
    bottom_value = list(range((grid_y // 2) + 1, grid_y))
    q1 = []
    q2 = []
    q3 = []
    q4 = []

    for robot in robots:
        rob_x, rob_y = robot.transpose(grid_x=grid_x, grid_y=grid_y)
        if rob_x in left_value and rob_y in top_value:
            q1.append(robot)
        elif rob_x in right_value and rob_y in top_value:
            q2.append(robot)
        elif rob_x in left_value and rob_y in bottom_value:
            q3.append(robot)
        elif rob_x in right_value and rob_y in bottom_value:
            q4.append(robot)

    return q1, q2, q3, q4


def solve_puzzle(puzzle_input, grid_x, grid_y, part2=False, display=False):
    robots = parse(puzzle_input)
    if part2:
        return solve_part2(robots, grid_x, grid_y, display=display)

    for i in range(100):
        for robot in robots:
            robot.move()

    q1, q2, q3, q4 = determine_quads(robots, grid_x, grid_y)
    return len(q1) * len(q2) * len(q3) * len(q4)


def print_grid(robots, grid_x, grid_y):
    robot_coords = set()
    for robot in robots:
        rob_x, rob_y = robot.transpose(grid_x=grid_x, grid_y=grid_y)
        robot_coords.add((rob_x, rob_y))
    for y in range(grid_y):
        print()
        for x in range(grid_x):
            if (x, y) in robot_coords:
                print("R", end="")
            else:
                print(".", end="")


def clear():  # pragma: no cover
    os.system("clear")


def solve_part2(robots: list[Robot], grid_x, grid_y, display=False):
    max_iter = math.lcm(grid_x, grid_y)

    initial_start = 0

    [robot.move(initial_start) for robot in robots]

    min_iter = 0
    min_safety_score = float("inf")

    for i in range(initial_start, max_iter):
        q1, q2, q3, q4 = determine_quads(robots, grid_x, grid_y)
        safety_score = len(q1) * len(q2) * len(q3) * len(q4)
        if safety_score < min_safety_score:
            min_safety_score = safety_score
            min_iter = i
            if display:
                clear()
                print_grid(robots, grid_x, grid_y)
                print()
                print(f"Iteration {i}")
            time.sleep(1)

        [robot.move() for robot in robots]

    return min_iter, min_safety_score


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    part_a = solve_puzzle(puzzle_input, grid_x=101, grid_y=103)
    print(part_a)

    part_b, _ = solve_puzzle(puzzle_input, grid_x=101, grid_y=103, part2=True, display=True)
    print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
