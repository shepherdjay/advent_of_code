from advent_2024day18 import solve_puzzle, create_grid, parse


MAIN_EXAMPLE = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def test_create_grid():
    assert len(create_grid(size=2)) == 4


def test_parse():
    assert len(parse(MAIN_EXAMPLE)) == 25


def test_solve_puzzle() -> None:
    assert solve_puzzle(MAIN_EXAMPLE, bytes_to_fall=12, max_coord=6) == 22


def test_solve_puzzle_part2() -> None:
    assert solve_puzzle(MAIN_EXAMPLE, bytes_to_fall=12, max_coord=6, part2=True) == (6, 1)
