import unittest
from src.reducers import resource

class TestResourceReducer(unittest.TestCase):
	
	def setUp(self):
		self.initial_state = dict(
			coal=0,
			gas=0,
			oil=0,
			uranium=0
		)
	def test_returns_intial_deck_if_no_state_supplied(self):
		state = resource()
		self.assertEqual(state, self.initial_state)
	
	def test_adds_value_to_state_on_replenish_resource(self):
		state = resource()
		new_state = resource(state, dict(type='REPLENISH_RESOURCE', resource='coal', amount=2))
		self.assertEqual(new_state['coal'], 2)
	
	def test_removes_amount_on_take_resource(self):
		state = resource(dict(coal=3))
		new_state = resource(state, dict(type='TAKE_RESOURCE', resource='coal', amount=2))
		self.assertEqual(new_state['coal'], 1)
	
	def test_returns_state_if_unknown_action_supplied(self):
		state = resource([], dict(type='UNKNOWN'))
		self.assertEquals(state, [])

if __name__ == '__main__':
	unittest.main()