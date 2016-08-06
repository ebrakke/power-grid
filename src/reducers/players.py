def create_player(player_id):
	""" Returns a new player for the game
	:param name
	"""
	return dict(
		player_id=player_id,
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
		return state + [create_player(action.get('player_id'))]
	
	return state

	
	