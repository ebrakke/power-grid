"""Manages the state for the map portion of the game state"""
import json
import os.path
from copy import deepcopy
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
MAP_COLORS = json.loads(
    open(os.path.join(CURRENT_PATH, '../config/map_colors.json')).read())
MAP_COSTS = json.loads(
    open(os.path.join(CURRENT_PATH, '../config/map_costs.json')).read())


def get_playable_cities(colors):
    """ Returns a list of cities that are playable based on the colors"""
    cities = [k for k in MAP_COLORS if MAP_COLORS.get(k) in colors]
    return cities


def initial_board(colors):
    """ Returns the initial board for the game
    This does not include the costs of moving between cities"""
    board = dict()
    for country in get_playable_cities(colors):
        board[country] = {'1': None, '2': None, '3': None}
    return board

# main reducer


def game_map(state=None, action=None):
    """ The reducer for the boarder state"""
    if state is None:
        # Hard coding in the 4 colors now
        state = initial_board(['brown', 'purple', 'red', 'yellow'])
    if action is None:
        return state

    action_type = action.get('type')
    if action_type == 'BUILD_IN_CITY':
        # add player to city if not already in city
        player_id = action.get('player_id')
        new_state = deepcopy(state)
        new_state[action.get('city')][action.get('slot')] = player_id
        return new_state

    return state
