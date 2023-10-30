import random
from queue import Queue as Cola
def armar_secuencia_de_bingo() -> Cola[int]:
    numeros: list[int] = list(range(100))
    random.shuffle(numeros)
    cola: Cola[int] = Cola()
 
    for num in numeros:
        cola.put(num)
 
    return cola

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
 
    #while bolillero:
    while not bolillero.empty():
        jugada: int = bolillero.get()
        jugadas += 1
 
        if jugada in carton:
            carton.remove(jugada)
 
            #if not carton:
            if len (carton) == 0:
                return jugadas
 
    return -1  # Si no se gano el bingo, se devuelve -1
 
 
''''''
bolillero = armar_secuencia_de_bingo()
carton = [4, 10, 25, 46, 60, 73, 84, 90, 33, 67, 78, 95,3,26,76,96,43,13,45,78,52,98,72]
jugadas = jugar_carton_de_bingo(carton, bolillero)
 
if jugadas != -1:
    print(f"Ganaste el bingo en {jugadas} jugadas")
else:
    print("No se gano el bingo.")
''''''