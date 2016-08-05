import json
from vendor.python_redux import create_store, combine_reducers
from src.reducers import game, players, board, resource, deck
from src.actions import *
from flask_api import FlaskAPI
from flask import request

app = FlaskAPI(__name__)

store = create_store(combine_reducers({
  'game': game,
  'players': players,
  'board': board,
  'resource': resource,
  'deck': deck
}))

@app.route('/', methods=['GET', 'POST'])
def state():
  if request.method == 'POST':
    action = request.json
    store['dispatch'](action)
    return store['get_state']()
  


if __name__ == '__main__':
  app.run(debug=True)


