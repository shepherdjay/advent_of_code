from pathlib import Path
from unittest import case
import re
import tqdm

import itertools

from tqdm import tqdm

BASEPATH = Path(__file__).parent.resolve()


class Computer3Bit:
    def __init__(self, reg_a: int = 0, reg_b: int = 0, reg_c: int = 0):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self._inst_pointer = 0

        self.stdout = list()

        self._program = None

        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def combo(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.reg_a
            case 5:
                return self.reg_b
            case 6:
                return self.reg_c
            case 7:
                raise RuntimeError("7 is not supposed to appear")

    def _dv(self, operand):
        numerator = self.reg_a
        denominator = 2 ** self.combo(operand)
        return numerator // denominator

    def adv(self, operand):
        self.reg_a = self._dv(operand)

    def bxl(self, operand):
        self.reg_b = self.reg_b ^ operand

    def bst(self, operand):
        self.reg_b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.reg_a != 0:
            self._inst_pointer = operand
            return False

    def bxc(self, operand):
        self.reg_b = self.reg_b ^ self.reg_c

    def out(self, operand):
        out_value = self.combo(operand) % 8
        self.stdout.append(out_value)

    def bdv(self, operand):
        self.reg_b = self._dv(operand)

    def cdv(self, operand):
        self.reg_c = self._dv(operand)

    def run(self, program: list[int], limit=False) -> None:
        self._inst_pointer = 0
        self.stdout = list()

        while True:
            if limit and len(self.stdout) > len(program):
                return
            try:
                opcode = program[self._inst_pointer]
                operand = program[self._inst_pointer + 1]
                if self.opcodes[opcode](operand=operand) is None:
                    self._inst_pointer += 2
            except IndexError:
                return

    def __repr__(self):
        return f"Computer3Bit(reg_a={self.reg_a}, reg_b={self.reg_b}, reg_c={self.reg_c})"


def parse(puzzle_input: str) -> tuple[Computer3Bit, list[int]]:
    computer = Computer3Bit()
    digits = re.compile(r"\d+")

    for i, line in enumerate(puzzle_input.splitlines(), start=1):
        match i:
            case 1:
                computer.reg_a = int(digits.search(line).group())
            case 2:
                computer.reg_b = int(digits.search(line).group())
            case 3:
                computer.reg_c = int(digits.search(line).group())
            case 5:
                program = [int(x) for x in digits.findall(line)]
            case _:
                pass
    return computer, program


def solve_puzzle(puzzle_input, part2=False) -> str:
    computer, program = parse(puzzle_input)

    if not part2:
        computer.run(program)
        return ",".join([str(x) for x in computer.stdout])
    else:
        for i in tqdm(itertools.count()):
            computer.reg_a = i
            computer.run(program, limit=True)
            if computer.stdout == program:
                return i


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    part_b = solve_puzzle(puzzle_input, part2=True)
    print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
