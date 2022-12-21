def surface_area(cubes):
    """
    >>> cubes = [(2, 2, 2), (1, 2, 2), (3, 2, 2), (2, 1, 2), (2, 3, 2), (2, 2, 1), (2, 2, 3), (2, 2, 4), (2, 2, 6), (1, 2, 5), (3, 2, 5), (2, 1, 5), (2, 3, 5)]
    >>> surface_area(cubes)
    64
    """
    exposed_sides = {}
    for x, y, z in cubes:
        exposed_sides[(x, y, z)] = 6

    for x, y, z in cubes:
        if (x + 1, y, z) in cubes:
            exposed_sides[(x, y, z)] -= 1
            exposed_sides[(x + 1, y, z)] -= 1
        if (x, y + 1, z) in cubes:
            exposed_sides[(x, y, z)] -= 1
            exposed_sides[(x, y + 1, z)] -= 1
        if (x, y, z + 1) in cubes:
            exposed_sides[(x, y, z)] -= 1
            exposed_sides[(x, y, z + 1)] -= 1
    return sum(exposed_sides.values())


with open('day18_input.txt', 'r') as cube_file:
    cubes = []
    for line in cube_file:
        clean_line = line.strip().split(',')
        x,y,z = clean_line
        cubes.append(
            (int(x), int(y), int(z))
        )
    print(len(cubes))
    print(surface_area(cubes))
