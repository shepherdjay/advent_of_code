import pytest
from a2024day13 import solver, solve_puzzle, parse, calculate_node


def test_calculate_node():
    dx_a = (94, 34)
    dx_b = (22, 67)
    prize = (8400, 5400)

    origin = (0, 0)
    for _ in range(80):
        origin = calculate_node(origin, dx_a)
    for _ in range(40):
        origin = calculate_node(origin, dx_b)
    assert origin == prize


@pytest.mark.parametrize(
    "dx_a,dx_b,prize,expected",
    [
        ((94, 34), (22, 67), (8400, 5400), 280),
        ((26, 66), (67, 21), (12748, 12176), float("inf")),
    ],
)
def test_solver(dx_a, dx_b, prize, expected):
    assert solver(dx_a=dx_a, dx_b=dx_b, prize=prize) == expected


def test_parse():
    assert parse("""
                 Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
                 
""") == [((94, 34), (22, 67), (8400, 5400))]


def test_parse_example():
    with open("sample_input.txt") as infile:
        assert len(parse(infile.read())) == 4


def test_solve_example():
    with open("sample_input.txt") as infile:
        assert solve_puzzle(infile.read()) == 480
