import re

def expand_coordinates(input_str: str) -> list:
    """ 
    Takes coordinates in form (498,4) -> (498, 6) and
    returns all cords as list.
    >>> expand_coordinates("498,4 -> 498,6")
    [(498, 4), (498, 5), (498, 6)]
    """

    parent_coords = re.findall(r'\(\d+,\d+\)', input_str)

    expanded_range = []

    for coord in parent_coords:
        if expanded_range:
            x_prev, y_prev = expanded_range[-1]
            x_new, y_new = coord
            all_combinations = [x, y for x in range(x_prev, x_new) for y in range(y_prev, y_new)]
            expanded_range.extend(all_combinations)
        expanded_range.append(coord)

    return expanded_range
        

