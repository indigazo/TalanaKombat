# Notes

## Overview
Juego de 2 personajes. Cada personaje 
tiene 2 golpes especiales que se ejecutan 
con una combinación de movimientos + 1 botón de golpe.


## Objective
Recibir un JSON que indica como ocurrio el combate, narrarlo,
para eso debo crear el set de reglas y recibir un JSON como entrada.


## Botons
W : UP      P : PUNCH            
A : LEFT    K : KICK
S : DOWN
D : RIGHT


## Moveset
Tony
Combinación 	Energía que quita	Nombre del movimiento
DSD + P	        3	                Taladoken
SD + K	        2	                Remuyuken
P o K	        1	                Puño o Patada

Arnaldor
Combinación	    Energía que quita	Nombre del movimiento
SA + K	        3	                Remuyuken
ASA + P	        2	                Taladoken
P o K	        1	                Puño o Patada


## Rules

## Starting the game
-Comienza el jugador con la menor combinacion de BOTONES (mov + golp)

-En caso de empate en BOTONES:
Comienza el jugador con el menor numero de MOVIMIENTOS

-En caso de empate en MOVIMIENTOS:
Inicia el que tenga menor cantidad de GOLPES 

-En caso de empate de GOLPES:
Inicia el player 1

## Game rules
-Personaje muere cuando su HP llega a 0 y de inmediato finaliza la pelea (incluso si quedan movimientos)

-Tony es el P1, siempre ataca hacia la derecha (y no cambia de lado)

-Arnaldor es el P2, siempre ataca hacia la izquierda (y no cambia de lado)

-Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es derrotado 

-Los golpes no pueden ser bloqueados, se asume que siempre son efectivos. 


## Data rules 
- Los datos llegan de batalla llegan en formato JSON, todos de una vez (P1 y P2)
- Los datos son las secuencias de movimientos y botones consolidados segun jugada
{
    "player1": {
        "movimientos":["D","DSD","S","DSD","SD"], <- Cada entrada del array una jugada
        "golpes":["K","P","","K","P"] <- Golpe que se ejecuto luego de su correspondiente movimiento
    },
    "player2": {
        "movimientos":["SA","SA","SA","ASA","SA"],
        "golpes":["K","","K","P","P"]
    }
} 
- Player 
    movimientos: List[str] : max_len 5 (nullable)
    golpes: List[str] : max_len 1 (nullable)


## Output example

INPUT:
{
    "player1": {
        "movimientos":["D","DSD","S","DSD","SD"], 
        "golpes":["K","P","","K","P"]
    },
    "player2": {
        "movimientos":["SA","SA","SA","ASA","SA"],
        "golpes":["K","","K","P","P"]
    }
} 

OUTPUT:
➢ Tonyn avanza y da una patada 
➢ Arnaldor conecta un Remuyuken 
➢ Tonyn usa un Taladoken 
➢ Arnaldor se mueve 
➢ Tonyn le da un puñetazo al pobre Arnaldor 
➢ Arnaldor conecta un Remuyuken 
➢ Arnardold Gana la pelea y aun le queda 1 de energía
