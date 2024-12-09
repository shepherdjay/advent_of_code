from pathlib import Path
from dataclasses import dataclass

BASEPATH = Path(__file__).parent.resolve()


@dataclass
class File:
    name: int
    size: int

    def __str__(self):
        return f"{self.name}"


class FileSystem:
    def __init__(self, disk_size: int = 0):
        self._disk = [None for _ in range(disk_size)]
        self.fragmented = False

    def find_free_space(self, desired_space: int, _start_idx=0):
        print(f"finding {desired_space}")
        free_sectors = 0
        for i, value in enumerate(self._disk):
            if i >= _start_idx:
                if value is None:
                    free_sectors += 1
                else:
                    free_sectors = 0
                if free_sectors == desired_space:
                    return i - desired_space + 1

    def add_file(self, file: File, loc: int = 0, dnf=False):
        if dnf:
            space_needed = file.size
        else:
            space_needed = 1

        allocated = 0
        start = self.find_free_space(space_needed, _start_idx=loc)
        while True:
            self._disk[start] = file
            allocated += 1
            if allocated == file.size:
                break
            if dnf:
                start += 1
            else:
                start = self.find_free_space(max(1, (space_needed - allocated)), _start_idx=loc)

    def describe(self):
        for sector in self._disk:
            if isinstance(sector, File):
                yield sector.name
            elif sector:
                yield sector
            else:
                yield "."

    @classmethod
    def from_string(cls, description_string) -> 'FileSystem':
        file_system = cls()
        print(file_system)
        file_index = 0
        location = 0
        for i, value in enumerate(description_string):
            if (i + 1) % 2 == 0:
                file_system._disk += [None] * int(value)
            else:
                file_system._disk += [f"{file_index}"] * int(value)
                file_index += 1
        return file_system


def construct_filesystem(puzzle_input):
    file_system = []
    file_index = 0
    for i, value in enumerate(puzzle_input):
        if (i + 1) % 2 == 0:
            file_system += ["."] * int(value)
        else:
            file_system += [f"{file_index}"] * int(value)
            file_index += 1
    return file_system


def solve_puzzle(puzzle_input, part2=False):
    filesystem = construct_filesystem(puzzle_input)
    left_idx = 0
    right_idx = len(filesystem) - 1

    new_filesystem = []
    while left_idx <= right_idx:
        if filesystem[left_idx] != ".":
            new_filesystem.append(int(filesystem[left_idx]))
            left_idx += 1
        else:
            if filesystem[right_idx] != ".":
                new_filesystem.append(int(filesystem[right_idx]))
                right_idx -= 1
                left_idx += 1
            else:
                right_idx -= 1

    return sum([i * x for i, x in enumerate(new_filesystem)])


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
        # submit(part_b, part="b", session=session)
    except AocdError as e:
        pass
