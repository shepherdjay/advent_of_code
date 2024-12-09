import y2024day09 as advent


def test_filesystem():
    input = "123"

    assert advent.construct_filesystem(input) == ["0", ".", ".", "1", "1", "1"]

def test_filesystem_class():
    input = "123"

    assert list(advent.FileSystem.from_string(input).describe()) == ["0", ".", ".", "1", "1", "1"]


def test_solve_example():
    input = "2333133121414131402"
    assert advent.solve_puzzle(input) == 1928


def test_filesystem_class_add():
    filesystem = advent.FileSystem(disk_size=5)
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, loc=2)

    assert list(filesystem.describe()) == [".", ".", 50, 50, "."]


def test_filesystem_class_add_fragment():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, 1, None]
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, loc=2)

    assert list(filesystem.describe()) == [1, 1, 50, 1, 50]


def test_filesystem_class_add_dnf():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, 1, None, None]
    file = advent.File(name=50, size=2)

    filesystem.add_file(file, dnf=True)
    assert list(filesystem.describe()) == [1, 1, ".", 1, 50, 50]


def test_filesystem_find_free_space_base_case():
    filesystem = advent.FileSystem()
    filesystem._disk = [None]

    assert filesystem.find_free_space(1) == 0


def test_filesystem_find_free_space():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, 1, None, None]

    assert filesystem.find_free_space(2) == 4


def test_filesystem_find_free_space_start():
    filesystem = advent.FileSystem()
    filesystem._disk = [1, 1, None, None, None, None]

    assert filesystem.find_free_space(2, 4) == 4
