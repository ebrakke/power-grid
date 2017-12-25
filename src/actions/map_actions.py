def remove_color(color):
    return {
        'type': 'REMOVE_COLOR',
        'color': color
    }


def build_in_city(player_id, city, slot):
    return {
        'type': 'BUILD_IN_CITY',
        'player_id': player_id,
        'city': city,
        'slot': slot
    }
