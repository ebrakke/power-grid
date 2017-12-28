from src.decorators.connect_to_store import connect
from src.actions.players_actions import add_player
from hashlib import md5
from random import random

@connect
def join_game(**kwargs):
    get_state = kwargs['get_state']
    dispatch = kwargs['dispatch']
    player_id = md5(str(random()).encode('utf-8')).hexdigest()
    dispatch(add_player(player_id))
    # Return the players id
    return player_id
