import unittest
from src.reducers import game
from src.reducers.game import initial_game


class TestGameReducer(unittest.TestCase):

    def test_returns_intial_players_if_no_state_supplied(self):
        initial_state = initial_game()
        state = game()
        self.assertEqual(state, initial_state)

    def test_returns_state_if_unknown_action_supplied(self):
        seed = dict(step=1, phase=1)
        state = game(seed, dict(type='UNKNOWN'))
        self.assertEqual(state, seed)

    def test_returns_state_with_next_phase(self):
        seed = dict(step=1, phase=1)
        state = game(seed, dict(type='GAME_NEXT_PHASE'))
        self.assertEqual(state['phase'], 2)

        state = game(dict(phase=5, turn=1), dict(type='GAME_NEXT_PHASE'))
        self.assertEqual(state['phase'], 1)

    def test_returns_state_with_next_turn(self):
        seed = dict(step=1, phase=1)
        state = game(seed, dict(type='GAME_NEXT_STEP'))
        self.assertEqual(state['step'], 2)

    def test_updates_current_bid_when_no_bid_exists(self):
        state = game()
        next_state = game(state, dict(type='GAME_SET_CURRENT_BID',
                                      card=None, amount=3, player_id='123'))
        self.assertEqual(next_state['current_bid']['amount'], 3)

    def test_does_not_update_current_bid_when_bid_is_higher_than_amount(self):
        state = initial_game()
        state['current_bid']['amount'] = 6
        next_state = game(state, dict(type='GAME_SET_CURRENT_BID',
                                      card=None, amount=3, player_id='123'))
        self.assertEqual(next_state['current_bid']['amount'], 6)
        self.assertNotEqual(next_state['current_bid']['player_id'], '123')


if __name__ == '__main__':
    unittest.main()
