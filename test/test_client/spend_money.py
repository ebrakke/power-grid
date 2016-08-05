import requests
import time

api_url = 'http://localhost:5000/'
state = {}
player_id = 1

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

while True:
  get_game_state()
  card = max(state['market']['current'], key=lambda x: x['market_cost'])
  make_bid_request(card, card['market_cost'] + 1)
  time.sleep(10)
  
