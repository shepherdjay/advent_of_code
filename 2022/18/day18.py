from collections import deque, namedtuple

EXAMPLE_CUBES = [(2, 2, 2), (1, 2, 2), (3, 2, 2), (2, 1, 2), (2, 3, 2), (2, 2, 1), (2, 2, 3), (2, 2, 4), (2, 2, 6),
                 (1, 2, 5), (3, 2, 5), (2, 1, 5), (2, 3, 5)]

Coord = tuple[int, int, int]

Dimensions = namedtuple('Dimensions', 'x_min,x_max,y_min,y_max,z_min,z_max')


def surface_area(cubes):
    """
    >>> surface_area(EXAMPLE_CUBES)
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


def get_dimensions(array):
    x_values = [i[0] for i in array]
    y_values = [i[1] for i in array]
    z_values = [i[2] for i in array]
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)
    min_z, max_z = min(z_values), max(z_values)
    return Dimensions(min_x, max_x, min_y, max_y, min_z, max_z)


def explore_exterior(cubes):
    """
    >>> explore_exterior({(1, 1, 1), (2, 1, 1), (1, 2, 1), (2, 2, 1), (1, 1, 2), (2, 1, 2), (1, 2, 2), (2, 2, 2)})
    24
    >>> explore_exterior(EXAMPLE_CUBES)
    58
    """
    # Find the dimensions of the object
    cubes_dim = get_dimensions(cubes)

    # Create a 3D box one larger than the dimensions of the object
    box = [(x, y, z)
           for z in range(cubes_dim.z_min - 1, cubes_dim.z_max + 2)
           for y in range(cubes_dim.y_min - 1, cubes_dim.y_max + 2)
           for x in range(cubes_dim.x_min - 1, cubes_dim.x_max + 2)]

    # Find the bottom left corner of the 3D box
    box_dim = get_dimensions(box)

    visited = set()
    queue = deque([(box_dim.x_min, box_dim.y_min, box_dim.z_min)])
    object_surface_area = 0

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        neighbors = calculate_neighbors(node)
        for neighbor in neighbors:
            if neighbor in cubes:
                object_surface_area += 1
                continue
            if neighbor[0] < box_dim.x_min or neighbor[0] > box_dim.x_max:
                continue
            if neighbor[1] < box_dim.y_min or neighbor[1] > box_dim.y_max:
                continue
            if neighbor[2] < box_dim.z_min or neighbor[2] > box_dim.z_max:
                continue
            queue.append(neighbor)
    return object_surface_area


def calculate_neighbors(cube):
    """
    >>> len(list(calculate_neighbors((2,2,2))))
    6
    """
    # Given 1x1x1 cube calculate coordinates for all six neighbors
    x, y, z = cube
    offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    return ((x + dx, y + dy, z + dz) for dx, dy, dz in offsets)


if __name__ == '__main__':
    with open('day18_input.txt', 'r') as cube_file:
        puzzle = []
        for line in cube_file:
            clean_line = line.strip().split(',')
            x, y, z = clean_line
            puzzle.append(
                (int(x), int(y), int(z))
            )

        for cubes in [EXAMPLE_CUBES, puzzle]:
            total_surface_area = surface_area(cubes)
            exposed = explore_exterior(cubes)
            print(
                f"For {len(cubes)} cubes. The total surface area is {total_surface_area}. The exposed surface area is {exposed}")
