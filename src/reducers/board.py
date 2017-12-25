import json
import os.path
current_path = os.path.dirname(os.path.realpath(__file__))
map_colors = json.loads(
    open(os.path.join(current_path, '../config/map_colors.json')).read())
map_costs = json.loads(
    open(os.path.join(current_path, '../config/map_costs.json')).read())


def get_playable_cities(*colors):
    cities = [k for k in map_colors if map_colors.get(k) in colors]
    return cities

# Just return all cities


def initial_board():
    board = dict()
    for country in map_colors:
        board[country] = [0, 0, 0]
    return board

# main reducer


def board(state=None, action=None):
    if state is None:
        state = initial_board()
    if action is None:
        return state

    ty = action.get('type')
    if ty == 'REMOVE_COLOR':
        # remove cities of the specified color
        cities_to_remove = [
            city for city in map_colors if map_colors[city] == action.get('color')]
        new_state = {key: state[key]
                     for key in state if key not in cities_to_remove}
        return new_state

    if ty == 'BUILD_IN_CITY':
        # add player to city if not already in city
        current_city_building = state[action.get('city')]
        player_id = action.get('player_id')
        new_state = dict(state)
        new_state[action.get('city')][action.get('slot')] = player_id
        return new_state

    return state
