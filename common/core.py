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

#@TODO: Posiblemente usar? 
@dataclass
class Jugada():
    movimientos: str
    golpe: str
    dmg: int
    
    def get_damage_jugada(self):
        return self.dmg

@dataclass
class Player():
    hp: int
    nombre : str
    movimientos: List[str]
    golpes: List[str]
        
    def __str__(self) -> str:
        total_movimientos = self.get_botones_presionados(self.movimientos)
        total_golpes = self.get_botones_presionados(self.golpes)
        total = self.get_total_botones_presionados()
        return f"Player {self.nombre} - HP: {self.hp} - Movimientos: {total_movimientos} - Golpes: {total_golpes} - Total Botones: {total}"
    
    def __len__(self) -> int:
        """Retorna el total_botones_presionados"""
        return self.get_total_botones_presionados()
        
    def get_botones_presionados(self, button_array: List[str]) -> int:
        """ Retorna la cantidad de botones presionados total segun el array entregado (movimiento o golpe)"""
        count = 0
        for combo in button_array:
            for char in combo:
                count += 1
        return count
    
    def get_total_botones_presionados(self) -> int:
        total_mov = self.get_botones_presionados(self.movimientos)
        total_gol = self.get_botones_presionados(self.golpes)
        return total_gol + total_mov
 
    
def read_json_file(ruta_json: str) -> Dict:
    """Lee un archivo Json en ruta X, lo transforma a python dict"""
    with open(ruta_json, 'r', ) as file:
        data = json.load(file)
        return data