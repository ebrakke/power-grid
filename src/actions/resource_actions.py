def replenish_resource(resource, amount):
	return {
		'type': 'REPLENISH_RESOURCE',
		'amount': amount
	}

def take_resource(resource, amount):
	return {
		'type': 'TAKE_RESOURCE',
		'amount': amount
	}