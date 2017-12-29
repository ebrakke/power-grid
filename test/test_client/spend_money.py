import requests
import time
import pprint
import random
from datetime import datetime

api_url = 'http://localhost:5000/'
state = {}
player_ids = []
max_bids = [random.randint(15, 20), random.randint(15, 20), random.randint(15, 20), random.randint(15, 20)]


def get_game_state():
    global state
    state = requests.get(api_url).json()


def make_bid_request(player_id, card, amount):
    data = {
        'player_id': player_id,
        'card': card,
        'amount': amount
    }
    requests.post(api_url + 'bid', json=data)

while len(player_ids) < 4:
    player_ids.append(requests.post(api_url + 'join').json().get('player_id'))

get_game_state()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(state)

while state['game']['phase'] == 2:
    get_game_state()
    current_player_index = player_ids.index(state['game']['current_player'])
    current_player_name = player_ids[current_player_index]
    max_bid = max_bids[current_player_index]
    print("Bidding as Player {}. My max bid limit is {}".format(current_player_name, max_bid))
    # There is not bid, so bid on the maximum card
    if not state['game'].get('current_bid').get('card'):
        card = max(state['market']['current'], key=lambda x: x['market_cost'])
        amount = card['market_cost']
        if amount <= max_bid:
            print("Player {} is bidding on {} -- {}/{}".format(current_player_name,
                                                               card, amount, max_bid))
            make_bid_request(current_player_name, card, card['market_cost'])
        else:
            print("Player {} is passing on {} -- {}/{}".format(current_player_name,
                                                               card, card.get('market_cost'), max_bid))
            make_bid_request(current_player_name, card, 0)

    # Try to outbid the top player
    else:
        current_bid = state['game'].get('current_bid')
        if current_bid.get('amount') < max_bid:
            print("Player {} is bidding on {} -- {}/{}".format(current_player_name,
                                                               card, current_bid.get('amount') + 1, max_bid))
            make_bid_request(current_player_name, card, current_bid.get('amount') + 1)
        else:
            print("Player {} is passing on {} -- {}/{}".format(current_player_name,
                                                               card, current_bid.get('amount'), max_bid))
            make_bid_request(current_player_name, card, 0)

get_game_state()
print("Bidding is over")
pp.pprint(state)
