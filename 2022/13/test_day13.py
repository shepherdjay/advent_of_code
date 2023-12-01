import pytest
from day13 import comparator, process_file, process_file_v2


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], True),
        ([[1], [2, 3, 4]], [[1], 4], True),
        ([9], [[8, 7, 6]], False),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], True),
        ([7, 7, 7, 7], [7, 7, 7], False),
        ([], [3], True),
        ([[[]]], [[]], False),
        (
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            False,
        ),
    ],
)
def test_comparator(a, b, expected):
    assert comparator(a, b) == expected


def test_process_file():
    assert process_file("test_day13_input.txt") == 13


def test_process_file_v2():
    assert process_file_v2("test_day13_input.txt") == 140
