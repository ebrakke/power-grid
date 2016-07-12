import unittest
import json
from src.reducers import board

class TestDeckReducer(unittest.TestCase):
	def test_returns_intial_state_if_no_state_supplied(self):
		state = board()
		self.assertEqual(len(state), 49)
	
	def test_removes_city_from_state_if_color_matches(self):
		state = board()
		cities = json.loads(open('src/config/map_colors.json').read())
		red_cities = [city for city in cities if cities[city] == 'red']
		
		new_state = board(state, dict(type='REMOVE_COLOR', color='red'))
		self.assertEqual([city for city in new_state if city in red_cities], [])
	
	def test_adds_player_to_city(self):
		state = board()
		new_state = board(state, dict(type='BUILD_IN_CITY', city='Lisboa', player_id=1, slot=0))
		self.assertEqual(state.get('Lisboa')[0], 1)
	
	def test_returns_state_if_unknown_action_supplied(self):
		state = board([], dict(type='UNKNOWN'))
		self.assertEquals(state, [])

if __name__ == '__main__':
	unittest.main()