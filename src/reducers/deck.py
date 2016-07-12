import json
from random import shuffle

cards = json.loads(open('src/config/cards.json').read())

def initialize_state(cards):
	light_cards = [c for c in cards if c['type'] == 'light']
	dark_cards = [c for c in cards if c['type'] == 'dark']
	shuffle(dark_cards)
	shuffle(light_cards)
	return dark_cards + light_cards
	
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


