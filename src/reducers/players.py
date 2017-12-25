from copy import deepcopy


def create_player(player_id):
    """ Returns a new player for the game
    :param name
    """
    return dict(
        player_id=player_id,
        money=50,
        power_plants=[]
    )


def players(state=None, action=None):
    if state is None:
        state = []
    if action is None:
        return state

    action_type = action.get('type')
    if action_type == 'PLAYER_CHANGE_MONEY':
        next_state = deepcopy(state)
        for p in next_state:
            if p == action.get('player_id'):
                p['money'] += action.get('money')
        return next_state
    if action_type == 'PLAYER_ADD_POWER_PLANT':
        next_state = deepcopy(state)
        for p in next_state:
            if p == action.get('player_id'):
                if len(p['power_plants']) < 4:
                    p['power_plants'].append(action.get('power_plant'))
        return next_state
    if action_type == 'PLAYER_REMOVE_POWER_PLANT':
        next_state = deepcopy(state)
        for p in next_state:
            if p == action.get('player_id'):
                if len(p['power_plants']) > 3:
                    p['power_plants'].remove(action.get('power_plant'))

            return next_state
    return state
