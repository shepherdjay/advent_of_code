from advent_07 import find_all_dir, construct_tree

TEST_INPUT = """$ cd /
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
    example_input = TEST_INPUT
    expected = {'a': 94853, 'e': 584}

    assert find_all_dir(example_input, maxsize=10000) == expected


def test_construct_tree():
    simple_input = [
        "$ cd /",
        "$ ls",
        "dir a",
        "dir b",
        "$ cd a",
        "$ ls",
        "20 c.txt"]
    simple_tree = {'a': {'c.txt': 20}, 'b': {}}

    assert construct_tree(simple_input) == simple_tree
    assert construct_tree(TEST_INPUT) == EXAMPLE_TREE
