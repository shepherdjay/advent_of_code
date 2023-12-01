from typing import Dict
from dataclasses import dataclass
from typing import List


class ElfDirectory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.contents = list()

    def get_size(self):
        size = 0
        for item in self.contents:
            size += item.get_size()
        return size

    def to_dict(self):
        temp_dict = {}

        for item in self.contents:
            if isinstance(item, ElfDirectory):
                temp_dict[item.name] = item.to_dict()
            elif isinstance(item, ElfFile):
                temp_dict[item.name] = item.size
        return temp_dict

    def add_file(self, filename, size):
        the_thing = ElfFile(filename, int(size), parent=self)
        self.contents.append(the_thing)
        return the_thing

    def add_directory(self, name):
        the_thing = ElfDirectory(name, parent=self)
        self.contents.append(the_thing)
        return the_thing

    def search_dir(self, search_name):
        for item in self.contents:
            if isinstance(item, ElfDirectory) and item.name == search_name:
                return item

    def __lt__(self, other: "ElfDirectory"):
        if not isinstance(other, ElfDirectory):
            raise TypeError
        if self.get_size() < other.get_size():
            return True

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Directory(name={self.name}, parent={self.parent})"


@dataclass
class ElfFile:
    name: str
    size: int
    parent: ElfDirectory

    def get_size(self):
        return self.size


def construct_tree(terminal_output: List[str]) -> List[ElfDirectory]:
    directories = [ElfDirectory("/")]
    cwd = directories[0]
    for line in terminal_output:
        if line.startswith("$ cd"):
            match line[5::]:
                case "/":
                    cwd = directories[0]
                case "..":
                    cwd = cwd.parent
                case other:
                    cwd = cwd.search_dir(other)
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            new_dir_name = line[4::]
            directories.append(cwd.add_directory(name=new_dir_name))
        else:
            size, filename = line.split()
            cwd.add_file(filename=filename, size=size)

    return directories


def find_all_dir_sizes(terminal_output: List[str], maxsize: int = float("inf")) -> Dict:
    all_dirs = construct_tree(terminal_output)

    sizes = {}
    for dir in all_dirs:
        size = dir.get_size()
        if size <= maxsize:
            sizes[dir] = size
    return sizes


if __name__ == "__main__":
    with open("advent_07_input.txt", "r") as elf_file:
        commands = [line.strip() for line in elf_file]

    max_100k = find_all_dir_sizes(commands, maxsize=100_000)
    print(max_100k)
    print(sum(max_100k.values()))

    # PART 2
    total_size = 70_000_000
    install_space = 30_000_000

    all_dirs = find_all_dir_sizes(commands)
    root_size = sorted(all_dirs.keys(), reverse=True)[0].get_size()

    unused_space = total_size - root_size
    needed_space = install_space - unused_space

    candidate_dirs = sorted(find_all_dir_sizes(commands, maxsize=install_space))

    for candidate_dir in candidate_dirs:
        if candidate_dir.get_size() >= needed_space:
            print(f"Unused Space: {unused_space}, Needed Space: {needed_space}")
            print(
                f"Should delete {candidate_dir.parent}/{candidate_dir} with size {candidate_dir.get_size()}"
            )
            break
