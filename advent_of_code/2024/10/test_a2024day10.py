from a2024day10 import solve_puzzle, calculate_path, create_grid, get_neighbors


EXAMPLE = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

SIMPLE = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""

def test_solve_puzzle_example():
    assert solve_puzzle(EXAMPLE) == 36

def test_create_grid():
    grid_str = ".1.\n..."
    expected = [[-1,1,-1],[-1,-1,-1,]]
    assert create_grid(grid_str) == expected

def test_calculate_path():
    grid = create_grid(SIMPLE)
    origin = (0, 3)
    assert calculate_path(origin, grid) == 2

def test_get_neighbors():
    origin = (4,4)
    neighbors = [
        (3, 4), (5,4), (4,3), (4,5)
    ]
    assert get_neighbors(origin) == neighbors
