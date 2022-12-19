import re
import itertools
from tqdm import tqdm


class Sensor:
    def __init__(self, location: tuple[int, int], beacon: tuple[int, int]):
        self.location = location
        self.beacon = beacon
        self.beacon_mdist = self.m_dist(location, beacon)

        self.x_min = self.location[0] - self.beacon_mdist
        self.x_max = self.location[0] + self.beacon_mdist
        self.y_min = self.location[1] - self.beacon_mdist
        self.y_max = self.location[1] + self.beacon_mdist

    @staticmethod
    def m_dist(a, b):
        loc_x, loc_y = a
        beac_x, beac_y = b
        return abs(loc_x - beac_x) + abs(loc_y - beac_y)

    def not_beacon(self, x: tuple[int, int]) -> bool:
        """ Given a location return True if it can't be a beacon according to this sensor """
        if x != self.beacon and self.in_sensor_net(x):
            return True
        return False

    def in_sensor_net(self, x: tuple[int, int]) -> bool:
        """ Given a location return True if location is inside sensor net """
        return self.m_dist(x, self.location) <= self.beacon_mdist

    def non_beacon_locations(self) -> set[tuple[int, int]]:
        """ Returns a set of coordinates that definitely don't contain a beacon """
        grid_coordinates = set(itertools.product(
            range(self.x_min, self.x_max + 1), range(self.y_min, self.y_max + 1)
        ))

        pruned_set = set(
            x for x in grid_coordinates if self.not_beacon(x))
        return pruned_set

    @staticmethod
    def _between_two_points(a, b):
        """
        Given two (x,y) coordinates where only x or y varies
        Return the set of those coordinates as well as all points between them.
        """
        a, b = sorted([a, b])

        x_range = range(a[0], b[0] + 1)
        y_range = range(a[1], b[1] + 1)

        return set(itertools.product(x_range, y_range))

    def return_outside_edges(self):
        orig_x, orig_y = self.location

        top = orig_x, self.y_min - 1
        right = self.x_max + 1, orig_y
        bottom = orig_x, self.y_max + 1
        left = self.x_min - 1, orig_y

        top_right = Sensor.rotate_45_cw(top)
        top_left = Sensor.rotate_45_cw(left)
        bottom_left = Sensor.rotate_45_cw(bottom)
        bottom_right = Sensor.rotate_45_cw(right)

        upper_edge = self._between_two_points(top_left, top_right)
        bottom_edge = self._between_two_points(bottom_left, bottom_right)
        right_edge = self._between_two_points(top_right, bottom_right)
        left_edge = self._between_two_points(top_left, bottom_left)

        edges = set().union(upper_edge, bottom_edge, left_edge, right_edge)

        return {self.rotate_45_ccw(edge) for edge in edges}

    @staticmethod
    def rotate_45_cw(coord: tuple[int, int], center=(0, 0)):
        x, y = coord
        x_rotated = x - y
        y_rotated = x + y

        return round(x_rotated), round(y_rotated)

    @staticmethod
    def rotate_45_ccw(coord: tuple[int, int], center=(0, 0)):
        x, y = coord
        x_rotated = (x + y) / 2
        y_rotated = (y - x) / 2

        return round(x_rotated), round(y_rotated)

    def __eq__(self, other: 'Sensor'):
        if not isinstance(other, Sensor):
            raise TypeError

        return all([
            self.location == other.location,
            self.beacon == other.beacon
        ])

    def __repr__(self):
        return f"{self.__class__.__name__}({self.location}, {self.beacon})"

    @classmethod
    def from_string(cls, sensor_string: str):
        parse = re.compile(r'-*\d+')
        loc_x, loc_y, beac_x, beac_y = (int(x) for x in parse.findall(sensor_string))

        return Sensor(location=(loc_x, loc_y), beacon=(beac_x, beac_y))

    @classmethod
    def from_file(cls, filename: str) -> list['Sensor']:
        with open(filename, 'r') as infile:
            lines = [line.strip() for line in infile]

        return [Sensor.from_string(line) for line in lines]


def rule_out_row(y: int, sensors: list[Sensor]) -> set[tuple[int, int]]:
    """ Given list of Sensors and a row number return the set of coordinates on that row that don't contain beacon """
    min_x = min(sensor.x_min for sensor in sensors)
    max_x = max(sensor.x_max for sensor in sensors)

    x_locations = range(min_x, max_x + 1)

    no_beacons = set()
    for x in x_locations:
        for sensor in sensors:
            if sensor.not_beacon((x, y)):
                no_beacons.add((x, y))

    return no_beacons


def find_beacon(sensors: list[Sensor], search_min, search_max) -> tuple[tuple[int, int], int]:
    """ Given a search space, and a list of sensors, return the beacon location and tuning freq"""

    print('Finding Edges')
    edges = set()
    for sensor in tqdm(sensors):
        edges.update(sensor.return_outside_edges())

    print('Finding Beacon')
    for coord in tqdm(edges):
        x = coord[0]
        y = coord[1]
        if search_min <= x <= search_max and search_min <= y <= search_max:
            results = [sensor.in_sensor_net(coord) for sensor in sensors]
            if not any(results):
                return ((x, y), (x * 4000000 + y))


if __name__ == '__main__':
    sensors = Sensor.from_file('day15_input.txt')

    # print(len(rule_out_row(2_000_000, sensors)))

    print(find_beacon(sensors, search_min=0, search_max=4_000_000))
