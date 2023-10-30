import random
from queue import LifoQueue as Pila

def generar_nro_random(n,desde,hasta):
    pila = Pila()
    i = 0
    while i <= n:
        a = random.randint(desde,hasta)
        pila.put(a)
        i = i+1
    return list(pila.queue)

#print(generar_nro_random(11,10,20))

def buscar_max():
    pila = Pila()
    for i in range(10): #Creamos la pila
        numeros = random.randint(10,30)
        pila.put(numeros)

    aux = pila.get()

    while not pila.empty():
        aux1= pila.get()
        if  aux1 > aux:
            aux = aux1
    return f"El mayor valor de la pila es {aux}"

#print(buscar_max())

def esta_bien_balanceada(ecuacion):
    pila = Pila()
    cont_parentesis = 0
    for i in ecuacion:
        pila.put(i)
    
    while not pila.empty(): #recorremos la pila, y con un contador vemos si
        letra = pila.get()  # los parentesis se igualan osea si son cero
        if letra == ')':
            cont_parentesis = cont_parentesis + 1
        if letra == '(':
            cont_parentesis = cont_parentesis - 1

    if cont_parentesis == 0:
        return True
    else:
        return False
    
#print(esta_bien_balanceada("1 + (2 x 3 = ( 20 / 5)))"))

def postfix(ecuacion:str):
    pila = Pila() 
    for numero in ecuacion.split(): #split sirve para hacer que el string no tenga espacios
        if numero.isnumeric():
            pila.put(int(numero))
        elif not numero.isnumeric():
            num1 = pila.get()
            num2 = pila.get()
            if numero == '+':
                res = num1 + num2
                pila.put(res)
            elif numero == '-':
                res = num2 - num1
                pila.put(res)
            elif numero == '*':
                res = num1 * num2
                pila.put(res)
            elif numero == '/':
                res = num2 / num1
                pila.put(res)
    return f"La respuestas es {pila.get()}"
#print(postfix("3 4 + 5 * 2 -"))
