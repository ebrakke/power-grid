import unittest
from src.controllers.bid import *

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

    players = [dict(
        player_id='player_1',
        money=50,
        power_plants=[]
    ),
        dict(
            player_id='player_2',
            money=50,
            power_plants=[]
        ),dict(
        player_id='player_3',
        money=50,
        power_plants=[]
    ),dict(
        player_id='player_4',
        money=50,
        power_plants=[]
    )
    ]

    def test_when_given_a_valid_bid_it_should_return_true(self):
        player_id = 'player_1'
        ammount = 20
        card = self.card_6
        game_state = dict(
                        phase=1,
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
                            passed=['player_3', 'player_4']
                        ),
                        player_rank=['player_1', 'player_3', 'player_4', 'player_2'],
                        bought_or_passed=['player_4'],
                        bidding_order=['player_1', 'player_2', 'player_3', 'player_4']
                    )
        self.assertTrue(valid_bid(player_id, ammount, card, game_state,self.players, self.market))












if __name__ == '__main__':
    unittest.main()