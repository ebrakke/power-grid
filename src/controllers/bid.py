from src.actions.game_actions import bid_on_power_plant, next_player


def bid(data, store):
    """ Handle how to update the game when a player tried to bid on a market item"""
    player_id = data.get('player_id')
    amount = data.get('amount')
    card = data.get('card')

    state = store['get_state']()
    if not valid_bid(player_id, amount, card, state):
        return False




    action = bid_on_power_plant(player_id, card, amount)
    store['dispatch'](action)
    store['dispatch'](next_player())
    return True

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

    player = [player for player in state.get('players') if player['player_id'] == player_id][0]
    # You can't bid more than you have
    if amount > player['money']:
        return False

