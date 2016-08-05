import unittest
from src.reducers import game

class TestGameReducer(unittest.TestCase):
	
	def test_returns_intial_players_if_no_state_supplied(self):
		state = game()
		self.assertEqual(state, dict(turn=0, phase=0, current_bid=None))
	
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
	
	def test_updates_current_bid_when_no_bid_exists(self):
		state = game()
		next_state = game(state, dict(type='BID_ON_POWER_PLANT', card={ 'market_cost': 3 }, amount=3))
		self.assertEqual(next_state['current_bid']['amount'], 3)
	
	def test_does_not_update_current_bid_when_bid_is_higher_than_amount(self):
		state = game(dict(turn=0, phase=0, current_bid={'player_id': 1, 'card': {}, 'amount': 6}))
		next_state = game(state, dict(type='BID_ON_POWER_PLANT', card={}, amount=4))
		self.assertEqual(next_state['current_bid']['amount'], 6)
		
		
		

if __name__ == '__main__':
	unittest.main()