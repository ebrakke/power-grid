from src.actions.game_actions import pass_current_bid, pass_initial_bid, set_current_bid, \
    set_current_player, win_current_bid, next_phase, clear_bid, clear_bought_or_passed
from src.actions.players_actions import remove_power_plant
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
            return handle_pass_actions(player_id, get_state().get('game'), dispatch)

        dispatch(pass_current_bid(player_id))
        return handle_pass_actions(player_id, get_state().get('game'), get_state().get('players'), dispatch)

    if not valid_bid(player_id, amount, card, initial_state.get('game'), initial_state.get('players'), initial_state.get('market')):
        return False

    action = bid(player_id, card, amount)
    dispatch(action)
    return handle_pass_actions(player_id, get_state().get('game'), get_state().get('players'), dispatch)


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

    dispatch(remove_power_plant(player_id, card))
    return handle_pass_actions(player_id, get_state().get('game'), get_state().get('players'), dispatch)


def handle_pass_actions(player_id, game_state, players, dispatch):
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

    potential_player_ids = [player.get('player_id') for player in players if player not in passed + [player_id]]
    for id in game_state.get('bid_order'):
        if id in potential_player_ids:
            dispatch(set_current_player(id))
            return True

    return False


def valid_bid(player_id, amount, card, game_state, players, market):
    current_bid = game_state.get('current_bid')
    # All of these fields must be present
    if not all([player_id, amount, card]):
        return False

    # This is not a valid card to bid on
    if card not in market.get('current'):
        return False

    # Not allowed to bid on another card if a bid is currently going
    if current_bid.get('card') != card or not current_bid.get('card'):
        return False

    if player_id in game_state.get('bought_or_passed'):
        return False

    if current_bid and player_id in current_bid.get('passed'):
        return False

    player = [player for player in players if player['player_id'] == player_id][0]
    # You can't bid more than you have
    if amount > player['money']:
        return False

    # You can't get another power plant while you have four
    if len(player.get('power_plants')) == 4:
        return False

    return True

