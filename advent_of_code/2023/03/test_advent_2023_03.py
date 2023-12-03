from advent_2023_03 import process_schematic, find_neighbors, extract_numbers_start_end


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


def test_process_schematic():
    assert process_schematic(EXAMPLE_SCHEMATIC.splitlines()) == 4361


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
    sample_row = ["467..114.."]
    expected = [(467, 0, 2), (114, 5, 7)]
