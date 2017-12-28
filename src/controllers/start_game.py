from src.actions.deck_actions import draw_card
from src.actions.market_actions import add_card
from src.decorators.connect_to_store import connect


@connect
def start_game(*args, **kwargs):
    get_state = kwargs['get_state']
    dispatch = kwargs['dispatch']
    state = get_state()
    first_eight_cards = state.get('deck')[:8]
    for card in first_eight_cards:
        # Add card to the market
        dispatch(add_card(card))
        # Remove the card from the top of the deck
        dispatch(draw_card())
