from src.actions.game_actions import pass_current_bid, pass_initial_bid, set_current_bid, \
    set_current_player, win_current_bid, next_phase, clear_bid, clear_bought_or_passed
from src.actions.players_actions import discard_power_plant
from src.decorators.connect import connect


@connect
def bid(bid_request, **kwargs):
    """ Handle how to update the game when a player tried to bid on a market item"""
    player_id = bid_request.get('player_id')
    amount = bid_request.get('amount')
    card = bid_request.get('card')

    get_state = kwargs['get_state']
    dispatch = kwargs['dispatch']

    initial_state = get_state()
    current_bid = initial_state.get('game').get('current_bid')

    # This indicates a passing bid
    if amount == 0:
        # If no one has bid, this indicates passing on an initial bid
        if not current_bid:
            dispatch(pass_initial_bid(player_id))
            return handle_pass_actions(player_id, get_state(), dispatch)

        dispatch(pass_current_bid(player_id))
        return handle_pass_actions(player_id, get_state(), dispatch)

    if not valid_bid(player_id, amount, card, get_state()):
        return False
    action = bid(player_id, card, amount)
    dispatch(action)
    handle_pass_actions(player_id, get_state(), dispatch)
    return True


@connect
def discard_power_plant(discard_request, **kwargs):
    """ Handle discarding a powerplant when a player has 4"""
    player_id = discard_request.get('player_id')
    card = discard_request.get('card')

    get_state = kwargs['get_state']
    dispatch = kwargs['dispatch']

    initial_state = get_state()
    if not card:
        return False

    player = [pl for pl in initial_state.get('game').get('players') if pl.get('player_id') == player_id][0]

    if len(player.get('power_plants')) != 4:
        return False

    dispatch(discard_power_plant(player_id, card))
    return handle_pass_actions(player_id, get_state(), dispatch)


def handle_pass_actions(player_id, state, dispatch):
    game_state = state.get('game')
    total_players = len(game_state.get('players'))
    # If everyone has passed, it's time to go to the next phase
    if len(game_state.get('bought_or_passed')) == total_players:
        dispatch(next_phase())
        dispatch(clear_bought_or_passed())
        # The next phase is resources, so the last player goes first
        dispatch(set_current_player(game_state.get('player_rank')[total_players - 1]))
        return True

    passed = game_state.get('current_bid').get('passed')
    # All but one player passed on the bid,
    if len(passed) == total_players - 1:
        dispatch(win_current_bid())
        return True

    potential_player_ids = [player.get('player_id') for player in game_state.get('players') if player not in passed + [player_id]]
    for id in game_state.get('bid_order'):
        if id in potential_player_ids:
            dispatch(set_current_player(id))
            return True

    return False


def valid_bid(player_id, amount, card, state):
    current_bid = state.get('game').get('current_bid')
    # All of these fields must be present
    if not all([player_id, amount, card]):
        return False

    # This is not a valid card to bid on
    if card not in state.get('market').get('current'):
        return False

    # Not allowed to bid on another card if a bid is currently going
    if current_bid and current_bid.get('card') != card:
        return False

    if player_id in state.get('game').get('bought_or_passed'):
        return False

    if current_bid and player_id in current_bid.get('passed'):
        return False

    player = [player for player in state.get('players') if player['player_id'] == player_id][0]
    # You can't bid more than you have
    if amount > player['money']:
        return False

    # You can't get another power plant while you have four
    if len(player.get['power_plants']) == 4:
        return False





    return True

