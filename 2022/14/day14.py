import re
import itertools


def can_fall(cur_position, rock_positions):
    x, y = cur_position
    neighbors = [
        (x, y + 1),  # down
        (x - 1, y + 1),  # down-left
        (x + 1, y + 1),  # down-right
    ]
    for neighbor in neighbors:
        if neighbor not in rock_positions:
            return neighbor


def between_two_slates(a, b):
    a_x, a_y = a
    b_x, b_y = b

    a_x, b_x = sorted([a_x, b_x])
    a_y, b_y = sorted([a_y, b_y])

    x_range = range(a_x, b_x + 1)
    y_range = range(a_y, b_y + 1)

    return set(itertools.product(x_range, y_range))


def expand_coordinates(input_str: str) -> set:
    """
    Takes coordinates in form (498,4) -> (498, 6) and
    returns all cords as set of coordinates
    >>> expand_coordinates("498,4 -> 498,6")
    {(498, 5), (498, 6), (498, 4)}
    """

    parent_coords_raw = re.findall(r'\d+,\d+', input_str)

    parent_coords = []
    for raw_string in parent_coords_raw:
        x, y = raw_string.split(',')
        parent_coords.append((int(x), int(y)))

    expanded_range = []

    for coord in parent_coords:
        if expanded_range:
            prev = expanded_range[-1]
            expanded_range.extend(between_two_slates(prev, coord))
        expanded_range.append(coord)

    return set(expanded_range)


def simulate_sand(rock_positions):
    """ Drops a unit of sand until it stops and returns rest position or None """
    cur_position = (500, 0)
    max_y = max([y for x, y in rock_positions])

    while True:
        new_position = can_fall(cur_position, rock_positions)
        if new_position is None:
            return cur_position
        elif new_position[1] > max_y:
            return None
        else:
            cur_position = new_position


def cave_in(rock_positions: set):
    grains_of_sand = 0

    while True:
        sand_rest = simulate_sand(rock_positions)
        if sand_rest is None:
            return grains_of_sand
        else:
            grains_of_sand += 1
            rock_positions.add(sand_rest)


if __name__ == '__main__':
    with open('day14_input.txt', 'r') as rock_file:
        rock_positions = set().union(*[expand_coordinates(line) for line in rock_file])
    
    print(cave_in(rock_positions))
