from copy import deepcopy


def initial_game():
    """ setup an intial game"""
    return dict(
        phase=1,
        step=1,
        current_player='',
        current_bid=dict(
            player_id='',
            card=None,
            amount=0,
            passed=[]
        ),
        player_rank=[],
        bought_or_passed=[]
    )


def game(state=None, action=None):
    if state is None:
        state = initial_game()
    if action is None:
        return state

    action_type = action.get('type')
    if action_type == 'GAME_NEXT_STEP':
        if state['step'] == 3:
            return state
        next_state = deepcopy(state)
        next_state['step'] = state['step'] + 1
        return next_state

    if action_type == 'GAME_NEXT_PHASE':
        next_state = deepcopy(state)
        if state['phase'] == 5:
            next_state['phase'] = 1
            return next_state
        next_state['phase'] = state['phase'] + 1
        return next_state

    if action_type == 'GAME_SET_CURRENT_BID':
        next_state = deepcopy(state)
        # only update the bid if the new amount is greater than the old amount
        if state.get('current_bid') is None or state.get('current_bid').get('amount') < action.get('amount'):
            next_state['current_bid'] = dict(
                player_id=action.get('player_id'),
                card=action.get('card'),
                amount=action.get('amount'),
                passed=state.get('current_bid').get('passed')
            )
        return next_state

    if action_type == 'GAME_PASS_CURRENT_BID':
        next_state = deepcopy(state)
        next_state['current_bid']['passed'] = state['current_bid']['passed'] + \
            [action.get('player_id')]
        return next_state

    if action_type == 'GAME_PASS_INITIAL_BID':
        next_state = deepcopy(state)
        next_state['bought_or_passed'] = state['bought_or_passed'] + \
            [action.get('player_id')]
        return next_state

    if action_type == 'GAME_WIN_CURRENT_BID':
        next_state = deepcopy(state)
        # Add the player with the highest bid to the bought_or_passed property
        next_state['bought_or_passed'] = state['bought_or_passed'] + \
            [state['current_bid']['player_id']]
        return next_state

    if action_type == 'GAME_CLEAR_BID':
        next_state = deepcopy(state)
        next_state['current_bid'] = dict(
            player_id='',
            card=None,
            amount=0,
            passed=[]
        )
        return next_state

    if action_type == 'GAME_SET_PLAYER_RANK':
        next_state = deepcopy(state)
        next_state['player_rank'] = action.get('player_rank')
        return next_state

    if action_type == 'GAME_SET_CURRENT_PLAYER':
        next_state = deepcopy(state)
        next_state['current_player'] = action.get('player_id')
        return next_state

    if action_type == 'GAME_CLEAR_BOUGHT_OR_PASSED':
        next_state = deepcopy(state)
        next_state['bought_or_passed'] = []
        return next_state

    return state
