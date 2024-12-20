from advent_2024day19 import solve_puzzle, try_combinations
import pytest
import hypothesis.strategies as st
from hypothesis import given
import random

MAIN_EXAMPLE = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

LOWER_ALPHABET = st.characters(min_codepoint=97, max_codepoint=122)


@st.composite
def true_example(draw):
    towels_list = draw(
        st.lists(st.text(alphabet=LOWER_ALPHABET, min_size=1, max_size=10), min_size=2, max_size=10)
    )

    pattern = []
    for _ in range(10):
        pattern.append(draw(st.sampled_from(towels_list)))

    return "".join(pattern), towels_list


@st.composite
def false_example(draw):
    towels_list = draw(
        st.lists(st.text(alphabet=LOWER_ALPHABET, min_size=1, max_size=10), min_size=2, max_size=10)
    )
    char_not_present = draw(
        st.characters(
            min_codepoint=97,
            max_codepoint=122,
            blacklist_characters=[char for towel in towels_list for char in towel],
        )
    )

    pattern = []
    for _ in range(10):
        pattern.append(draw(st.sampled_from(towels_list)))
        pattern.append(char_not_present)

    return "".join(pattern), towels_list


@pytest.mark.parametrize(
    "pattern,possible",
    [
        ("brwrr", True),
        ("bggr", True),
        ("gbbr", True),
        ("rrbgbr", True),
        ("ubwu", False),
        ("bwurrg", True),
        ("brgr", True),
        ("bbrgwb", False),
    ],
)
def test_try_combinations(pattern, possible):
    available_towels = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
    assert try_combinations(available_towels, pattern) is possible


def test_solve_puzzle():
    assert solve_puzzle(MAIN_EXAMPLE) == 6


@given(true_example())
def test_hypothesis_try_combinations_true(example):
    pattern, towels = example
    assert try_combinations(towels, pattern) is True


@given(false_example())
def test_hypothesis_try_combinations_false(example):
    pattern, towels = example
    assert try_combinations(towels, pattern) is False
