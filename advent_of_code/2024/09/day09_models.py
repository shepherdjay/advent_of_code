from dataclasses import dataclass

@dataclass
class File:
    name: int
    size: int

    def __str__(self):
        return f"{self.name}"

    def __hash__(self):
        return hash(self.name)

@dataclass
class FileBlock:
    size: int
    start_idx: int
    file_ptr: File

    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.file_ptr)

@dataclass
class FreeBlock:
    size: int
    start_idx: int

    def __len__(self):
        return self.size
    
    def __str__(self):
        return '.'


class FileSystem:
    def __init__(self, disk_size: int = 0):
        self._disk = [None for _ in range(disk_size)]
        self._descriptors = [FreeBlock(disk_size, start_idx=0)]

    def find_free_space(self, desired_space: int, _start_idx=0):
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
            if start is None:
                raise RuntimeError("No Space")
            self._disk[start] = file
            allocated += 1
            if allocated == file.size:
                break
            if dnf:
                start += 1
            else:
                start = self.find_free_space(max(1, (space_needed - allocated)), _start_idx=start)

    def delete_file(self, file: File):
        indexes = [i for i, x in enumerate(self._disk) if id(x) == id(file)]
        for i in indexes:
            self._disk[i] = None

    def describe(self):
        for descriptor in self._descriptors:
            for _ in range(len(descriptor)):
                yield str(descriptor)

    def __len__(self):
        return len(self._disk)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        for descriptor in self._descriptors:
            for _ in range(descriptor.size()):
                yield descriptor
        raise StopIteration

    @classmethod
    def from_string(cls, description_string) -> "FileSystem":
        file_system = cls()
        file_index = 0
        for i, value in enumerate(description_string):
            if (i + 1) % 2 == 0:
                file_system._disk += [None] * int(value)
            else:
                file = File(file_index, size=int(value))
                file_system._disk += [file] * int(value)
                file_index += 1
        return file_system