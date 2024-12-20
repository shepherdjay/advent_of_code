from pathlib import Path
import re

BASEPATH = Path(__file__).parent.resolve()


class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self):
        pos_x, pos_y = self.position
        vel_x, vel_y = self.velocity
        self.position = pos_x + vel_x, pos_y + vel_y

    def transpose(self, grid_x, grid_y):
        """
        Returns robot position wrapped by grid boundaries
        """
        pos_x, pos_y = self.position
        return pos_x % grid_x, pos_y % grid_y


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


def solve_puzzle(puzzle_input, grid_x, grid_y, part2=False):
    robots = parse(puzzle_input)
    for i in range(100):
        for robot in robots:
            robot.move()

    q1, q2, q3, q4 = determine_quads(robots, grid_x, grid_y)
    return len(q1) * len(q2) * len(q3) * len(q4)


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    part_a = solve_puzzle(puzzle_input, grid_x=101, grid_y=103)
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
