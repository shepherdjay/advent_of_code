from advent_2024_04 import solve_puzzle, get_neighbor_coord, get_neighbors

EXAMPLE = '''
..X...
.SAMX.
.A..A.
XMAS.S
.X....
'''

EXAMPLE_AS_GRID = [row for row in EXAMPLE.split('\n') if row]

def test_get_neighbor_coord():
    row, column = 3, 2
    assert get_neighbor_coord(row, column) == set([
        (2,2),(4,2),(3,1),(3,3)
    ])

def test_get_neighbors():
    coord = (3,2)
    assert get_neighbors(coord, EXAMPLE_AS_GRID) == set([
        ('M',(3,1)),
        ('.',(2,2)),
        ('S',(3,3)),
        ('.',(4,2))
    ])

def test_solve_puzzle():
    assert solve_puzzle(EXAMPLE) == 18