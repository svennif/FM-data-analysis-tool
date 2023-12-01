def calculate_speed_workrate_score(player_data):
    player_data['Spd'] = (
        player_data['Pac'] + player_data['Acc']) / 2
    player_data['Work'] = (
        player_data['Wor'] + player_data['Sta']) / 2
    player_data['SetP'] = (
        player_data['Jum'] + player_data['Bra']) / 2
    return player_data