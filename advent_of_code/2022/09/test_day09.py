from day09 import follow_the_leader, Point

EXAMPLE_INPUT = [
    ('R', 4),
    ('U', 4),
    ('L', 3),
    ('D', 1),
    ('R', 4),
    ('D', 1),
    ('L', 5),
    ('R', 2),
]


def test_follow_the_leader():
    head = Point(1000, 1000)
    tail = Point(1000, 1000, head=head)
    assert follow_the_leader(EXAMPLE_INPUT, head=head, tails=[tail]) == 13


def test_reduce_distance():
    head = Point(1, 1)
    tail = Point(3, 3, head=head)

    tail.reduce_distance()

    assert tail.x, tail.y == (2, 2)
