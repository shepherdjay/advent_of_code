import pytest
from day16 import Valve, ValveTree, relieve_pressure, parse_line


@pytest.fixture(scope='function')
def simple_valve_tree():
    """ Constructs and returns simple valve tree"""
    return ValveTree([
        Valve(id='A', neighbors=('B', 'C'), flow=0),
        Valve(id='B', neighbors=('A', 'D'), flow=0),
        Valve(id='C', neighbors=('A',), flow=10),
        Valve(id='D', neighbors=('B',), flow=16),
    ])


@pytest.fixture(scope='function')
def example_valve_tree():
    with open('day16_example_input.txt', 'r') as infile:
        valves = [parse_line(line.strip()) for line in infile]
    return ValveTree(valves)


def test_simple_valve_tree(simple_valve_tree):
    """ GIVEN: The simple_valve_tree and 10 Minutes """
    assert relieve_pressure(tree=simple_valve_tree, timer=10, starting_node_id='A') == 144


def test_parse_line():
    assert parse_line('Valve AA has flow rate=0; tunnels lead to valves DD, II, BB') \
           == Valve(id='AA', flow=0, neighbors=('DD', 'II', 'BB'))


def test_example_valve_tree(example_valve_tree):
    pressure = relieve_pressure(tree=example_valve_tree, timer=30, starting_node_id='AA')

    assert pressure == 1651

