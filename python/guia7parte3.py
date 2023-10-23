import random
import numpy as np
from guia7 import ordenados
def aprobado (notas:list) -> int:
    sumatoria = 0
    for i in range(len(notas)):
        sumatoria = sumatoria + notas[i]
    promedio = sumatoria / len(notas)

    if revisadorDenotas(notas) and promedio >= 7:
        return 1
    elif revisadorDenotas(notas) and (promedio >= 4 and promedio<7):
        return 2
    elif revisadorDenotas(notas) or promedio < 4:
        return 3
def revisadorDenotas (notas):
    for i in notas:
        if i < 4:
            return False
    return True

# print(aprobado([10,10,1,5,5]))

def ingresarEstudiantes():
    nombres = []
    nombre = ""
    while nombre != "listo":
        nombre = str(input("Ingrese Nombres /n "))
        nombres.append(nombre)
    return nombres

# print(ingresarEstudiantes())
def sube ():
    historial = []
    palabra = ""
    while palabra != "X":
        palabra = str(input("Ingrese C o D \n"))
        monto = int(input("Ingrese monto \n"))
        tupla = (palabra,monto)
        if palabra == "C":
            historial.append(tupla)
        elif palabra == "D":
            historial.append(tupla)
    return historial

#print(sube())
## PODRIA DIVIDIR ESTO EN FUNCIONES PARA QUE EL CODIGO NO SE VEA TAN ILEGIBLE
def juego ():
    historial = []
    carta = random.randint(1,12)
    puntaje= carta
    historial.append(carta)
    if carta == 10 or carta == 11 or carta ==12:
        puntaje = 0.5
    print(puntaje)
    if puntaje >= 7.5:
            print(f"perdiste {puntaje}") 
            return historial
    user = str(input("Quieres continuar?"))
    while user != "plantarse":
        carta = random.randint(1,12)
        historial.append(carta)
        if carta == 10 or carta == 11 or carta ==12:
            carta = 0.5
        puntaje = puntaje + carta
        if puntaje >= 7.5:
            print(f"perdiste {puntaje}") 
            return historial
        print(puntaje)
        user = str(input("Quieres continuar?"))
    print(f"Ganaste {puntaje}") 
    return historial
#print(juego())

def esMatriz (matriz:list) -> bool:
    if len(matriz)>0 and len(matriz[0])>0 and otrosElem(matriz):
        return True
    else:
        return False

def otrosElem(matriz):
    aux = []
    for i in range(len(matriz)):
        aux.append(len(matriz[i])==len(matriz[0]))
    if False in aux:
        return False
    else:
        return True
    
#otrosElem([["mesi","pasmne","cris","pepe"],[7,8,9]])
#print(esMatriz([["mesi","pasmne","cris"],[7,8,2,9]]))

def filasOrdenadas(matriz):
    res = []
    for i in range(len(matriz)):
        res.append(ordenados(matriz[i]))
    return res

#print(filasOrdenadas([[1,2,3],[7,8,2]]))

#m = np.random.random((2,2))**2
m = np.random.randint(1,1000, (2, 2))**3
print(m)