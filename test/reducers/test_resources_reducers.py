import unittest
import json
import os.path
from copy import deepcopy
from src.reducers import resources
from src.reducers.resources import INITIAL_STATE


class TestResourcesReducer(unittest.TestCase):

    def setUp(self):
        self.initial_state = deepcopy(INITIAL_STATE)

    def test_returns_intial_deck_if_no_state_supplied(self):
        state = resources()
        self.assertEqual(state, self.initial_state)

    def test_adds_value_to_state_on_replenish_resource(self):
        state = resources()
        new_state = resources(state, dict(
            type='REPLENISH_RESOURCE', resource_type='coal'))
        self.assertEqual(new_state['current_resource_bank'][0]['coal'], 1)

    def test_removes_amount_on_take_resource(self):
        state = resources()
        new_state = resources(state, dict(
            type='TAKE_RESOURCE', resource_type='coal'))
        self.assertEqual(new_state['current_resource_bank'][1]['coal'], 3)

    def test_removes_nothing_if_no_resource(self):
        state = resources()
        state['current_resource_bank'] = [
            dict(coal=0, uranium=0, oil=0, gas=0)] * 9
        new_state = resources(state, dict(
            type='TAKE_RESOURCE', resource_type='coal'
        ))
        self.assertFalse(any(x != y for (x, y) in zip(
            state['current_resource_bank'], new_state['current_resource_bank'])))

    def test_adds_nothing_if_all_resources_are_full(self):
        state = resources()
        state['current_resource_bank'] = deepcopy(state['max_resource_bank'])
        new_state = resources(state, dict(
            type='REPLENISH_RESOURCE', resource_type='coal'
        ))
        self.assertFalse(any(x != y for (x, y) in zip(
            state['current_resource_bank'], new_state['current_resource_bank'])))

    def test_returns_state_if_unknown_action_supplied(self):
        state = resources([], dict(type='UNKNOWN'))
        self.assertEquals(state, [])


if __name__ == '__main__':
    unittest.main()
