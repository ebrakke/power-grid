from src.actions.deck_actions import draw_card
from src.actions.market_actions import add_card

def start_game(store):
  state = store['get_state']()
  first_eight_cards = state.get('deck')[:8]
  for card in first_eight_cards:
    # Add card to the market
    store['dispatch'](add_card(card))
    # Remove the card from the top of the deck
    store['dispatch'](draw_card())

  