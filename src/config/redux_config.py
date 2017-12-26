import src.decorators.connect as connect_decorator
from vendor.python_redux import create_store, combine_reducers
from src.reducers import game, players, game_map, resources, deck, market

# Setup the redux store
store = create_store(combine_reducers({
    'game': game,
    'players': players,
    'game_map': game_map,
    'resources': resources,
    'deck': deck,
    'market': market
}))
connect_decorator.initialize(store)


def configure():
    return store