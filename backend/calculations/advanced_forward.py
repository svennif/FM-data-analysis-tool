def calculate_advanced_forward_attack(player_data):
    # calculates Advanced_forward_Attack score
    player_data['afa_key'] = ( player_data['Acc'] + player_data['Pac'] + player_data['Fin'] )
    player_data['afa_green'] = ( player_data['Dri'] + player_data['Fir'] + player_data['Tec'] + player_data['Cmp'] + player_data['OtB'] )
    player_data['afa_blue'] = ( player_data['Pas'] + player_data['Ant'] + player_data['Dec'] + player_data['Wor'] + player_data['Agi'] + player_data['Bal'] + player_data['Sta'] )
    player_data['afa'] =( ( ( player_data['afa_key'] * 5) + (player_data['afa_green'] * 3) + (player_data['afa_blue'] * 1) ) / 37)
    player_data.afa= player_data.afa.round(1)
    return(player_data)
