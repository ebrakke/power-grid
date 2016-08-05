import json
from vendor.python_redux import create_store, combine_reducers
from src.reducers import game, players, board, resource, deck, market
from src.controllers import bid, start_game
from flask_api import FlaskAPI
from flask import request

app = FlaskAPI(__name__)

store = create_store(combine_reducers({
  'game': game,
  'players': players,
  'board': board,
  'resource': resource,
  'deck': deck,
  'market': market
}))

# This will setup the game for players
start_game(store)

@app.route('/', methods=['GET'])
def state():
  return store['get_state']()

@app.route('/bid', methods=['POST'])
def handle_bid():
  if request.method == 'POST':
    try:
      # handle the bid action
      bid(request.json, store)
      return store['get_state']()
    except Exception as e:
      print(str(e))
  return store['get_state']()
    
  


if __name__ == '__main__':
  app.run(debug=True)


