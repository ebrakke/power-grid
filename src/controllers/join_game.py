from random import choice
from string import ascii_lowercase
from src.actions.players_actions import create_player


def join_game(data, store):
  name = data.get('name')
  if name is None:
    name = ''.join([choice(ascii_lowercase) for i in range(5)]) + ' ' + ''.join([choice(ascii_lowercase) for i in range(5)])
  store['dispatch'](create_player(name))
  state = store['get_state']()
  # Return the players id
  return [player.get('id') for player in state['players'] if player.get('name') == name][0]