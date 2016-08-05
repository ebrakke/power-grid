from hashlib import md5
from random import random

def create_player(name):
	""" Returns a new player for the game
	:param name
	"""
	if name is None:
		name = ''
	return dict(
		id=md5(str(random()).encode('utf-8') + name.encode('utf-8')).hexdigest(),
		name=name,
		money=50,
		power_plants=[]
	)

def players(state=None, action=None):
	if state is None:
		state = []
	if action is None:
		return state
	
	ty = action.get('type')
	if ty == 'CREATE_PLAYER':
		return state + [create_player(action.get('name'))]
	
	return state

	
	