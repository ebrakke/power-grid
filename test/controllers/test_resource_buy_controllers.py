import unittest
import functools
from src.controllers.resource_buy import get_available_resource_costs, bank_has_enough_resources
from copy import deepcopy


class TestResourceBuyControllers(unittest.TestCase):
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
        ), dict(
            player_id='player_4',
            money=50,
            power_plants=[]
        )
    ]
    resources = dict(
        current_resource_bank=[
            {
                "coal": 0,
                "uranium": 0,
                "oil": 0,
                "gas": 0
            },
            {
                "coal": 4,
                "uranium": 0,
                "oil": 0,
                "gas": 0
            },
            {
                "coal": 4,
                "uranium": 0,
                "oil": 0,
                "gas": 3
            },
            {
                "coal": 3,
                "uranium": 0,
                "oil": 2,
                "gas": 3
            },
            {
                "coal": 3,
                "uranium": 0,
                "oil": 2,
                "gas": 3
            },
            {
                "coal": 3,
                "uranium": 0,
                "oil": 2,
                "gas": 3
            },
            {
                "coal": 2,
                "uranium": 0,
                "oil": 2,
                "gas": 3
            },
            {
                "coal": 2,
                "uranium": 0,
                "oil": 2,
                "gas": 3
            },
            {
                "coal": 2,
                "uranium": 2,
                "oil": 4,
                "gas": 0
            }
        ]
    )

    def test_get_available_resource_costs_returns_lowest_costs_for_amount(self):
        cost = get_available_resource_costs(
            'coal', 2, [dict(coal=2, oil=2), dict(coal=4, oil=1)])
        self.assertEqual(cost, 2)

    def test_get_available_resource_costs_only_returns_maximum_available(self):
        cost = get_available_resource_costs('coal', 10, [dict(coal=2, oil=2)])
        self.assertEqual(cost, 2)

    def test_get_available_resource_costs_only_uses_non_zero_buckets(self):
        cost = get_available_resource_costs(
            'coal', 2, [dict(coal=0), dict(coal=2)])
        self.assertEqual(cost, 4)
    
    def test_bank_has_enough_resources_true_when_enough_resources_present(self):
        buying = dict(coal=3, oil=3)
        bank = [dict(coal=1, oil=2), dict(coal=2, oil=2)]
        self.assertTrue(bank_has_enough_resources(buying, bank))
    
    def test_bank_has_enough_resources_false_when_not_enough(self):
        buying = dict(coal=10)
        bank = [dict(coal=2)]
        self.assertFalse(bank_has_enough_resources(buying, bank))
