"""
Overview Practico:
1. Leer json file
    > Game_1 gana Arnarlord
    > Game_2 gana Tonyn
    > Game_3 gana Arnarlord
2. Mapear a dataclass para mayor orden y control
"""
from typing import Dict, Tuple
from common.core import Player, read_json_file

# Globals
ROOT_JSON_PATH = 'json_files/'


def game_loop() -> None:
    """ Cada "Turno" durara 1 segundo para que no se vea tan automatico"""
    return


def get_players_from_json(json_data: Dict) -> Tuple[Player, Player]:
    """Usando la data del json retornamos a 2 jugadores como un tuple"""
    player_1_data = json_data.get("player1")
    player_2_data = json_data.get("player2")
    
    player_1 = Player(
        hp = 6,
        nombre="Tonyn",
        movimientos = player_1_data.get("movimientos"),
        golpes = player_1_data.get("golpes")
    )
    player_2 = Player(
        hp = 6,
        nombre="Arnaldor",
        movimientos = player_2_data.get("movimientos"), 
        golpes = player_2_data.get("golpes")
    )
    return (player_1, player_2)


def players_are_valid(players: Tuple[Player, Player]) -> bool:
    """Verificamos que el json cumpla con las reglas"""
    for player in players:
        print(f"Verificando data player {player.nombre}")
        for combo in player.movimientos:
            if len(combo) > 5:
                return False
        for combo in player.golpes:
            if len(combo) > 1:
                return False
    print("")
    return True


def choose_first_player(players: Tuple[Player, Player]) -> Player:
    """ Usando las reglas, determina que jugador va primero """
    player_tonyn = players[0] 
    player_arnaldor = players[1]
    
    n_movimientos_tonyn = player_tonyn.get_botones_presionados(player_tonyn.movimientos)
    n_movimientos_arnaldor = player_arnaldor.get_botones_presionados(player_arnaldor.movimientos)
    
    n_golpes_tonyn = player_tonyn.get_botones_presionados(player_tonyn.golpes)
    n_golpes_arnaldor = player_tonyn.get_botones_presionados(player_arnaldor.golpes)
    
    # first rule: menos botones    
    if len(player_tonyn) != len(player_arnaldor):
        return player_tonyn if len(player_tonyn) < len(player_arnaldor) else player_arnaldor
    
    # second rule: menos movimientos
    if n_movimientos_tonyn != n_movimientos_arnaldor: 
        return player_tonyn if n_movimientos_tonyn < n_movimientos_arnaldor else player_arnaldor
    
    # third rule: menos golpes (Esta regla tal vez no es posible?)
    if n_golpes_tonyn != n_golpes_arnaldor: 
        return player_tonyn if n_golpes_tonyn < n_golpes_arnaldor else player_arnaldor
    
    print("Primero por defecto es el P1 ", player_tonyn.nombre)
    return player_tonyn


def main() -> None:
    # Obtener game data desde el json
    data = read_json_file(ROOT_JSON_PATH + 'game_1.json')
    players = get_players_from_json(data)
    
    if players_are_valid(players):
        # Mapear a una clase
        players = get_players_from_json(data)
        player_tonyn = players[0]
        player_arnaldor = players[1]
        
        # Decidir quien va primero
        starting_player = choose_first_player(players)
        print("Comienza jugando ", starting_player.nombre)
        
        # Comenzar game loop
        game_loop()
        
    
    else:
        print("Se ingreso un JSON con valores incorrectos:\n" + \
            "Verifique tener entre [0, 5] movimientos y " + \
            "entre [0, 1] golpes en el JSON")    




if __name__ == "__main__":
    main()
