"""
Funciones genericas, clases, etc
"""
from dataclasses import dataclass
from typing import List
import json
from typing import Dict

# Para obtener los valores de cada combo / golpe
COMBO_TABLE = {
    "SAK"  : 3,
    "DSDP" : 3,
    "SDK"  : 2,
    "ASAP" : 2,
    "P"    : 1,
    "K"    : 1,
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
        # Primero revisamos si existe un combo establecido perfecto 
        combo_strings = COMBO_TABLE.keys()
        if jugada in combo_strings:
            return COMBO_TABLE[jugada]
         
        # Si no encontramos el combo tal cual, dividamos en partes     
        return 999
    
    def obtener_texto_jugada(self, jugada: str) -> str:
        """Recibe una jugada (mov + gol) y retorna el texto del turno """
        return f"Este turno estoy haciendo la jugada {jugada}!"

    def mensaje_victoria(self) -> None:
        """ Mensaje que presentara el player al ganar """
        print(f"{self.nombre} Ganó la partida con {self.hp} de HP restante")

    
def read_json_file(ruta_json: str) -> Dict:
    """Lee un archivo Json en ruta X, lo transforma a python dict"""
    with open(ruta_json, 'r', ) as file:
        data = json.load(file)
        return data