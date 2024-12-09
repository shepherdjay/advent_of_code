import y2024day09 as advent


def test_filesystem():
    input = '123'

    assert advent.construct_filesystem(input) == ['0','.','.','1','1','1']

def test_solve_example():
    input = '2333133121414131402'
    assert advent.solve_puzzle(input) == 1928


def test_filesystem_class_add():
    filesystem = advent.FileSystem(disk_size=5)
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, loc=2)

    assert list(filesystem.describe()) == ['.', '.', 50, 50, '.']

def test_filesystem_class_add_fragment():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, 1, None]
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, loc=2)

    assert list(filesystem.describe()) == [1, 1, 50, 1, 50]
    assert filesystem.fragmented