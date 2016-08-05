import requests
import time

api_url = 'http://localhost:5000/'
state = {}

def get_game_state():
  global state
  state = requests.get(api_url).json()

def make_bid_request(card, amount):
  data = {
    'player_id': player_id,
    'card': card,
    'amount': amount
  }
  requests.post(api_url + 'bid', json=data)

player_id = requests.post(api_url + 'join', json={}).json().get('player_id')
get_game_state()

while True:
  get_game_state()
  print(state['game']['current_bid'])
  print(player_id)
  if not state['game'].get('current_bid'):
    card = max(state['market']['current'], key=lambda x: x['market_cost'])
    make_bid_request(card, card['market_cost'])
  elif state['game']['current_bid']['player_id'] != player_id:
    card = state['game']['current_bid']['card']
    make_bid_request(card, state['game']['current_bid']['amount'] + 1)
  
  time.sleep(5)
  
