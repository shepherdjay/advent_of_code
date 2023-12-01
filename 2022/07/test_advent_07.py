from advent_07 import find_all_dir_sizes, construct_tree, ElfDirectory
import pytest
import os

SIMPLE = ["$ cd /", "$ ls", "dir a", "dir b", "$ cd a", "$ ls", "20 c.txt"]

with open(os.path.join(os.path.dirname(__file__), "test_advent_07_input.txt"), "r") as testfile:
    EXAMPLE_INPUT = [line.strip() for line in testfile]

EXAMPLE_TREE = {
    "a": {"e": {"i": 584}, "f": 29116, "g": 2557, "h.lst": 62596},
    "b.txt": 14848514,
    "c.dat": 8504156,
    "d": {"j": 4060174, "d.log": 8033020, "d.ext": 5626152, "k": 7214296},
}


@pytest.mark.parametrize(
    "test_input,result",
    [(EXAMPLE_INPUT, {"a": 94853, "e": 584}), (SIMPLE, {"a": 20, "b": 0, "/": 20})],
)
def test_find_all_dir(test_input, result):
    assert find_all_dir_sizes(test_input, maxsize=100_000) == result


@pytest.mark.parametrize(
    "test_input,expected_tree",
    [(SIMPLE, {"a": {"c.txt": 20}, "b": {}}), (EXAMPLE_INPUT, EXAMPLE_TREE)],
)
def test_construct_tree(test_input, expected_tree):
    result_dirs = construct_tree(test_input)
    assert result_dirs[0].to_dict() == expected_tree


def test_elf_directory_nested_size():
    elfdir = ElfDirectory(name="test")
    elfdir.add_directory("childdir").add_file("childdirfile", size=100)
    elfdir.add_file("file1", size=200)

    assert elfdir.get_size() == 300


def test_elf_directory_multiple_files():
    elfdir = ElfDirectory(name="test")
    elfdir.add_file("file1", 500)
    elfdir.add_file("file2", 1000)

    assert elfdir.get_size() == 1500
