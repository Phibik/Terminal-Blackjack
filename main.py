from menus import *
from partida import partida
from records import records
from enum import IntEnum

class ev(IntEnum):
    INIT_GAME    = 0
    DEAL_INITIAL = 1
    PLAYER_TURN  = 2
    PLAYER_HIT   = 3
    PLAYER_STAND = 4
    DEALER_TURN  = 5
    RESOLVE_HAND = 6
    ROUND_END    = 7

while True:
    menuPrincipal()
    opcion = input("Selecciona una opción: ").lower()
    while opcion != "a" and opcion != "s" and opcion != "d" and opcion != "f" and opcion != "h":
        menuPrincipalParaEstupidos()
        opcion = input("Selecciona una opción: ").lower()

    match opcion:
        case "a":
            partida(17)
        case "h":
            partida(21)
        case "s":
            records()
        case "d":
            reglas()
        case "f":
            break

