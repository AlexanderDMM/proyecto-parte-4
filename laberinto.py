from typing import List, Tuple

def crear_laberinto(cadena_laberinto: str) -> List[List[str]]:
    filas = cadena_laberinto.strip().split("\n")
    laberinto = [list(fila) for fila in filas]
    return laberinto

def mostrar_laberinto(laberinto: List[List[str]]):
    limpiar_pantalla()
    for fila in laberinto:
        print("".join(fila))

def mover_jugador(laberinto: List[List[str]], posicion_inicial: Tuple[int, int], posicion_final: Tuple[int, int]):
    px, py = posicion_inicial

    while (px, py) != posicion_final:
        laberinto[py][px] = 'P'
        mostrar_laberinto(laberinto)
        tecla = input("Presiona una tecla (flecha arriba, abajo, izquierda o derecha): ")
        laberinto[py][px] = '.'
        if tecla == "flecha arriba" and py > 0 and laberinto[py - 1][px] != '#':
            py -= 1
        elif tecla == "flecha abajo" and py < len(laberinto) - 1 and laberinto[py + 1][px] != '#':
            py += 1
        elif tecla == "flecha izquierda" and px > 0 and laberinto[py][px - 1] != '#':
            px -= 1
        elif tecla == "flecha derecha" and px < len(laberinto[0]) - 1 and laberinto[py][px + 1] != '#':
            px += 1

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

cadena_laberinto = """
###############
#P#.........#.#
#.#.#######.#.#
#.#.#.....#.#.#
#.#.#.#.#.#.#.#
#...#...#...#.#
###############
"""

laberinto = crear_laberinto(cadena_laberinto)
mostrar_laberinto(laberinto)

posicion_inicial = (1, 1)
posicion_final = (12, 6)
mover_jugador(laberinto, posicion_inicial, posicion_final)