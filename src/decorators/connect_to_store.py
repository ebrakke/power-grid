"""Provides a way to get the state, and get a dispatch function
for a store"""

STORE = None


def initialize(store):
    global STORE
    STORE = store


def connect(func):
    global STORE
    if STORE is None:
        return func

    get_state = STORE['get_state']
    dispatch = STORE['dispatch']

    def wrapped_func(*args, **kwargs):
        kwargs['get_state'] = get_state
        kwargs['dispatch'] = dispatch
        return func(*args, **kwargs)
    return wrapped_func
