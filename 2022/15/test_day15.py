from day15 import Sensor, rule_out_row, find_beacon
import hypothesis.strategies as st


class TestSensor:
    def setup_method(self):
        self.simple_sensor = Sensor(location=(0,0), beacon=(1,0))

    def test_Sensor_from_string(self):
        sensor_string = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
        expected_sensor = Sensor(location=(2, 18), beacon=(-2, 15))

        assert Sensor.from_string(sensor_string) == expected_sensor

    def test_Sensor_from_filel(self):
        filename = 'test_day15_input.txt'

        sensors = Sensor.from_file(filename)

        assert len(sensors) == 14

    def test_Sensor_non_beacon_locations(self):
        expected_non_beacon_locations = {
            (-1,0), (0,0), (0,1), (0,-1)
        }

        assert self.simple_sensor.non_beacon_locations() == expected_non_beacon_locations

    def test_rule_out_row(self):
        sensors = [self.simple_sensor]
        expected = {(0,1)}

        assert rule_out_row(y=1, sensors=sensors) == expected

def test_example_input():
    sensors = Sensor.from_file('test_day15_input.txt')
    non_beacons = rule_out_row(10, sensors)

    assert len(non_beacons) == 26

def test_find_beacon():
    sensors = Sensor.from_file('test_day15_input.txt')
    expected_beacon_location = (14,11)
    expected_tuning_freq = 56000011

    assert find_beacon(sensors=sensors, search_min=0, search_max=20) == (expected_beacon_location, expected_tuning_freq)