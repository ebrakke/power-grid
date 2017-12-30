from src.decorators.connect_to_store import connect


@connect
def buy_resource(request, **kwargs):
    """Handle how a player can buy resources"""
    get_state = kwargs['get_state']
    dispatch = kwargs['dispatch']

    # dict representing what the player is buying
    resources_to_buy = request.get('resources')
    player_id = request.get('player_id')
    state = get_state()

    # Get the player
    player = [pl for pl in state.get(
        'players') if pl.get('player_id') == player_id]
    if not player:
        return False

    current_resource_bank = state.get('resources').get('current_resource_bank')
    resource_costs = [get_available_resource_costs(
        r, resources_to_buy.get(r), current_resource_bank) for r in resources_to_buy]

    # Validation

    # Check that the player has enough money to buy these resources
    if not player_has_sufficient_funds(resource_costs, player):
        return False

    # Check that there exists enough resources for the player to buy
    if not bank_has_enough_resources(resources_to_buy, current_resource_bank):
        return False

    # Check that the player can store these resources


def get_available_resource_costs(resource, amount, current_resource_bank):
    """Returns the costs for the resource to purchase"""
    costs = [[i + 1] * r.get(resource)
             for (i, r) in enumerate(current_resource_bank)
             if r.get(resource) != 0]
    flattened = [c for bucket in costs for c in bucket]
    return sum(flattened[:amount])


def player_has_sufficient_funds(costs, player):
    total_cost = sum(costs)
    return player.get('money') > total_cost


def bank_has_enough_resources(resources_to_buy, current_resource_bank):
    bank_totals = dict(coal=0, oil=0, uranium=0, gas=0)
    for bucket in current_resource_bank:
        for r in bucket:
            bank_totals[r] += bucket.get(r)

    for resource in resources_to_buy:
        if bank_totals.get(resource) < resources_to_buy.get(resource):
            return False
    return True


def player_can_store_resources(resources_to_buy, player):
    # Add resources to play and see if they have enough powerplants to store them
    for resource in resources_to_buy:
        player['resources'][resource] += resources_to_buy[resource]

    total_storage = sum([p.get('generators') for p in player['power_plants']])
    player_total_resources = sum([player['resources'][r]
                                  for r in player['resources']])
    # Can't store more than twice the amount of pp generators
    if player_total_resources > total_storage * 2:
        return False

    # Can they fit on the powerplants
    partitions = [(p, p['resource_cost'] * 2, p['resources'])
                  for p in player['power_plants']]
