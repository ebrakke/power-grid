""" List of action creators to dispatch to the market reducers """
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


def add_cards(cards):
    return {
        'type': 'MARKET_ADD_CARDS',
        'cards': cards
    }
