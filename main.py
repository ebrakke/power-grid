from src.config import redux_config
from src.controllers import bid, start_game, join_game
from src.decorators import is_player_turn

from flask_api import FlaskAPI
from flask import request

app = FlaskAPI(__name__)

# This will setup the game for players
store = redux_config.configure()
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
