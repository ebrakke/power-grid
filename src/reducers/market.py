def order_market(state):
    all_cards = state['futures'] + state['current']
    sorted_market = sorted(all_cards, key=lambda x: x.get('market_cost'))
    return dict(futures=sorted_market[4:], current=sorted_market[:4])


def market(state=None, action=None):
    if state is None:
        state = {
            'futures': [],
            'current': []
        }
    if action is None:
        return state

    ty = action.get('type')
    if ty == 'MARKET_PURCHASE_CARD':
        new_market = dict(**state)
        new_market['current'].pop(action.get('purchased_index'))
        return new_market

    if ty == 'MARKET_ADD_CARD':
        state['current'] = state['current'] + [action.get('card')]
        new_state = order_market(state)
        return new_state

    return state
