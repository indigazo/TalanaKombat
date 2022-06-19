"""
Funciones genericas, clases, etc
"""
from dataclasses import dataclass
from email import message
from typing import List, Tuple
import json
from typing import Dict

# Para generar el mensaje de cada jugada 
MESSAGE_TABLE = {
    "Combo"  : "#player utiliza #habilidad causando #dmg de daño! ",
    "P"      : "#player da un puñetazo. casuando 1 de daño! ",
    "K"      : "#player da una patada. Causando 1 de daño! ",
    "W"      : "#player da un salto en el aire! ",
    "S"      : "#player se agacha! ",
    "A"      : "#player da un paso #orientacion. ",  # ej: Tonyn da un paso adelante/atras
    "D"      : "#player da un paso #orientacion. ",  # ej: Tonyn da un paso adelante/atras
}


# Para obtener los valores de cada combo / golpe
COMBO_TABLE = {
    "Tonyn": {
        "Taladoken" : { "DSDP" : 3 },
        "Remuyuken" : { "SDK"  : 2 },
        "Punch"     : { "P"    : 1 },
        "Kick"      : { "K"    : 1 }
    },
    "Arnaldor": {
        "Taladoken" : { "ASAP" : 2 },
        "Remuyuken" : { "SAK"  : 3 },
        "Punch"     : { "P"    : 1 },
        "Kick"      : { "K"    : 1 }
    },
}


@dataclass
class Player():
    """Clase principal del juego"""
    hp: int
    nombre : str
    movimientos: List[str]
    golpes: List[str]
        
        
    def __str__(self) -> str:
        total_movimientos = self.get_botones_presionados(self.movimientos)
        total_golpes = self.get_botones_presionados(self.golpes)
        total = len(self)
        return f"Player {self.nombre} - HP: {self.hp} - Movimientos: {total_movimientos} - Golpes: {total_golpes} - Total Botones: {total}"
    
    
    def __len__(self) -> int:
        """Retorna el total_botones_presionados"""
        total_mov = self.get_botones_presionados(self.movimientos)
        total_gol = self.get_botones_presionados(self.golpes)
        return total_gol + total_mov
    
        
    def get_botones_presionados(self, button_array: List[str]) -> int:
        """ Retorna la cantidad de botones presionados total segun el array entregado (movimiento o golpe)"""
        count = 0
        for combo in button_array:
            for char in combo:
                count += 1
        return count
    
    
    def get_jugadas(self) -> List[str]:
        """Retorna una lista de todas las jugadas, separando movimiento de golpes"""
        play_list = []
        for index, movimiento in enumerate(self.movimientos):
            play_string = movimiento + self.golpes[index]
            play_list.append(play_string)
        return play_list 
    
            
    def obtener_dmg_jugada(self, jugada: str) -> int:
        """Recibe una jugada (mov + gol) y retorna el dmg """
        combo_strings = COMBO_TABLE[self.nombre].keys()  # Segun nombre
        for tecnica in combo_strings:   # probamos cada tecnica
            for key in COMBO_TABLE[self.nombre][tecnica]:    # Obtenemos las button strings
                if key in jugada:
                    return COMBO_TABLE[self.nombre][tecnica][key]
        return 0
    
    
    def obtener_data_jugada(self, jugada: str) -> Tuple[int, str]:
        """Recibe una jugada (mov + gol) y retorna el dmg que se hizo y el mensaje que se debe mostrar """
        message_to_send = ""
        damage_to_send = 0
        is_combo = False
        combo_usado = ""
        
        # Obtener dmg y text desde COMBO_TABLE y MESSAGE_TABLE
        combo_strings = COMBO_TABLE[self.nombre].keys()  # Segun nombre
        for tecnica in combo_strings:   # probamos cada tecnica
            key = list(COMBO_TABLE[self.nombre][tecnica].keys())[0]
            if key in jugada:
                is_combo = True if len(key) > 1 else False
                combo_usado = tecnica
                damage_to_send = COMBO_TABLE[self.nombre][tecnica][key]
                if is_combo:
                    message_to_send = MESSAGE_TABLE["Combo"] \
                        .replace("#player", self.nombre) \
                        .replace("#habilidad", combo_usado) \
                        .replace("#dmg", str(damage_to_send))
                    break
                else:
                    # Se unen los ataques y movimientos
                    message_to_send = self.obtener_texto_movimientos(jugada)
                    message_to_send = message_to_send + MESSAGE_TABLE[key].replace("#player", self.nombre)
                    break
                
        # Aqui no se encontro nada de dmg
        # mostrar los movimientos si no se agrego nada en la pasada de arriba 
        if message_to_send == "":
            message_to_send = self.obtener_texto_movimientos(jugada)                  
        return (damage_to_send, message_to_send)


    def get_orientacion(self, boton_presionado: str) -> str:
        """Segun el boton presionado retorna la orientacion en la que el personaje dara el paso"""
        orientacion = ""
        if self.nombre == "Tonyn":
            orientacion = "adelante" if boton_presionado == "D" else "atrás"
        else:
            orientacion = "adelante" if boton_presionado == "A" else "atrás"                
        return orientacion
 
    
    def obtener_texto_movimientos(self, jugada: str) -> str:
        message_to_send = ""
        movements = [char for char in jugada if char not in ["P", "K"] ]
        for char in movements: 
            if char in ["W", "S"]:
                message_to_send = message_to_send + MESSAGE_TABLE[char].replace("#player", self.nombre)
            else:   # A y D requieren orientacion
                orientacion = self.get_orientacion(char)
                message_to_send = message_to_send + MESSAGE_TABLE[char].replace("#player", self.nombre).replace("#orientacion", orientacion)
        return message_to_send

        
    def mensaje_victoria(self) -> None:
        """ Mensaje que presentara el player al ganar """
        return f"{self.nombre} Ganó la partida con {self.hp} de HP restante"


    
# Otras funciones 
def read_json_file(ruta_json: str) -> Dict:
    """Lee un archivo Json en ruta X, lo transforma a python dict"""
    with open(ruta_json, 'r', ) as file:
        data = json.load(file)
        return data