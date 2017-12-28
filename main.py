import src.decorators.connect_to_store as connect_decorator
from src.decorators import is_player_turn
from vendor.python_redux import create_store, combine_reducers
from src.reducers import game, players, game_map, resources, deck, market

from flask_api import FlaskAPI
from flask import request

# This will setup the game for players
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
from src.controllers import bid, start_game, join_game
app = FlaskAPI(__name__)


start_game.start_game()


@app.route('/', methods=['GET'])
def state():
    return store['get_state']()


@app.route('/bid', methods=['POST'])
@is_player_turn(store, request)
def handle_bid():
    if request.method == 'POST':
        # handle the bid action
        if bid(request.json, store):
            return store['get_state']()
        else:
            return False
    return store['get_state']()


@app.route('/join', methods=['POST'])
def handle_join():
    if request.method == 'POST':
        player_id = join_game.join_game(store)
        return {'player_id': player_id}


if __name__ == '__main__':
    app.run(debug=True)
