import unittest
import json
import os.path
from copy import deepcopy
from src.reducers import resources
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
INITIAL_RESOURCES = json.loads(
    open(os.path.join(CURRENT_PATH, '../../src/config/initial_resources.json')).read())
MAX_RESOURCES = json.loads(
    open(os.path.join(CURRENT_PATH, '../../src/config/max_resources.json')).read())

class TestResourcesReducer(unittest.TestCase):

    def setUp(self):
        self.initial_state = deepcopy(INITIAL_RESOURCES)

    def test_returns_intial_deck_if_no_state_supplied(self):
        state = resources()
        self.assertEqual(state, self.initial_state)

    def test_adds_value_to_state_on_replenish_resource(self):
        state = resources()
        new_state = resources(state, dict(
            type='REPLENISH_RESOURCE', resource_type='coal'))
        self.assertEqual(new_state[0]['coal'], 1)

    def test_removes_amount_on_take_resource(self):
        state = resources()
        new_state = resources(state, dict(
            type='TAKE_RESOURCE', resource_type='coal'))
        self.assertEqual(new_state[1]['coal'], 3)
    
    def test_removes_nothing_if_no_resource(self):
        empty_state = [dict(coal=0, oil=0, gas=0, uranium=0) for x in range(9)]
        new_state = resources(empty_state, dict(
            type='TAKE_RESOURCE', resource_type='coal'
        ))
        self.assertFalse(any(x != y for (x,y) in zip(empty_state, new_state)))
    
    def test_adds_nothing_if_all_resources_are_full(self):
        full_state = deepcopy(MAX_RESOURCES)
        new_state = resources(full_state, dict(
            type='REPLENISH_RESOURCE', resource_type='coal'
        ))
        self.assertFalse(any(x != y for (x,y) in zip(full_state, new_state)))

    def test_returns_state_if_unknown_action_supplied(self):
        state = resources([], dict(type='UNKNOWN'))
        self.assertEquals(state, [])


if __name__ == '__main__':
    unittest.main()
