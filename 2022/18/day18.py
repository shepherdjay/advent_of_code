from collections import deque
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

EXAMPLE_CUBES = [(2, 2, 2), (1, 2, 2), (3, 2, 2), (2, 1, 2), (2, 3, 2), (2, 2, 1), (2, 2, 3), (2, 2, 4), (2, 2, 6),
                 (1, 2, 5), (3, 2, 5), (2, 1, 5), (2, 3, 5)]

Coord = tuple[int, int, int]


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

def visualization(box):
    x_values = [cube[0] for cube in box]
    y_values = [cube[1] for cube in box]
    z_values = [cube[2] for cube in box]
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)
    min_z, max_z = min(z_values), max(z_values)

    axes = [
        max_x - min_x,
        max_y - min_y,
        max_z - min_z
    ]

    # Create Data
    data = [np.ones(cube, dtype=np.bool_) for cube in cubes]

    # Control Transparency
    alpha = 0.9

    # Control colour
    colors = np.empty(axes + [4], dtype=np.float32)

    colors[:] = [0, 0, 0, alpha]  # red

    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Voxels is used to customizations of the
    # sizes, positions and colors.
    ax.voxels(data, facecolors=colors)
    plt.show()

def explore_exterior(cubes):
    """
    >>> explore_exterior(EXAMPLE_CUBES)
    1
    """
    # Find the dimensions of the object
    x_values = [cube[0] for cube in cubes]
    y_values = [cube[1] for cube in cubes]
    z_values = [cube[2] for cube in cubes]
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)
    min_z, max_z = min(z_values), max(z_values)

    # Create a 3D box one larger than the dimensions of the object
    box = [(x, y, z) for z in range(min_z, max_z + 1) for y in range(min_y, max_y +1) for x in range(min_x, max_x + 1)]
    visualization(cubes)

    # Find the bottom left corner of the 3D box
    x_values = [cube[0] for cube in box]
    y_values = [cube[1] for cube in box]
    z_values = [cube[2] for cube in box]
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)
    min_z, max_z = min(z_values), max(z_values)

    visited = set()
    queue = deque([(min_x, min_y, min_z)])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node not in cubes:
            neighbors = calculate_neighbors(node)
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in cubes:
                    queue.append(neighbor)

    # Calculate the surface area of the object by counting the number of exposed cells
    exterior_area = 2 * ((max_x - min_x + 1) * (max_y - min_y + 1) + (max_x - min_x + 1) * (max_z - min_z + 1) + (
                max_y - min_y + 1) * (max_z - min_z + 1))

    return exterior_area

def calculate_neighbors(cube):
    """
    >>> len(list(calculate_neighbors((2,2,2))))
    6
    """
    # Given 1x1x1 cube calculate coordinates for all six neighbors
    x, y, z = cube
    offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    return ((x + dx, y + dy, z + dz) for dx, dy, dz in offsets)


with open('day18_input.txt', 'r') as cube_file:
    puzzle = []
    for line in cube_file:
        clean_line = line.strip().split(',')
        x, y, z = clean_line
        puzzle.append(
            (int(x), int(y), int(z))
        )

    simplest = {
        (1, 1, 1), (2, 1, 1), (1, 2, 1), (2, 2, 1), (1, 1, 2), (2, 1, 2), (1, 2, 2), (2, 2, 2)
    }

    for cubes in [simplest]:
        total_surface_area = surface_area(cubes)
        exposed = explore_exterior(cubes)
        print(f"For {len(cubes)} cubes. The total surface area is {total_surface_area}. The exposed surface area is {exposed}")
