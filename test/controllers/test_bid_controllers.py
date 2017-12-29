import unittest
import functools
from src.controllers.bid import *
from copy import deepcopy


class TestBidControllers(unittest.TestCase):
    card_3 = {
        "generators": 1,
        "market_cost": 3,
        "resource_cost": 2,
        "resources": ["coal"],
        "type": "dark"
    }
    card_42 = {
        "generators": 6,
        "market_cost": 42,
        "resource_cost": 2,
        "resources": ["oil"],
        "type": "light"
    }
    card_38 = {
        "generators": 6,
        "market_cost": 38,
        "resource_cost": 3,
        "resources": ["oil"],
        "type": "light"
    }
    card_30 = {
      "generators": 5,
      "market_cost": 30,
      "resource_cost": 2,
      "resources": ["oil"],
      "type": "light"
    }
    card_23 = {
      "generators": 4,
      "market_cost": 23,
      "resource_cost": 2,
      "resources": [
        "oil"
      ],
      "type": "light"
    },
    card_18 = {
      "generators": 3,
      "market_cost": 18,
      "resource_cost": 2,
      "resources": [
        "oil"
      ],
      "type": "light"
    }
    card_10 = {
      "generators": 2,
      "market_cost": 10,
      "resource_cost": 2,
      "resources": [
        "oil"
      ],
      "type": "dark"
    }
    card_6 = {
      "generators": 1,
      "market_cost": 6,
      "resource_cost": 1,
      "resources": [
        "oil"
      ],
      "type": "dark"
    }

    market = {
        'futures': [card_23, card_30, card_38, card_42],
        'current': [card_3, card_6, card_10, card_18]
    }

    players = [
        dict(
            player_id='player_1',
            money=50,
            power_plants=[]
        ),
        dict(
            player_id='player_2',
            money=50,
            power_plants=[]
        ),
        dict(
            player_id='player_3',
            money=50,
            power_plants=[]
        ),dict(
            player_id='player_4',
            money=50,
            power_plants=[]
        )
    ]

    base_game_state = dict(
                        phase=2,
                        step=1,
                        current_player='player_1',
                        current_bid=dict(
                            player_id='player_2',
                            card={
                                "generators": 1,
                                "market_cost": 6,
                                "resource_cost": 1,
                                "resources": [
                                    "oil"
                                ],
                                "type": "dark"
                            },
                            amount=18,
                            passed=['player_3']
                        ),
                        player_rank=['player_1', 'player_3', 'player_4', 'player_2'],
                        bought_or_passed=['player_4'],
                        bidding_order=['player_1', 'player_2', 'player_3', 'player_4']
                    )

    def check_player_id(self, player_id, id_to_check):
        self.assertTrue(player_id == id_to_check)

    def test_when_given_a_valid_bid_it_should_return_true(self):
        self.assertTrue(valid_bid('player_1', 20, self.card_6, self.base_game_state,self.players, self.market))

    def test_fail_when_bidding_on_different_card(self):
        self.assertFalse(valid_bid('player_1', 20, self.card_10, self.base_game_state, self.players, self.market))

    def test_fail_when_bidding_when_passed(self):
        self.assertFalse(valid_bid('player_3', 20, self.card_6, self.base_game_state, self.players, self.market))

    def test_false_when_bidding_more_than_you_have(self):
        self.assertFalse(valid_bid('player_1', 51, self.card_6, self.base_game_state, self.players, self.market))

    def test_false_when_you_have_too_many_power_plants(self):
        test_players = deepcopy(self.players)
        test_players[0]['power_plants'] = [self.card_42, self.card_10, self.card_18, self.card_3]
        self.assertFalse(valid_bid('player_1', 20, self.card_6, self.base_game_state, test_players, self.market))

    def test_bid_is_won_with_pass(self):
        test_state = deepcopy(self.base_game_state)
        test_state['current_bid']['passed'] = test_state['current_bid']['passed'] + ['player_1']
        self.assertTrue(bid_is_won(test_state, 4))

    def test_bid_is_not_won_without_pass(self):
        self.assertFalse(bid_is_won(self.base_game_state, 4))

    def test_next_player_after_bid_is_player_3(self):
        test_state = deepcopy(self.base_game_state)
        test_state['current_bid'] = dict(player_id='', card=None, amount=0, passed=[])
        test_state['bought_or_passed'] = ['player_4', 'player_2']
        self.assertEqual('player_3', get_next_player(test_state, self.players))

    def test_next_player_after_player_1_bid_is_player_2(self):
        test_state = deepcopy(self.base_game_state)
        test_state['current_bid'] = dict(player_id='player_1', card=self.card_6, amount=20, passed=['player_3'])
        self.assertEqual('player_2', get_next_player(test_state, self.players))

    def test_next_player_is_one_with_4_powerplants(self):
        test_players = deepcopy(self.players)
        test_players[0]['power_plants'] = self.market['futures']
        self.assertEqual(self.players[0].get('player_id'), get_next_player(self.base_game_state, test_players))

    def test_next_player_is_last_ranked_in_next_phase(self):
        test_state = deepcopy(self.base_game_state)
        test_state['phase'] = 3
        test_state['bought_or_passed'] = []
        self.assertEqual(self.base_game_state['player_rank'][3] ,get_next_player(test_state, self.players))

    def test_next_player_is_next_after_initial_bid(self):
        test_state = deepcopy(self.base_game_state)
        test_state['bought_or_passed'] = ['player_1']
        test_state['current_bid'] = dict(player_id='', amount=0, card=None, passed=[])
        self.assertEqual('player_2', get_next_player(test_state, self.players))















if __name__ == '__main__':
    unittest.main()