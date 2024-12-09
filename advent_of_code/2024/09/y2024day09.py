from pathlib import Path
from dataclasses import dataclass

BASEPATH = Path(__file__).parent.resolve()

@dataclass
class Freespace:
    i: int
    size: int

@dataclass
class File:
    name: int
    size: int

class FileSystem():
    def __init__(self, disk_size: int):
        self._disk = ['.'] * disk_size

    def add_file(file: File, start=None):
        pass
        
        

def construct_filesystem(puzzle_input):
    file_system = []
    file_index = 0
    for i, value in enumerate(puzzle_input):
        if (i + 1) % 2 == 0:
            file_system += ['.'] * int(value)
        else:
            file_system += [f'{file_index}'] * int(value)
            file_index += 1
    return file_system

def solve_puzzle(puzzle_input, part2=False):
    filesystem = construct_filesystem(puzzle_input)
    left_idx = 0
    right_idx = len(filesystem) - 1

    new_filesystem = []
    while left_idx <= right_idx:
        if filesystem[left_idx] != '.':
            new_filesystem.append(int(filesystem[left_idx]))
            left_idx += 1
        else:
            if filesystem[right_idx] != '.':
                new_filesystem.append(int(filesystem[right_idx]))
                right_idx -= 1
                left_idx += 1
            else:
                right_idx -= 1
    
    return sum([i * x for i,x in enumerate(new_filesystem)])
        



if __name__ == "__main__":  # pragma: no cover
    from aocd import submit
    from aocd.exceptions import AocdError

    with open(f"{BASEPATH}/input.txt") as infile:
        puzzle_input = infile.read().strip('\n')

    part_a = solve_puzzle(puzzle_input)
    print(part_a)

    part_b = solve_puzzle(puzzle_input, part2=True)
    print(part_b)

    try:
        with open(f'../../../.token') as infile:
            session = infile.read().strip()
        submit(part_a, part="a", session=session)
        # submit(part_b, part="b", session=session)
    except AocdError as e:
        pass