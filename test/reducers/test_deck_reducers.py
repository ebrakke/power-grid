import unittest
from src.reducers import deck


class TestDeckReducer(unittest.TestCase):
    def test_deck_returns_intial_deck_if_no_state_supplied(self):
        state = deck()
        self.assertEqual(len(state), 39)

    def test_deck_returns_state_if_no_action_supplied(self):
        state = []
        self.assertEqual(deck(state), [])

    def test_removes_first_card_on_draw_card_action(self):
        state = deck()
        action = dict(type='DRAW_CARD')
        next_state = deck(state, action)

        self.assertNotEqual(state, next_state)
        self.assertTrue(state[0] not in next_state)

    def test_adds_card_to_bottom_of_deck_on_add_bottom_card_action(self):
        state = deck()
        test_card = dict(text='Test Card')
        action = dict(type='ADD_BOTTOM_CARD', card=test_card)
        next_state = deck(state, action)

        self.assertEqual(next_state[-1], test_card)

    def test_returns_state_if_unknown_action_supplied(self):
        state = deck([], dict(type='UNKNOWN'))
        self.assertEquals(state, [])


if __name__ == '__main__':
    unittest.main()
