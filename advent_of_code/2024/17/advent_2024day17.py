from pathlib import Path
from unittest import case

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

    def adv(self, operand):
        numerator = self.reg_a
        denominator = 2**operand
        self.reg_a = numerator // denominator

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
        self.stdout.append(self.combo(operand) % 8)

    def bdv(self, operand):
        numerator = self.reg_a
        denominator = 2**operand
        self.reg_b = numerator // denominator

    def cdv(self, operand):
        numerator = self.reg_a
        denominator = 2**operand
        self.reg_c = numerator // denominator

    def run(self, program: list[int]) -> None:
        while True:
            try:
                opcode = program[self._inst_pointer]
                operand = str(program[self._inst_pointer + 1])
                if self.opcodes[opcode](operand=operand) is not False:
                    self._inst_pointer += 2
            except IndexError:
                return


def solve_puzzle(computer: Computer3Bit, program: list[int]) -> str:
    computer.run(program)
    return ",".join([str(x) for x in computer.stdout])


if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip("\n")

    # part_a = solve_puzzle(computer_a, program_a)
    # print(part_a)

    # part_b = solve_puzzle(puzzle_input, part2=True)
    # print(part_b)

    try:
        with open(f"../../../.token") as infile:
            session = infile.read().strip()
        # submit(part_a, part="a", session=session)
        # submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
