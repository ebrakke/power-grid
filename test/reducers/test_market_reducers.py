import unittest
from src.reducers import market
from src.actions.market_actions import purchase_card, add_card

class TestMarketReducer(unittest.TestCase):
	
	def test_returns_intial_market_if_no_state_supplied(self):
		state = market()
		self.assertEqual(state, dict(futures=[], current=[]))
	
	def test_returns_state_if_unknown_action_supplied(self):
		seed = dict(current=[], futures=[])
		state = market(seed, dict(type='UNKNOWN'))
		self.assertEqual(state, seed)
	
	def test_removes_card_by_index_from_current_market(self):
		state = dict(
			current=[ dict(market_cost=3), dict(market_cost=4), dict(market_cost=5), dict(market_cost=6)],
			futures=[ dict(market_cost=7), dict(market_cost=8), dict(market_cost=9), dict(market_cost=10)]
		)
		new_state = market(state, purchase_card(2))
		self.assertTrue(len([c for c in new_state['current'] if c['market_cost'] == 5]) == 0)
	
	def test_adds_card_to_market_and_sorts(self):
		state = dict(
			current=[ dict(market_cost=3), dict(market_cost=5), dict(market_cost=6)],
			futures=[ dict(market_cost=7), dict(market_cost=8), dict(market_cost=9), dict(market_cost=10)]
		)
		new_state = market(state, add_card(dict(market_cost=4)))
		self.assertEqual(new_state['current'][1], dict(market_cost=4))
		

if __name__ == '__main__':
	unittest.main()