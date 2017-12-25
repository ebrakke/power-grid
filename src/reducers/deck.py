"""Reducers for handing the deck game state"""
import json
import os.path
from random import shuffle
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
CARDS = json.loads(
    open(os.path.join(CURRENT_PATH, '../config/cards.json')).read())


def initialize_state(cards):
    """Initialize the deck"""
    light_cards = [c for c in cards if c['type'] == 'light']
    dark_cards = [c for c in cards if c['type'] == 'dark']
    shuffle(dark_cards)
    shuffle(light_cards)
    return dark_cards + light_cards


def deck(state=None, action=None):
    """Main reducer for the deck"""
    if state is None:
        state = initialize_state(CARDS)
    if action is None:
        return state

    action_type = action.get('type')
    if action_type == 'DRAW_CARD':
        # remove first card from the state
        return state[1:]

    if action_type == 'ADD_BOTTOM_CARD':
        # add new card to end of list
        return state + [action.get('card')]
    return state
