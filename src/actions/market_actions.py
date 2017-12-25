def purchase_card(card_index):
    return {
        'type': 'MARKET_PURCHASE_CARD',
        'purchased_index': card_index
    }


def add_card(card):
    return {
        'type': 'MARKET_ADD_CARD',
        'card': card
    }


def bid_on_card(card, amount, player_id):
    return {
        'type': 'BID_ON_CARD',
        'amount': amount,
        'card': card,
        'player_id': player_id
    }
