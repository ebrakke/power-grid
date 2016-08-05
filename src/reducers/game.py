def initial_game():
	""" setup an intial game"""
	return dict(
		turn=0,
		phase=0,
		current_bid=None
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
	
	if ty == 'BID_ON_POWER_PLANT':
		next_state = dict(**state)
		# only update the bid if the new amount is greater than the old amount
		if state.get('current_bid') is None or state.get('current_bid').get('amount') < action.get('amount'):
			next_state['current_bid'] = dict(
				player_id=action.get('player_id'),
				card=action.get('card'),
				amount=action.get('amount')
			)
		return next_state
	
	return state
	
	