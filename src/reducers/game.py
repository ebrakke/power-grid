def initial_game():
	""" setup an intial game"""
	return dict(
		turn=0,
		phase=0
	)

def game(state=None, action=None):
	if state is None:
		state = initial_game()
	if action is None:
		return state
	
	ty = action.get('type')
	if ty == 'NEXT_TURN':
		next_state = dict(**state)
		next_state['turn'] = (state['turn'] + 1) % 3
		return next_state
	
	if ty == 'NEXT_PHASE':
		next_state = dict(**state)
		next_state['phase'] = (state['phase'] + 1) % 4
		return next_state
	
	return state
	
	