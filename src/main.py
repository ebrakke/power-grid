from vendor.python_redux import create_store, combine_reducers
from .reducers import game, players, board, resource, deck
from .actions import *

store = create_store(combine_reducers({
  'game': game,
  'players': players,
  'board': board,
  'resource': resource,
  'deck': deck
}))


