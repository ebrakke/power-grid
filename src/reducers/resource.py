initial_state = dict(
	coal=0,
	oil=0,
	gas=0,
	uranium=0
)

max_vals = {
	"gas" : 24,
	"oil" : 20,
	"coal" : 27,
	"uranium" : 12
}

def resource(state=None, action=None):
	if state is None:
		state = initial_state
	if action is None or type(action) is not dict:
		return state
	
	ty = action.get('indicator')
	if ty == 'REPLENISH_RESOURCE':
		new_state = dict(**state)
		# check for max values
		new_state['resource'][action.get('resource')] += action.get('amount')
		return new_state
	
	if ty == 'TAKE_RESOURCE':
		print("Value 1: " + str(state[action.get('resource')]))
		print("Value 2: " + str(state['resource'][action.get('resource')]))
		new_amount = state['resource'][action.get('resource')] - action.get('amount')
		new_state = dict(**state)
		new_state[action.get('resource')] = new_amount
		return new_state
	
	return state