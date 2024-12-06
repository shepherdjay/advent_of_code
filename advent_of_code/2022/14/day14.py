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
    """
    Given two (x,y) coordinates where only x or y varies
    Return the set of those coordinates as well as all points between them.
    """
    a, b = sorted([a, b])

    x_range = range(a[0], b[0] + 1)
    y_range = range(a[1], b[1] + 1)

    return set(itertools.product(x_range, y_range))


def expand_coordinates(input_str: str) -> set:
    """
    Takes coordinates in form (498,4) -> (498, 6) and
    returns all cords as set of coordinates
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


def simulate_sand(rock_positions, max_y: int):
    """Drops a unit of sand until it stops and returns rest position or None"""
    cur_position = (500, 0)

    while True:
        new_position = can_fall(cur_position, rock_positions)
        if new_position is None:
            return cur_position
        elif new_position[1] > max_y:
            return None
        else:
            cur_position = new_position


def cave_in(rock_positions: set, floor=False):
    start_position = (500, 0)
    grains_of_sand = 0

    if floor:
        # Populate initial floor
        floor_y = max([y for _, y in rock_positions]) + 2
        floor_x_min = min([x for x, _ in rock_positions]) - 1
        floor_x_max = max([x for x, _ in rock_positions]) + 1
        floor = between_two_slates((floor_x_min, floor_y), (floor_x_max, floor_y))
        rock_positions.update(floor)

    max_y = max([y for _, y in rock_positions])

    while True:
        if floor:
            floor_x_min -= 1
            floor_x_max += 1
            rock_positions.add((floor_x_min, floor_y))
            rock_positions.add((floor_x_max, floor_y))

        sand_rest = simulate_sand(rock_positions, max_y=max_y)
        if sand_rest is None:
            return grains_of_sand
        elif sand_rest == start_position:
            return grains_of_sand + 1
        else:
            grains_of_sand += 1
            rock_positions.add(sand_rest)


if __name__ == '__main__':
    with open('day14_input.txt', 'r') as rock_file:
        rock_positions = set().union(*[expand_coordinates(line) for line in rock_file])

    # print(cave_in(rock_positions))
    print(cave_in(rock_positions, floor=True))
