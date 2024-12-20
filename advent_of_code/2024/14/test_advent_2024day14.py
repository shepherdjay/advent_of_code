from advent_2024day14 import solve_puzzle, parse, Robot, determine_quads, print_grid, solve_part2

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


def test_print_grid(capsys):
    robot = Robot((1, 1), (0, 0))
    grid_x, grid_y = 3, 3

    print_grid([robot], grid_x, grid_y)
    captured = capsys.readouterr()
    assert captured.out == "\n...\n.R.\n..."


def test_solve_part2_zero():
    """Min safety score will be 0 as robot never moves from middle"""
    robot = Robot((1, 1), (0, 0))
    grid_x, grid_y = 3, 3
    _, safety_score = solve_part2([robot], grid_x, grid_y)

    assert safety_score == 0


def test_solve_part2_two():
    """Min safety score will be 16 as there are 8 robots, two in each quadrant that never move"""
    robots = [
        Robot((0, 0)),
        Robot((0, 0)),
        Robot((2, 0)),
        Robot((2, 0)),
        Robot((2, 2)),
        Robot((2, 2)),
        Robot((0, 2)),
        Robot((0, 2)),
    ]
    grid_x, grid_y = 3, 3
    _, safety_score = solve_part2(robots, grid_x, grid_y)

    assert safety_score == 16
