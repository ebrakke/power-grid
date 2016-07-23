import unittest
from src.reducers import game

class TestGameReducer(unittest.TestCase):
	
	def test_returns_intial_players_if_no_state_supplied(self):
		state = game()
		self.assertEqual(state, dict(turn=0, phase=0))
	
	def test_returns_state_if_unknown_action_supplied(self):
		seed = dict(turn=0, phase=0)
		state = game(seed, dict(type='UNKNOWN'))
		self.assertEqual(state, seed)
	
	def test_returns_state_with_next_phase(self):
		seed = dict(turn=0, phase=0)
		state = game(seed, dict(type='NEXT_PHASE'))
		self.assertEqual(state['phase'], 1)
		
		state = game(dict(phase=3, turn=1), dict(type='NEXT_PHASE'))
		self.assertEqual(state['phase'], 0)
	
	def test_returns_state_with_next_turn(self):
		seed = dict(turn=0, phase=0)
		state = game(seed, dict(type='NEXT_TURN'))
		self.assertEqual(state['turn'], 1)
		

if __name__ == '__main__':
	unittest.main()