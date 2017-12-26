def change_money(player_id, money):
    return dict(
        type='PLAYER_CHANGE_MONEY',
        player_id=player_id,
        money=money  # pos of neg value
    )


def add_power_plant(player_id, power_plant):
    return dict(type='PLAYER_ADD_POWER_PLANT', player_id=player_id, power_plant=power_plant)


def remove_power_plant(player_id, power_plant):
    return dict(type='PLAYER_REMOVE_POWER_PLANT', player_id=player_id, power_plant=power_plant)
