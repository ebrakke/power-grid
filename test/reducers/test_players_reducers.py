import unittest
from src.reducers import players

class TestPlayersReducer(unittest.TestCase):
	
	def test_returns_intial_players_if_no_state_supplied(self):
		state = players()
		self.assertEqual(state, [])
	
	def test_returns_state_if_unknown_action_supplied(self):
		state = players([], dict(type='UNKNOWN'))
		self.assertEqual(state, [])

if __name__ == '__main__':
	unittest.main()