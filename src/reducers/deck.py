import json
import os.path
from random import shuffle
current_path = os.path.dirname(os.path.realpath(__file__))
cards = json.loads(
    open(os.path.join(current_path, '../config/cards.json')).read())


def initialize_state(cards):
    light_cards = [c for c in cards if c['type'] == 'light']
    dark_cards = [c for c in cards if c['type'] == 'dark']
    shuffle(dark_cards)
    shuffle(light_cards)
    #we are only playing 4 payers, so we need to remove some cards
    held_card = dark_cards.pop()
    dark_cards = dark_cards[1:] #discard 1
    light_cards = light_cards[3:] # discard 3
    inital_market = dark_cards[:8]
    deck = dark_cards[8:] + light_cards
    shuffle(deck)
    return inital_market + held_card + deck


def deck(state=None, action=None):
    if state is None:
        state = initialize_state(cards)
    if action is None or type(action) != dict:
        return state

    ty = action.get('type')
    if ty == 'DRAW_CARD':
        # remove first card from the state
        return state[1:]

    if ty == 'ADD_BOTTOM_CARD':
        # add new card to end of list
        return state + [action.get('card')]
    return state
