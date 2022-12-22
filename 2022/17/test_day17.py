from itertools import cycle
from day17 import part1, part2, Rock, Coord, solver
from unittest.mock import patch
import math

@patch('day17.tqdm')
def test_part1_example(fake_tqdm):
    example_str = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    assert part1(example_str) == 3068

@patch('day17.tqdm')
def test_part2_example(fake_tqdm):
    example_str = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    assert part2(example_str) == 1514285714288

@patch('day17.tqdm')
def test_cycle_checker(fake_tqdm):
    cycle_str = '<<<<'
    iterations = 1000
    lcm = math.lcm(5, len(cycle_str))
    cycle_solver = solver(cycle(cycle_str), max_rocks=iterations, lcm=lcm)
    assert cycle_solver == 2200

def test_generate_rocks():
    straight_h = [Coord(2, 0), Coord(3, 0), Coord(4, 0), Coord(5, 0)]
    plus = [Coord(3, 0), Coord(2, 1), Coord(3, 1), Coord(4, 1), Coord(3, 2)]
    right_angle = [Coord(2, 0), Coord(3, 0), Coord(4, 0), Coord(4, 1), Coord(4, 2)]
    straight_v = [Coord(2, 0), Coord(2, 1), Coord(2, 2), Coord(2, 3)]
    block = [Coord(2, 0), Coord(3, 0), Coord(2, 1), Coord(3, 1)]

    assert Rock._straight_h(height=0) == Rock(straight_h), 'straight'
    assert Rock._plus(height=0) == Rock(plus), 'plus'
    assert Rock._right_angle(height=0) == Rock(right_angle), 'right_angle'
    assert Rock._straight_v(height=0) == Rock(straight_v), 'straight_v'
    assert Rock._block(height=0) == Rock(block), 'block'
