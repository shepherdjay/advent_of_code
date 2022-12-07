from advent_07 import find_all_dir, construct_tree
from xml.etree import ElementTree as ET


SIMPLE = [
    "$ cd /",
    "$ ls",
    "dir a",
    "dir b",
    "$ cd a",
    "$ ls",
    "20 c.txt"]

EXAMPLE_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
EXAMPLE_TREE = {
    'a': {
        'e': {
            'i': 584
        },
        'f': 29116,
        'g': 2557,
        'h.lst': 62596
    },
    'b.txt': 14848514,
    'c.dat': 8504156,
    'd': {
        'j': 4060174,
        'd.log': 8033020,
        'd.ext': 5626152,
        'k': 7214296
    }
}


def test_find_all_dir():
    example_input = SIMPLE
    expected_simple = {'a': 20, 'c': 20}

    assert find_all_dir(example_input, maxsize=10000) == expected_simple


def test_construct_tree():
    simple_tree = {'a': {'c.txt': 20}, 'b': {}}

    simple_result = construct_tree(SIMPLE)

    assert simple_result == simple_tree
