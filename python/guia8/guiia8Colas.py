from queue import Queue as Cola
import random
def generar_nros_azar(n,desde,hasta):
    cola = Cola()
    for i in range(n):
        elem = random.randint(desde,hasta)
        cola.put(elem)
#print(generar_nros_azar(4,10,20))
colaGlobal = Cola()
for i in range(5):
        elem = random.randint(10,20)
        colaGlobal.put(elem)

def cant_elem(cola):
    cont = 0
    while not cola.empty():
        cola.get()
        cont += 1
    return f"La cantidad de elem es {cont}"
#print(cant_elem(colaGlobal))

def buscar_max(cola:Cola):
    aux = cola.get()
    while not cola.empty():
        num = cola.get()
        if num > aux:
            aux = num
    return f"El numero mayor es {aux}"
#print(buscar_max(colaGlobal))

def armar_sec_bingo(): #BOlillero
    cola = Cola()
    numeros = list(range(100))
    random.shuffle(numeros)
    for num in numeros:
        cola.put(num)
    return cola

#armar_sec_bingo()
# carton = []
# for i in range(25):
#     carton.append(random.randint(0,100))
carton = random.sample(range(100),25) #Crea lista de 25 numeros(0,100)random sin repetir 
def jugar_carton_bingo(carton:list[int],bolillero:Cola()):
    cont_jugadas = 0
    while not bolillero.empty():
        bolita = bolillero.get()
        cont_jugadas = cont_jugadas + 1

        if bolita in carton:
            carton.remove(bolita)
       
        if len(carton)==0:
            return cont_jugadas
    
    return -1
a = armar_sec_bingo()
carton1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
resp = jugar_carton_bingo(carton1,a)
print(resp)