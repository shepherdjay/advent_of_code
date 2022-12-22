import copy
from itertools import cycle
from collections import namedtuple
from typing import Iterable
import tqdm
import math
from collections import deque

Coord = namedtuple('Coord', 'x,y')


class Rock:
    last_collision_height = -1

    def __init__(self, coordinates: set[Coord] | list[Coord], shape_name: str=None):
        if not isinstance(coordinates, set):
            coordinates = set(coordinates)
        self.coordinates = coordinates
        self.shape_name = shape_name

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __repr__(self):
        return f'Rock({list(set(self.coordinates))})'

    def collided(self, obstructions: set[Coord], compare_coords):
        if compare_coords is None:
            compare_coords = self.coordinates

        for coord in compare_coords:
            if coord in obstructions:
                return True
        return False

    def move_direction(self, direction, obstructions: set[Coord]) -> None:
        match direction:
            case '<':
                x_adjustment = - 1
            case '>':
                x_adjustment = + 1
            case _:
                raise

        new_coords = {(x + x_adjustment, y) for x, y in self.coordinates}
        if self.collided(obstructions, new_coords):
            return
        for x, y in new_coords:
            if not -1 < x < 7:
                return
        self.coordinates = new_coords

    def move_down(self, obstructions):
        new_coordinates = [(x, y - 1) for x, y in self.coordinates]
        if self.collided(obstructions, compare_coords=new_coordinates):
            return False
        self.coordinates = new_coordinates
        return True

    @classmethod
    def yield_rock(cls) -> Iterable:
        rock_iterator = cycle(
            [cls._straight_h,
             cls._plus,
             cls._right_angle,
             cls._straight_v,
             cls._block]
        )
        for rock_func in rock_iterator:
            yield rock_func(height=cls.last_collision_height + 4)

    @staticmethod
    def _straight_h(height: int):
        coords = [Coord(x, height) for x in range(2, 6)]
        return Rock(coords, shape_name='straight_h')

    @staticmethod
    def _plus(height: int):
        horiz_coord = [Coord(x, height + 1) for x in range(2, 5)]
        vertical_coord = [Coord(3, y) for y in range(height, height + 3)]
        return Rock(horiz_coord + vertical_coord, shape_name='plus')

    @staticmethod
    def _right_angle(height: int):
        horiz_coord = [Coord(x, height) for x in range(2, 5)]
        vert_coord = [Coord(4, y) for y in range(height, height + 3)]
        return Rock(horiz_coord + vert_coord, shape_name='right_angle')

    @staticmethod
    def _straight_v(height: int):
        coord = [Coord(2, y) for y in range(height, height + 4)]
        return Rock(coord, shape_name='straight_v')

    @staticmethod
    def _block(height: int):
        coord = [
            Coord(2, height),
            Coord(2, height + 1),
            Coord(3, height),
            Coord(3, height + 1)
        ]
        return Rock(coord, shape_name='block')


def solver(jets: Iterable, max_rocks, lcm=None):
    num_rocks = 0
    floor = set(Coord(x, -1) for x in range(0, 7))
    obstructions = deque(maxlen=1000)
    obstructions.extendleft(floor)

    # Amys Idea: Look for Cycle
    # we need the lcm of the jet pattern and rock pattern - passed into function
    # this will tell us whether we are starting the same rock at the same jet pattern.
    if lcm is None:
        lcm = max_rocks + 1  # never exit for cycle
    queue_length = 32
    rock_dist_queue = deque(maxlen=queue_length)
    compare_queue = None

    with tqdm.tqdm(total=max_rocks) as pbar:
        for rock in Rock.yield_rock():
            # Before we drop another rock we check for cycle:
            if num_rocks % lcm == 0 and num_rocks != 0:
                cycle_height = max(y for x, y in obstructions) + 1
                cycles_left = max_rocks // num_rocks
            if compare_queue is not None and (num_rocks - queue_length) % lcm == 0 and num_rocks > ( lcm * 3 ):
                if rock_dist_queue == compare_queue:
                    # We are in cycle:
                    print(f'Exiting for Cycle after dropping {num_rocks} out of {max_rocks}')
                    print(f'Cycle Detection Info: cycle_height {cycle_height}, cycles_left {cycles_left}')
                    return cycle_height * cycles_left
            if num_rocks == max_rocks:
                break

            rock_dist = 0
            for direction in jets:
                rock.move_direction(direction, obstructions)
                if rock.move_down(obstructions):
                    rock_dist += 1
                    continue
                else:
                    break
            rock_dist_queue.append(rock_dist)
            stop_height = max(y for x, y in rock.coordinates)
            Rock.last_collision_height = max(Rock.last_collision_height, stop_height)
            obstructions.extendleft(rock.coordinates)
            num_rocks += 1

            if num_rocks == (lcm * 2) + queue_length:
                compare_queue = copy.deepcopy(rock_dist_queue)

            pbar.update()

    return max(y for x, y in obstructions) + 1


def part1(char_string, cycle_check=False):
    jets = cycle(char_string)
    if cycle_check:
        lcm = math.lcm(5, len(char_string))
        return solver(jets, max_rocks=2022, lcm=lcm)
    else:
        return solver(jets, max_rocks=2022)


def part2(char_string):
    jets = cycle(char_string)
    lcm = math.lcm(5, len(char_string))
    print(f'LCM Activated:: {lcm}')
    return solver(jets, max_rocks=1_000_000_000_000, lcm=lcm)


if __name__ == '__main__':
    with open('day17_input.txt') as elfile:
        char_string = elfile.readline().strip()

    # print(part1(char_string))
    print(part2(char_string))
