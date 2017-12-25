import unittest
import json
from src.reducers import game_map


class TestMapReducer(unittest.TestCase):
    def test_adds_player_to_city(self):
        state = game_map()
        new_state = game_map(state, dict(type='BUILD_IN_CITY',
                                      city='Lisboa', player_id='1', slot='1'))
        self.assertEqual(new_state.get('Lisboa')['1'], '1')

    def test_returns_state_if_unknown_action_supplied(self):
        state = game_map([], dict(type='UNKNOWN'))
        self.assertEquals(state, [])


if __name__ == '__main__':
    unittest.main()
