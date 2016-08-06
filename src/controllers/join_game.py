from src.actions.players_actions import create_player
from hashlib import md5
from random import random

def join_game(store):
  player_id = md5(str(random()).encode('utf-8')).hexdigest()
  store['dispatch'](create_player(player_id))
  state = store['get_state']()
  # Return the players id
  return player_id