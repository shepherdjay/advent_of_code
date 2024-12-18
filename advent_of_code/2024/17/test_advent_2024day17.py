from advent_2024day17 import Computer3Bit, solve_puzzle, parse
import pytest

MAIN_EXAMPLE = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


def test_simple_example_1():
    computer = Computer3Bit(reg_c=9)
    computer.run(program=[2, 6])

    assert computer.reg_b == 1


def test_simple_example_2():
    # If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2
    computer = Computer3Bit(reg_a=10)
    computer.run(program=[5, 0, 5, 1, 5, 4])

    assert computer.stdout == [0, 1, 2]


def test_simple_example_3():
    """
    If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0
    and leave 0 in register A.
    """
    computer = Computer3Bit(reg_a=2024)
    computer.run(program=[0, 1, 5, 4, 3, 0])
    assert computer.stdout == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]
    assert computer.reg_a == 0


def test_simple_example_4():
    """
    If register B contains 29, the program 1,7 would set register B to 26
    """
    computer = Computer3Bit(reg_b=29)
    computer.run(program=[1, 7])
    assert computer.reg_b == 26


def test_simple_example_5():
    """
    If register B contains 2024 and register C contains 43690,
    the program 4,0 would set register B to 44354.
    """
    computer = Computer3Bit(reg_b=2024, reg_c=43690)
    computer.run(program=[4, 0])
    assert computer.reg_b == 44354


def test_parse():
    actual_comp, act_program = parse(MAIN_EXAMPLE)

    assert act_program == [0, 1, 5, 4, 3, 0]
    assert actual_comp.reg_a == 729


def test_solver_example():
    assert solve_puzzle(MAIN_EXAMPLE) == "4,6,3,5,6,3,5,2,1,0"


def test_solver_example_part2():
    assert (
        solve_puzzle(
            puzzle_input="""Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""",
            part2=True,
        )
        == 117440
    )
