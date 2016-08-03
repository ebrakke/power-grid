def next_turn():
	return {
		'type': 'NEXT_TURN'
	}

def next_phase():
	return {
		'type': 'NEXT_PHASE'
	}

def bid_on_power_plant(player_id, market_index, amount):
	return {
		'player_id': player_id,
		'market_index': market_index,
		'amount': amount
	}