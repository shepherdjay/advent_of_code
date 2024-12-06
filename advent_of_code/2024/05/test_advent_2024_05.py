import pytest
from advent_2024_05 import split_input, solve_puzzle, check_printjob

EXAMPLE = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def test_split_input():
    simple_split = """
47|53

97,12,42
"""
    expected_dict = {47: [53]}
    expected_list = [[97, 12, 42]]

    actual_dict, actual_list = split_input(simple_split)

    assert actual_dict == expected_dict
    assert actual_list == expected_list


def test_solve_puzzle():
    assert solve_puzzle(EXAMPLE) == 143

def test_check_printjob_ok():
    rules = {47: [53]}
    printjob = [47,95,53]

    assert check_printjob(printjob, rules) is True

def test_check_printjob_bad():
    rules = {47: [53]}
    printjob = [53,95,47]

    assert check_printjob(printjob, rules) is False