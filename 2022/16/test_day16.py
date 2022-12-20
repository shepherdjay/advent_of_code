import pytest
from day16 import Valve, ValveTree, parse_line


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
    tree = simple_valve_tree
    starting_node = tree['A']
    relief_tree = tree.construct_relief_node_tree(starting_node)
    assert simple_valve_tree.dfs(tree=relief_tree, node=starting_node, time=10) == 144


def test_simple_valve_tree_v2(simple_valve_tree):
    """ GIVEN: The simple_valve_tree and 10 Minutes """
    assert simple_valve_tree.dfs_part2(starting_node=simple_valve_tree['A'], cost_limit=10) == 192


def test_parse_line():
    assert parse_line('Valve AA has flow rate=0; tunnels lead to valves DD, II, BB') \
           == Valve(id='AA', flow=0, neighbors=('DD', 'II', 'BB'))


def test_example_valve_tree(example_valve_tree):
    tree = example_valve_tree
    starting_node = tree['AA']
    relief_tree = tree.construct_relief_node_tree(starting_node)
    pressure = tree.dfs(tree=relief_tree, node=starting_node, time=30)

    assert pressure == 1651


def test_example_valve_tree_v2(example_valve_tree):
    tree = example_valve_tree
    starting_node = tree['AA']
    relief_tree = tree.construct_relief_node_tree(starting_node)
    pressure = tree.dfs_part2(starting_node=starting_node, cost_limit=26)

    assert pressure == 1707
