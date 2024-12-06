from advent_2023_03 import (
    find_neighbors,
    extract_numbers_start_end,
    process_schematic,
    process_gears,
)
import pytest

EXAMPLE_SCHEMATIC = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


@pytest.mark.parametrize(
    'schematic,result',
    [
        (EXAMPLE_SCHEMATIC, 4361),
        ('.1.\r1*1\r.1.', 4),
        ('1.1\r.*.\r1.1' '', 4),
        ('111\r1@1\r111', 224),
        ('12.23\r..*..\r......', 35),
    ],
)
def test_process_schematic(schematic, result):
    assert process_schematic(schematic.splitlines()) == result


@pytest.mark.parametrize(
    'schematic,result',
    [
        (EXAMPLE_SCHEMATIC, 467835),
        ('.1.\r1*1\r.1.', 0),
        ('.1.\r.*1\r...', 1),
        ('2..\r.*.\r..2', 4),
        ('12.23\r..*..\r......', 276),
        ('13...4\r.*....\r.....', 0),
    ],
)
def test_process_gears(schematic, result):
    assert process_gears(schematic.splitlines()) == result


def test_find_neighbors():
    exp_neighbors = {
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 2),
        (1, 4),
        (2, 2),
        (2, 3),
        (2, 4),
    }
    assert find_neighbors((1, 3)) == exp_neighbors


def test_extract_numbers_start_end():
    sample_row = '467..114..'
    expected = [(467, 0, 3), (114, 5, 8)]
    assert extract_numbers_start_end(sample_row) == expected
