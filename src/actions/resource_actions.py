def replenish_resource(resource, amount):
	return {
		'indicator': 'REPLENISH_RESOURCE',
		'type': resource,
		'amount': amount
	}

def take_resource(resource, amount):
	return {
		'indicator': 'TAKE_RESOURCE',
		'type': resource,
		'amount': amount
	}