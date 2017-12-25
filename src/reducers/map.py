"""Manages the state for the map portion of the game state"""
import json
import os.path
CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
MAP_COLORS = json.loads(
    open(os.path.join(CURRENT_PATH, '../config/map_colors.json')).read())
MAP_COSTS = json.loads(
    open(os.path.join(CURRENT_PATH, '../config/map_costs.json')).read())


def get_playable_cities(*colors):
    """ Returns a list of cities that are playable based on the colors"""
    cities = [k for k in MAP_COLORS if MAP_COLORS.get(k) in colors]
    return cities

# Just return all cities


def initial_board():
    """ Returns the initial board for the game
    This does not include the costs of moving between cities"""
    board = dict()
    for country in MAP_COLORS:
        board[country] = {'0': None, '1': None, '2': None}
    return board

# main reducer


def game_map(state=None, action=None):
    """ The reducer for the boarder state"""
    if state is None:
        state = initial_board()
    if action is None:
        return state

    action_type = action.get('type')
    if action_type == 'REMOVE_COLOR':
        # remove cities of the specified color
        cities_to_remove = [
            city for city in MAP_COLORS if MAP_COLORS[city] == action.get('color')]
        new_state = {key: state[key]
                     for key in state if key not in cities_to_remove}
        return new_state

    if action_type == 'BUILD_IN_CITY':
        # add player to city if not already in city
        player_id = action.get('player_id')
        new_state = dict(state)
        new_state[action.get('city')][action.get('slot')] = player_id
        return new_state

    return state
