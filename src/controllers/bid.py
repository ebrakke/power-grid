from src.actions.game_actions import bid_on_power_plant, next_player

def bid(data, store):
  """ Handle how to update the game when a player tried to bid on a market item"""
  player_id = data.get('player_id')
  amount = data.get('amount')
  card = data.get('card')
  
  state = store['get_state']()
  current_bid = state.get('game').get('current_bid')
  # All of these fields must be present
  if not all([player_id, amount, card]):
    return
  
  # This is not a valid card to bid on
  if card not in state.get('market').get('current'):
    return
  
  # Not allowed to bid on another card if a bid is currently going
  if current_bid and current_bid.get('card') != card:
    return
  
  action = bid_on_power_plant(player_id, card, amount)
  store['dispatch'](action)
  store['dispatch'](next_player())
  return
  