def is_player_turn(store, request):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            player_id = request.json.get('player_id')
            state = store['get_state']()
            print(player_id, state.get('game').get('current_player'))
            if state.get('game').get('current_player') != player_id:
                return state
            return func(*args, **kwargs)
        return wrapped_func
    return decorator
