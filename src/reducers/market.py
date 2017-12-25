"""Manage the state for the market"""


def order_market(state):
    """Orders the market based on costs in ascending order"""
    all_cards = state['futures'] + state['current']
    sorted_market = sorted(all_cards, key=lambda x: x.get('market_cost'))
    # This will have to change based on the stage
    return dict(futures=sorted_market[4:], current=sorted_market[:4])


def market(state=None, action=None):
    """The reducer for the market state"""
    if state is None:
        state = {
            'futures': [],
            'current': []
        }
    if action is None:
        return state

    action_type = action.get('type')
    if action_type == 'MARKET_PURCHASE_CARD':
        new_market = dict(**state)
        new_market['current'].pop(action.get('purchased_index'))
        return new_market

    if action_type == 'MARKET_ADD_CARD':
        state['current'] = state['current'] + [action.get('card')]
        new_state = order_market(state)
        return new_state

    if action_type == 'MARKET_ADD_CARDS':
        state['current'] = state['current'] + action.get('cards')
        new_state = order_market(state)
        return new_state

    return state
