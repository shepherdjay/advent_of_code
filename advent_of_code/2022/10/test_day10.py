import pytest
from day10 import process_instruction_set, CommunicationsDevice
import os

with open(os.path.join(os.path.dirname(__file__), "test_day10_input.txt"), "r") as elf_file:
    EXAMPLE_INSTRUCTIONS = [line.strip() for line in elf_file]


@pytest.mark.parametrize("cycle,register,signal", [(20, 21, 420), (60, 19, 1140), (100, 18, 1800)])
def test_day10_with_example(cycle, register, signal):
    prototype = CommunicationsDevice()

    inst_indx = 0
    while prototype.cycles < cycle:
        cur_instruction = EXAMPLE_INSTRUCTIONS[inst_indx]
        process_instruction_set(instructions=[cur_instruction], cpu=prototype)
        inst_indx += 1

    assert prototype.reg_history[cycle] == register
    assert prototype.signal_strength(cycle) == signal


def test_CPU_initialization():
    prototype = CommunicationsDevice()
    assert prototype.X == 1
    assert prototype.reg_history == [1]


def test_CPU_addx():
    prototype = CommunicationsDevice()

    prototype.addx(5)

    assert prototype.X == 6
    assert prototype.cycles == 2
    assert prototype.reg_history == [1, 1, 1]

    prototype._tick()
    assert prototype.reg_history == [1, 1, 1, 6]
