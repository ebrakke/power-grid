from src.actions.game_actions import pass_current_bid, pass_initial_bid, set_current_bid, \
    set_current_player, win_current_bid, next_phase, clear_bid, clear_bought_or_passed
from src.actions.players_actions import remove_power_plant, add_power_plant, change_money
from src.actions.market_actions import purchase_card, add_card
from src.actions.deck_actions import draw_card
from src.decorators.connect_to_store import connect


@connect
def bid(bid_request, **kwargs):
    """ Handle how to update the game when a player tried to bid on a market item"""
    player_id = bid_request.get('player_id')
    amount = bid_request.get('amount')
    card = bid_request.get('card')

    get_state = kwargs['get_state']
    dispatch = kwargs['dispatch']

    initial_state = get_state()
    if initial_state.get('game').get('phase') != 2:
        return False
    num_players = len(initial_state.get('players'))
    current_bid = initial_state.get('game').get('current_bid')
    # This indicates a passing bid
    if amount == 0:
        # If no one has bid, this indicates passing on an initial bid
        if not current_bid.get('card'):
            player = [pl for pl in initial_state.get('players') if pl.get('player_id') == player_id]
            if not player:
                return False
            if not len(player[0].get('power_plants')) > 0:
                return False
            dispatch(pass_initial_bid(player_id))
        else:
            dispatch(pass_current_bid(player_id))
    else:
        if not valid_bid(player_id, amount, card, initial_state.get('game'), initial_state.get('players'), initial_state.get('market')):
            return False
        dispatch(set_current_bid(player_id, card, amount))

    if bid_is_won(get_state().get('game'), num_players):
        dispatch(win_current_bid())

        current_bid = get_state().get('game').get('current_bid')
        dispatch(add_power_plant(current_bid.get('player_id'), current_bid.get('card')))
        dispatch(change_money(current_bid.get('player_id'), -1 * current_bid.get('amount')))
        dispatch(purchase_card(get_state().get('market').get('current').index(current_bid.get('card'))))

        next_plant = get_state().get('deck')[0]
        dispatch(draw_card())
        dispatch(add_card(next_plant))

        dispatch(clear_bid())

    if len(get_state().get('game').get('bought_or_passed')) == num_players:
        dispatch(next_phase())
        dispatch(clear_bought_or_passed())
        dispatch(clear_bid())
    dispatch(set_current_player(get_next_player(get_state().get('game'), get_state().get('players'))))

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

    player = [pl for pl in initial_state.get('players') if pl.get('player_id') == player_id]
    if not player:
        return False

    if len(player[0].get('power_plants'))!= 4:
        return False

    dispatch(remove_power_plant(player_id, card))
    dispatch(set_current_player(get_next_player(get_state().get('game'), get_state().get('players'))))

    return True


def bid_is_won(game_state, num_players):
    bought_or_passed = game_state.get('bought_or_passed')
    passed = game_state.get('current_bid').get('passed')

    # All but one player passed on the bid,
    if len(passed) + len(bought_or_passed) == num_players - 1 and game_state.get('current_bid').get('card'):
        return True

    return False


def get_next_player(game_state, players):
    bought_or_passed = game_state.get('bought_or_passed')
    total_players = len(players)

    players_with_4_plants = [player for player in players if len(player.get('power_plants')) == 4]
    if len(players_with_4_plants) > 0:
        return players_with_4_plants[0].get('player_id')

    if len(bought_or_passed) == 0 and game_state.get('phase') == 3:
        # The next phase is resources, so the last player goes first
        return game_state.get('player_rank')[total_players - 1]

    bidding_order = game_state.get('bidding_order')
    player_id = game_state.get('current_player')
    bidding_order_index = bidding_order.index(player_id)
    for player_id in bidding_order[bidding_order_index + 1:] + bidding_order[:bidding_order_index + 1]:
        if player_id not in bought_or_passed + game_state.get('current_bid').get('passed'):
            return player_id
    return None


def valid_bid(player_id, amount, card, game_state, players, market):
    current_bid = game_state.get('current_bid')
    # All of these fields must be present
    if not all([player_id, amount, card]):
        return False

    if amount <= current_bid.get('amount'):
        return False

    # This is not a valid card to bid on
    if card not in market.get('current'):
        return False

    # Not allowed to bid on another card if a bid is currently going
    if current_bid.get('card') and current_bid.get('card') != card:
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

