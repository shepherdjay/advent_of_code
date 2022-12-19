import pytest
from day16 import Valve, ValveTree, relieve_pressure, generate_possible_paths, cost_between_nodes, parse_line, simulate_path


@pytest.fixture(scope='function')
def simple_valve_tree():
    """ Constructs and returns simple valve tree"""
    return ValveTree([
        Valve(id='A', neighbors={'B', 'C'}, flow=0),
        Valve(id='B', neighbors={'A', 'D'}, flow=0),
        Valve(id='C', neighbors={'A'}, flow=10),
        Valve(id='D', neighbors={'B'}, flow=16),
    ])


@pytest.fixture(scope='function')
def example_valve_tree():
    with open('day16_example_input.txt', 'r') as infile:
        valves = [parse_line(line.strip()) for line in infile]
    return ValveTree(valves)


def test_simple_valve_tree(simple_valve_tree):
    """ GIVEN: The simple_valve_tree and 10 Minutes """
    assert relieve_pressure(valve_tree=simple_valve_tree, timer=10, starting_node_id='A') == (144, ['C', 'A', 'B', 'D'])


def test_parse_line():
    assert parse_line('Valve AA has flow rate=0; tunnels lead to valves DD, II, BB') \
           == Valve(id='AA', flow=0, neighbors={'DD', 'II', 'BB'})


def test_example_valve_tree(example_valve_tree):
    pressure, path = relieve_pressure(valve_tree=example_valve_tree, timer=30, starting_node_id='AA')
    assert path == ["DD", "CC", "BB", "AA",
                    "II", "JJ", "II", "AA",
                    "DD", "EE", "FF", "GG",
                    "HH", "GG", "FF", "EE",
                    "DD", "CC", ]
    assert pressure == 1651


def test_generate_possible_paths(simple_valve_tree):
    """
    GIVEN: The simple valve_tree calculate all possible combinations of paths
    that could be taken to all nodes with positive flow
    """
    possible_paths = generate_possible_paths(starting_node_id='A', valve_tree=simple_valve_tree)
    by_id = [[valve.id for valve in path] for path in possible_paths]
    assert by_id == [
        ['C', 'A', 'B', 'D'],
        ['B', 'D', 'B', 'A', 'C']
    ]


def test_simulate_path(example_valve_tree):
    example_path = ["AA", "DD", "CC", "BB", "AA",
                    "II", "JJ", "II", "AA",
                    "DD", "EE", "FF", "GG",
                    "HH", "GG", "FF", "EE",
                    "DD", "CC", ]

    node_path = [example_valve_tree[node_id] for node_id in example_path]
    relief_nodes = [example_valve_tree[node_id] for node_id in ['BB', 'CC', 'DD', 'EE', 'HH', 'JJ']]

    path_cost, path = simulate_path(node_path, relief_nodes=relief_nodes, timer=30)
    assert path_cost == 1651


def test_cost_between_nodes(simple_valve_tree):
    assert cost_between_nodes('C', 'D', simple_valve_tree) == 3
