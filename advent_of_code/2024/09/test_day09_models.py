import pytest
import day09_models as advent
from typing import Generator

@pytest.fixture()
def bare_filesystem() -> Generator[advent.FileSystem]:
    filesystem = advent.FileSystem()
    filesystem.descriptors = set([
        advent.FileBlock(size=1, start_idx=0, file_ptr=advent.File(name = 0, size = 0)),
        advent.FreeBlock(size=2, start_idx=1),
        advent.FileBlock(size=3, start_idx=3, file_ptr=advent.File(name=1, size=3))
    ])
    yield filesystem

def test_filesystem_class(bare_filesystem):
    assert list(bare_filesystem.describe()) == ['0', ".", ".", '1', '1', '1']

def test_filesystem_class_from_string():
    input = "123"
    assert list(advent.FileSystem.from_string(input).describe()) == ["0", ".", ".", "1", "1", "1"]

def test_filesystem_class_add():
    filesystem = advent.FileSystem(disk_size=5)
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, loc=2)

    assert list(filesystem.describe()) == [".", ".", "50", "50", "."]


def test_filesystem_class_add_fragment():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, 1, None]
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, loc=2)

    assert list(filesystem.describe()) == ["1", "1", "50", "1", "50"]


def test_filesystem_class_add_dnf():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, 1, None, None]
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, dnf=True)
    assert list(filesystem.describe()) == ["1", "1", ".", "1", "50", "50"]


def test_filesystem_find_free_space():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, 1, None, None]

    assert filesystem.find_free_space(2) == 4


def test_filesystem_find_free_space_start():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, None, None, None]

    assert filesystem.find_free_space(2, 4) == 4


def test_filesystem_delete():
    filesystem = advent.FileSystem(disk_size=3)

    myfile = advent.File(50, 2)
    myfile2 = advent.File(30, 1)

    filesystem.add_file(myfile)
    filesystem.add_file(myfile2)

    assert filesystem._disk == [myfile, myfile, myfile2]

    filesystem.delete_file(myfile)
    assert filesystem._disk == [None, None, myfile2]