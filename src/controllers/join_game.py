from src.decorators.connect_to_store import connect
from src.actions.players_actions import add_player
from src.actions.game_actions import set_bidding_order, set_player_rank, set_current_player, next_phase
from hashlib import md5
from random import random, shuffle

@connect
def join_game(**kwargs):
    get_state = kwargs['get_state']
    dispatch = kwargs['dispatch']
    player_id = 'player_' + md5(str(random()).encode('utf-8')).hexdigest()[:2]
    dispatch(add_player(player_id))
    new_state = get_state()
    players = new_state.get('players')
    if len(players) == 4:
        player_ids = [player.get('player_id') for player in players]
        shuffle(player_ids)
        dispatch(set_player_rank(player_ids))
        shuffle(player_ids)
        dispatch(set_bidding_order(player_ids))
        final_state = get_state()
        dispatch(set_current_player(final_state.get('game').get('player_rank')[0]))
        dispatch(next_phase())
    # Return the players id
    return player_id
