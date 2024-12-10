from dataclasses import dataclass
from typing import Generator
from collections.abc  import MutableSequence

@dataclass
class File:
    name: int
    size: int

    def __str__(self):
        return f"{self.name}"

    def __hash__(self):
        return hash(self.name)

@dataclass
class Block:
    size: int
    start_idx: int

    def __len__(self):
        return self.size
    
    @property
    def end_idx(self):
        return self.start_idx + self.size - 1

@dataclass
class FileBlock(Block):
    file_ptr: File
    
    def __str__(self):
        return str(self.file_ptr)

@dataclass
class FreeBlock(Block): 
    def __str__(self):
        return '.'
    
class Disk(MutableSequence):
    def __init__(self, disk_size: int = 0):
        self.disk_size = disk_size

        if self.disk_size == 0:
            self.blocks = []
        else:
            self.blocks = FreeBlock(size=disk_size, start_idx=0)
    
    def __getitem__(self, idx):
        print(f'get {idx}')
        for block in self.blocks:
            print(block.start_idx, block.end_idx, block.__repr__())
            if block.start_idx <= idx < block.end_idx:
                return block
        raise IndexError(f"Index {idx} out of range")
    
    def __setitem__(self, idx, block: Block):
        print('set')
        for i, b in enumerate(self.blocks):
            if b.start_idx <= idx < b.end_idx:
                self.blocks[i] = block
                return
        raise IndexError(f"Index {idx} out of range")
    
    def __delitem__(self, idx):
        print('del')
        raise NotImplementedError
        for i, block in enumerate(self):
            if block.start_idx <= idx < block.end_idx:
                pass

    def __len__(self):
        print('len')
        return len(self.blocks)
    
    def insert(self, i, block):
        raise NotImplementedError


        

class FileSystem:
    def __init__(self, disk_size: int = 0):
        self._disk = [None for _ in range(disk_size)]
        self.disk = Disk(disk_size=disk_size)

    def find_free_space(self, desired_space: int, _start_idx=0) -> FreeBlock|None:
        for block in self.disk:
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
        
        self[file_block.start_idx] = file_block
        if new_free_block:
            print(new_free_block.start_idx)
            self[new_free_block.start_idx] = new_free_block

    def delete_file(self, file: File):
        indexes = [i for i, x in enumerate(self._disk) if id(x) == id(file)]
        for i in indexes:
            self._disk[i] = None

    def describe(self):
        for block in self.disk:
            yield str(block)


    @classmethod
    def from_string(cls, description_string) -> "FileSystem":
        file_index = 0
        system_idx = 0
        blocks = []
        for i, value in enumerate(description_string):
            if (i + 1) % 2 == 0:
                blocks.append(FreeBlock(size=int(value), start_idx = system_idx))
            else:
                file = File(name=file_index, size=int(value))
                blocks.append(FileBlock(size=file.size, start_idx=system_idx, file_ptr=file))
                file_index += 1
            system_idx += 1
        
        file_system = cls(disk_size = blocks[-1].end_idx)
        print(blocks)
        file_system.disk.blocks = blocks
        return file_system