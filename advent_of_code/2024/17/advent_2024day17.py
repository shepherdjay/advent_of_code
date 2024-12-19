import re
from pathlib import Path

import tqdm

BASEPATH = Path(__file__).parent.resolve()

from queue import PriorityQueue


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

    def run(self, program: list[int], limit=False) -> list[int]:
        self._inst_pointer = 0
        self.stdout = list()

        iteration_cap = 10_000_000
        i = 0
        while i < iteration_cap:
            if limit and len(self.stdout) > len(program):
                return self.stdout
            try:
                opcode = program[self._inst_pointer]
                operand = program[self._inst_pointer + 1]
                if self.opcodes[opcode](operand=operand) is None:
                    self._inst_pointer += 2
            except IndexError:
                return self.stdout
            i += 1

    def __repr__(self):
        return f"Computer3Bit(reg_a={self.reg_a}, reg_b={self.reg_b}, reg_c={self.reg_c})"


def reverse_engineer_bits(target_value: int, program, existing_value: int = 0):
    possible_values = []
    for i in range(8):
        reg_a = (existing_value << 3) + i
        computer = Computer3Bit(reg_a=reg_a)
        if computer.run(program, limit=True)[0] == target_value:
            possible_values.append(reg_a)
    return possible_values


def find_reg_a(target_output: list[int]):
    possible_values = PriorityQueue()
    possible_values.put((0, len(target_output) - 1))

    while not possible_values.empty():
        reg_a, ptr = possible_values.get()
        computer = Computer3Bit(reg_a=reg_a)
        if computer.run(target_output, limit=True) == target_output:
            return reg_a
        else:
            possibilities = reverse_engineer_bits(
                target_output[ptr], existing_value=reg_a, program=target_output
            )
            for possibility in possibilities:
                possible_values.put((possibility, ptr - 1))


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
        return find_reg_a(program)


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
