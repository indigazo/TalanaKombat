"""
Overview Practico:
1. Leer json file
    > Game_1 gana Arnarlord
    > Game_2 gana Tonyn
    > Game_3 gana Arnarlord
2. Mapear a dataclass para mayor orden y control
"""
import os
from typing import Dict, Tuple
from common.core import Player, read_json_file

# Globals
ROOT_JSON_PATH = 'json_files/'

def game_loop(player_1: Player, player_2: Player) -> None:
    """ En el contexto del game loop el player 1 es el que INICIA """
    print(f"Comienza jugando {player_1.nombre}")
    game_over = False
    current_player = player_1   
        
    def press_enter() -> str:
        """Detiene el juego para darle mejor 'feeling'"""
        print("presione ENTER para continuar")
        input()
        
        
    def switch_player(current_player: Player) -> Player:
        """Cambia al jugador actual por el otro jugador"""
        return player_1 if current_player == player_2 else player_2
    
        
    def check_game_state() -> bool:
        """Chequeamos si se acabo el juego"""
        if player_1.hp <= 0 or player_2.hp <= 0:
            return True
        return False
        
        
    def get_game_winner() -> Player:
        """ Retorna el jugador que gano """
        return player_1
        
    
    def ejecutar_jugada(jugada: str) -> None:
        print(f"Ejecutando tecnica {jugada}")
        dmg_jugada = current_player.obtener_dmg_jugada(jugada)
        mensaje_jugada = current_player.obtener_texto_jugada(jugada)                  
        
        # Causa el dmg en el otro jugador
        other_player = switch_player(current_player) 
        other_player.hp -= dmg_jugada
        other_player.hp = 0 if other_player.hp < 0 else other_player.hp # para que no salgan negativos

        # Da el mensaje del ataque 
        print(mensaje_jugada)        
        print(f"{other_player.nombre} recibio {dmg_jugada} de daño")
        print(f"A {other_player.nombre} le quedan {other_player.hp}/6 HP")
        
        
    def eliminar_jugada(current_player: Player) -> None:
        current_player.movimientos.remove(current_player.movimientos[0])
        current_player.golpes.remove(current_player.golpes[0])
        print(f"Jugadas disponibles: {current_player.get_jugadas()}")
    
    
    while not game_over:
        # player_1 hace su primera jugada
        print(f"Turno de {current_player.nombre}")
        current_player_plays = current_player.get_jugadas()
        print("Jugadas disponibles: ", current_player_plays)
        press_enter()
        
        # Ejecuta y borra la jugada que uso 
        if len(current_player_plays):
            
            # Ejecutamos la jugada 
            ejecutar_jugada(current_player_plays[0])
            
            # Limpiamos esa jugada del array 
            eliminar_jugada(current_player)
            press_enter()
        
        else:
            print(f"Player {current_player.nombre} no tiene plays disponibles")
            game_over = check_game_state()
            if game_over:
                break
            current_player = switch_player(current_player)
    
        # Se chequea si ya es hora de game over
        game_over = check_game_state()

        if game_over:
            break
    
        # proximo player juega 
        current_player = switch_player(current_player)
        print(f"Cambiamos al {current_player.nombre}")
        press_enter()
    
    print("Alguien gano!")
    winner = get_game_winner()
    winner.mensaje_victoria()


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
        for combo in player.movimientos:
            if len(combo) > 5:
                return False
        for combo in player.golpes:
            if len(combo) > 1:
                return False
    return True


def choose_first_player(players: Tuple[Player, Player]) -> Tuple[Player]:
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
        
        # Comenzar game loop
        second_player = player_arnaldor if starting_player.nombre == "Tonyn" else player_tonyn 
        game_loop(starting_player, second_player)
        
    
    else:
        print("Se ingreso un JSON con valores incorrectos:\n" + \
            "Verifique tener entre [0, 5] movimientos y " + \
            "entre [0, 1] golpes en el JSON")    

if __name__ == "__main__":
    main()
