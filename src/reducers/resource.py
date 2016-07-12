initial_state = dict(
	coal=0,
	oil=0,
	gas=0,
	uranium=0
)

def resource(state=None, action=None):
	if state is None:
		state = initial_state
	if action is None or type(action) is not dict:
		return state
	
	ty = action.get('type')
	if ty == 'REPLENISH_RESOURCE':
		new_state = dict(**state)
		new_state[action.get('resource')] = action.get('amount')
		return new_state
	
	if ty == 'TAKE_RESOURCE':
		new_amount = state[action.get('resource')] - action.get('amount')
		new_state = dict(**state)
		new_state[action.get('resource')] = new_amount
		return new_state
	
	return state