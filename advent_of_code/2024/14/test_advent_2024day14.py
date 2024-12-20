from advent_2024day14 import solve_puzzle, parse, Robot, determine_quads

MAIN_EXAMPLE = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def test_parse():
    robots = parse("""p=0,4 v=3,-3""")
    assert len(robots) == 1
    assert robots[0].position == (0, 4)
    assert robots[0].velocity == (3, -3)


def test_parse_example():
    robots = parse(MAIN_EXAMPLE)
    assert len(robots) == 12


def test_robot_move_basic():
    robot = Robot((2, 4), (2, -3))
    robot.move()
    assert robot.position == (4, 1)


def test_robot_move_wraps():
    robot = Robot((2, 4), (2, -3))
    for i in range(5):
        robot.move()
    assert robot.transpose(grid_x=11, grid_y=7) == (1, 3)


def test_solve_puzzle_example():
    assert solve_puzzle(MAIN_EXAMPLE, grid_x=11, grid_y=7) == 12


def test_determine_quads():
    robot = Robot((2, 4), (2, -3))
    for i in range(5):
        robot.move()
    q1, q2, q3, q4 = determine_quads([robot], grid_x=11, grid_y=7)
    # ROBOT IS IN MIDDLE
    assert len(q1) == 0
    assert len(q2) == 0
    assert len(q3) == 0
    assert len(q4) == 0
