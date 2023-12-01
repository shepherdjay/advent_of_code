from typing import List


class CommunicationsDevice:
    def __init__(self, X: int = 1, cycles: int = 0):
        self.X = X
        self.cycles = cycles
        self.reg_history = [X]

        self.display = []
        for _ in range(6):
            new_row = list()
            for _ in range(40):
                new_row.append(".")
            self.display.append(new_row)

        self._pixel_gen = self._yield_pixel()

    def _yield_pixel(self):
        while True:
            for row_idx in range(6):
                for col_idx in range(40):
                    yield col_idx, row_idx

    def _tick(self):
        self.reg_history.append(self.X)
        pixel_x, pixel_y = self._pixel_gen.__next__()

        if pixel_x in range(self.X - 1, self.X + 2):
            char = "#"
        else:
            char = "."
        self.display[pixel_y][pixel_x] = char

        self.cycles += 1

    def draw(self):
        for row in self.display:
            for char in row:
                print(char, end="")
            print()

    def addx(self, value: int):
        self._tick()
        self._tick()
        self.X += value

    def noop(self):
        self._tick()

    def signal_strength(self, reg_hist_indx=-1):
        return reg_hist_indx * self.reg_history[reg_hist_indx]


def process_instruction_set(instructions: List[str], cpu: CommunicationsDevice):
    """
    >>> instructions = ['noop', 'addx 3', 'addx -5']
    >>> cpu = CommunicationsDevice()
    >>> process_instruction_set(instructions, cpu)
    >>> cpu.reg_history[1], cpu.reg_history[2], cpu.reg_history[3], cpu.reg_history[4], cpu.reg_history[5]
    (1, 1, 1, 4, 4)
    """
    for instruction in instructions:
        match instruction.split():
            case ["noop"]:
                cpu.noop()
            case ["addx", value]:
                cpu.addx(value=int(value))


if __name__ == "__main__":
    with open("day10_input.txt", "r") as elf_file:
        instructions = [line.strip() for line in elf_file]

    walkie_talkie = CommunicationsDevice()
    process_instruction_set(instructions, walkie_talkie)

    print(sum([walkie_talkie.signal_strength(x) for x in [20, 60, 100, 140, 180, 220]]))

    walkie_talkie.draw()
