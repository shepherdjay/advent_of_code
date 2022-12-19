import pytest
from day16 import Valve, ValveTree, relieve_pressure


@pytest.fixture(scope='function')
def simple_valve_tree():
    """ Constructs and returns simple valve tree"""
    return ValveTree([
        Valve(id='A', neighbors={'B', 'C'}, flow=0),
        Valve(id='B', neighbors={'A', 'D'}, flow=0),
        Valve(id='C', neighbors={'A'}, flow=10),
        Valve(id='D', neighbors={'B'}, flow=16),
    ])


def test_simple_valve_tree(simple_valve_tree):
    """ GIVEN: The simple_valve_tree and 10 Minutes """
    assert relieve_pressure(valve_tree=simple_valve_tree, timer=10) == (144, ['A', 'C', 'A', 'B', 'D'])

def test_find_common_ancester(simple_valve_tree):
    """ GIVEN: The simple_valve_tree with an additional relationship between B and C """
    simple_valve_tree['B'].neighbors.add('C')
    simple_valve_tree['C'].neighbors.add('B')

    assert find_common_ancester(['C', 'D'], valve_tree=simple_valve_tree) == 'B'