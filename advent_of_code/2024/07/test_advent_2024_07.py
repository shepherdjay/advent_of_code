import pytest
from hypothesis import given, assume, strategies as st, settings
import random

import advent_2024_07 as advent

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


@st.composite
def generate_positive_example(draw, max_size: int, min_value: int = 1) -> tuple[int, list[int]]:
    values = draw(
        st.lists(st.integers(min_value=min_value, max_value=1000), min_size=2, max_size=max_size)
    )
    total = values[0]
    for n in values[1:]:
        match draw(st.sampled_from(["multiply", "add"])):
            case "multiply":
                total *= n
            case "add":
                total += n

    return total, values


@st.composite
def generate_negative_example(draw: st.DrawFn, max_size: int) -> tuple[int, list[int]]:
    _, values = draw(generate_positive_example(max_size=max_size, min_value=2))
    total = draw(st.sampled_from(values))

    return total, values


@st.composite
def generate_full_example(
    draw: st.DrawFn, max_size_per_example: int, max_report_size: int = 100
) -> str:
    positive_examples = []
    negative_examples = []
    report = []

    report_size = draw(st.integers(min_value=1, max_value=max_report_size))
    for _ in range(report_size):
        match draw(st.sampled_from(["positive", "negative"])):
            case "positive":
                example = draw(generate_positive_example(max_size=max_size_per_example))
                positive_examples.append(example)
            case "negative":
                example = draw(generate_positive_example(max_size=max_size_per_example))
                negative_examples.append(example)
        report.append(example)

    puzzle_input = ""
    for total, value_list in report:
        puzzle_input += f"{total}: {' '.join([str(x) for x in value_list])}\n"

    expected_result = sum([x for x, _ in positive_examples])

    return expected_result, puzzle_input


def test_solve_puzzle():
    assert advent.solve_puzzle(EXAMPLE) == 3749


def test_solve_layer_simple():
    target_number = 190
    values = advent.deque([10, 19])

    assert advent.solve_layer(target=target_number, values=values)


def test_solve_layer_more():
    target = 3267
    values = advent.deque([81, 40, 27])

    assert advent.solve_layer(target=target, values=values)


@given(generate_positive_example(max_size=5))
def test_solve_layer_hypyothesis_positive(example):
    target, values = example
    values = advent.deque(values)

    assert advent.solve_layer(target=target, values=values)


@given(generate_negative_example(max_size=5))
def test_solve_layer_hypyothesis_negative(example):
    target, values = example
    values = advent.deque(values)

    assert not advent.solve_layer(target=target, values=values)


@settings(max_examples=5)  # Generating these is computationally expensive
@given(generate_full_example(max_size_per_example=4))
def test_solve_hypothesis(sample_report):
    expected, puzzle_input = sample_report

    assert advent.solve_puzzle(puzzle_input) == expected
