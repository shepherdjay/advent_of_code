from hypothesis import given
from strategies import positive_example, negative_example, full_report

import advent_2024_07 as advent
import pytest
import os

EXAMPLE = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def test_solve_puzzle():
    assert advent.solve_puzzle(EXAMPLE) == 3749


def test_solve_puzzle_concat():
    assert advent.solve_puzzle(EXAMPLE, concat=True) == 11387


@pytest.mark.parametrize(
    "target,numbers,result",
    [
        (156, [15, 6], True),
        (7290, [6, 8, 6, 15], True),
        (161011, [16, 10, 13], False),
    ],
)
def test_solve_layer_concat(target, numbers, result):
    assert advent.solve_layer(target=target, queue=advent.deque(numbers), concat=True) is result


@pytest.mark.parametrize(
    "target,numbers,result",
    [
        (190, [10, 19], True),
        (3267, [81, 40, 27], True),
    ],
)
def test_solve_layer(target, numbers, result):
    assert advent.solve_layer(target=target, queue=advent.deque(numbers)) is result


@given(positive_example(max_size=5))
def test_solve_layer_hypyothesis_positive(example):
    target, values = example
    values = advent.deque(values)

    assert advent.solve_layer(target=target, queue=values)


@given(negative_example(max_size=5))
def test_solve_layer_hypyothesis_negative(example):
    target, values = example
    values = advent.deque(values)

    assert not advent.solve_layer(target=target, queue=values)


@given(full_report(max_size_per_example=5, max_report_size=10))
def test_solve_hypothesis(sample_report):
    expected, puzzle_input, *_ = sample_report

    assert advent.solve_puzzle(puzzle_input) == expected
