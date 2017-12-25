import json
from vendor.python_redux import create_store, combine_reducers
from src.reducers import game, players, game_map, resources, deck, market
from src.controllers import bid, start_game, join_game
from src.decorators import is_player_turn
from flask_api import FlaskAPI
from flask import request

app = FlaskAPI(__name__)

# Setup the redux store
store = create_store(combine_reducers({
    'game': game,
    'players': players,
    'game_map': game_map,
    'resources': resources,
    'deck': deck,
    'market': market
}))

# This will setup the game for players
start_game(store)


@app.route('/', methods=['GET'])
def state():
    return store['get_state']()


@app.route('/bid', methods=['POST'])
@is_player_turn(store, request)
def handle_bid():
    if request.method == 'POST':
        # handle the bid action
        bid(request.json, store)
        return store['get_state']()
    return store['get_state']()


@app.route('/join', methods=['POST'])
def handle_join():
    if request.method == 'POST':
        player_id = join_game(store)
        return {'player_id': player_id}


if __name__ == '__main__':
    app.run(debug=True)
