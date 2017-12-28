def next_step():
    return {
        'type': 'GAME_NEXT_STEP'
    }


def next_phase():
    return {
        'type': 'GAME_NEXT_PHASE'
    }


def set_current_bid(player_id, card, amount):
    return dict(
        type='GAME_SET_CURRENT_BID',
        player_id=player_id,
        amount=amount,
        card=card
    )


def pass_current_bid(player_id):
    return dict(type='GAME_PASS_CURRENT_BID', player_id=player_id)


def pass_initial_bid(player_id):
    return dict(type='GAME_PASS_INITIAL_BID', player_id=player_id)


def win_current_bid():
    return dict(type='GAME_WIN_CURRENT_BID')


def clear_bid():
    return dict(type='GAME_CLEAR_BID')


def set_player_rank(player_rank):
    return dict(type='GAME_SET_PLAYER_RANK', player_rank=player_rank)


def set_current_player(player_id):
    return dict(type='GAME_SET_CURRENT_PLAYER', player_id=player_id)


def clear_bought_or_passed():
    return dict(type='GAME_CLEAR_BOUGHT_OR_PASSED')

def set_bidding_order(bidding_order):
    return dict(type='GAME_SET_BIDDING_ORDER', bidding_order=bidding_order)
