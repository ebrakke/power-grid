from src.actions.resource_actions import take_resource
from src.actions.game_actions import next_player

def buy_resources(data, store):
  """ Handle how to update the game when a player buys resources"""
  player_id = data.get('player_id')
  resource_request = data.get('resources')
  print(resource_request)
  
  state = store['get_state']()
  current_market = state.get('resource')
  # All of these fields must be present
  if not all([player_id, resource_request]):
    return
  
  for resource in resource_request:
    amount = resource_request[resource]
    available = current_market[resource]
    cost = self.cost_to_buy(available, resource, amount)
    if available < amount:
      # not enough available resources
      continue
    elif not self.player_has_enough_money(player_id, cost):
      continue
    else:
      action = take_resource(resource, amount)
      store['dispatch'](action)

  store['dispatch'](next_player())
  return
  
def player_has_enough_money(self, player_id, cost):
  # if the player can afford the requested transaction
  # raise NotImplementedError
  return True

def cost_to_buy(self, available, resource, amount):
  cost = {
    "gas" : [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8],
    "oil" : [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,9,9],
    "coal" : [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8,9,9],
    "uranium" : [1,2,3,4,5,6,7,7,8,8,9,9]
  }
  new_amount = available - amount
  prices = cost[rtype]
  cost = sum(prices[len(prices)-available : len(prices)-new_amount])
  return cost





