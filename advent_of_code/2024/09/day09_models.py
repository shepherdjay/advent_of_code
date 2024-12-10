from dataclasses import dataclass
from typing import Generator

@dataclass
class File:
    name: int
    size: int

    def __str__(self):
        return f"{self.name}"

    def __hash__(self):
        return hash(self.name)

@dataclass(frozen=True)
class Block:
    size: int
    start_idx: int

    def __len__(self):
        return self.size

@dataclass(frozen=True)
class FileBlock(Block):
    file_ptr: File
    
    def __str__(self):
        return str(self.file_ptr)

@dataclass(frozen=True)
class FreeBlock(Block): 
    def __str__(self):
        return '.'

class FileSystem:
    def __init__(self, disk_size: int = 0):
        self._disk = [None for _ in range(disk_size)]
        self.descriptors = set( [FreeBlock(disk_size, start_idx=0)] )

    def find_free_space(self, desired_space: int, _start_idx=0) -> FreeBlock|None:
        for block in self.descriptors:
            # if descriptor.start_idx < _start_idx > descriptor.start_idx + descriptor.size:
            #     continue
            if isinstance(block, FreeBlock) and len(block) >= desired_space:
                return block

    def add_file(self, file: File, loc: int = 0, dnf=False):
        space_needed = file.size
        
        free_block = self.find_free_space(space_needed, _start_idx=loc)
        if free_block is None:
            raise RuntimeError("No Space")
        
        file_block = FileBlock(size=space_needed, start_idx=free_block.start_idx, file_ptr=file)
        remaining = free_block.size - file_block.size
        if free_block.size > file_block.size:
            new_free_block = FreeBlock(size=remaining, start_idx=file_block.start_idx + file_block.size)
        else:
            new_free_block = None 
        
        self.descriptors[file_block.start_idx] = file_block
        if new_free_block:
            print(new_free_block.start_idx)
            self.descriptors[new_free_block.start_idx] = new_free_block

    def delete_file(self, file: File):
        indexes = [i for i, x in enumerate(self._disk) if id(x) == id(file)]
        for i in indexes:
            self._disk[i] = None

    def describe(self):
        ordered = sorted(self.descriptors, key = lambda x : x.start_idx)
        for descriptor in ordered:
            for _ in range(len(descriptor)):
                yield str(descriptor)

    def __len__(self):
        return len(self._disk)
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Generator[FreeBlock|FileBlock]:
        for descriptor in self.descriptors:
            yield descriptor
        raise StopIteration
    
    def __getitem__(self, i):
        for block in self:
            start_idx, end_idx = block.start_idx + block.size
            if start_idx <= i < end_idx:
                return block
    


    @classmethod
    def from_string(cls, description_string) -> "FileSystem":
        file_system = cls()
        file_index = 0
        system_idx = 0
        for i, value in enumerate(description_string):
            if (i + 1) % 2 == 0:
                descriptor = FreeBlock(size=int(value), start_idx = system_idx)
            else:
                file = File(name=file_index, size=int(value))
                descriptor = FileBlock(size=file.size, start_idx=system_idx, file_ptr=file)
                file_index += 1
            file_system.descriptors.add(descriptor)
            system_idx += len(descriptor)
        return file_system