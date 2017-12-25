def next_turn():
    return {
        'type': 'NEXT_TURN'
    }


def next_phase():
    return {
        'type': 'NEXT_PHASE'
    }


def bid_on_power_plant(player_id, card, amount):
    return {
        'type': 'BID_ON_POWER_PLANT',
        'player_id': player_id,
        'card': card,
        'amount': amount
    }


def next_player():
    return {
        'type': 'NEXT_PLAYER'
    }
