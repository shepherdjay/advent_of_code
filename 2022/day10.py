from typing import List


class CPU:

    def __init__(self, X: int = 1, cycles: int = 0):
        self.X = X
        self.cycles = cycles
        self.reg_history = [X]

    def _tick(self):
        self.reg_history.append(self.X)
        self.cycles += 1

    def addx(self, value: int):
        self._tick()
        self._tick()
        self.X += value

    def noop(self):
        self._tick()

    def signal_strength(self, reg_hist_indx=-1):
        return reg_hist_indx * self.reg_history[reg_hist_indx]


def process_instruction_set(instructions: List[str], cpu: CPU):
    """
    >>> instructions = ['noop', 'addx 3', 'addx -5']
    >>> cpu = CPU()
    >>> process_instruction_set(instructions, cpu)
    >>> cpu.reg_history[1], cpu.reg_history[2], cpu.reg_history[3], cpu.reg_history[4], cpu.reg_history[5]
    (1, 1, 1, 4, 4)
    """
    for instruction in instructions:
        match instruction.split():
            case ['noop']:
                cpu.noop()
            case ['addx', value]:
                cpu.addx(value=int(value))


if __name__ == '__main__':
    with open('day10_input.txt', 'r') as elf_file:
        instructions = [line.strip() for line in elf_file]

    walkie_talkie = CPU()
    process_instruction_set(instructions, walkie_talkie)

    print(sum([
        walkie_talkie.signal_strength(x) for x in [20, 60, 100, 140, 180, 220]]
    ))
