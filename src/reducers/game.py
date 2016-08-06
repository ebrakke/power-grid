def initial_game():
	""" setup an intial game"""
	return dict(
		turn=0,
		phase=0,
		current_bid=None,
		player_order=[],
		current_player=None
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
	
	if ty == 'CREATE_PLAYER':
		next_state = dict(**state)
		next_state['player_order'].append(action.get('player_id'))
		
		# Set current player if none is set yet
		if state.get('current_player') is None:
			next_state['current_player'] = action.get('player_id')
		return next_state
	
	if ty == 'NEXT_PLAYER':
		current_player_index = state.get('player_order').index(state.get('current_player'))
		# This will just be the next player in the player_order list
		next_player_index = (current_player_index + 1) % len(state.get('player_order'))
		next_state = dict(**state)
		next_state['current_player'] = state.get('player_order')[next_player_index]
		return next_state
	
	
	return state
	
	