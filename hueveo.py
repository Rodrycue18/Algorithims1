#Sort [4,5,2,3,1] -> [1,2,3,4,5]
import random
import time
start_time = time.time()
#Primero el mas pequeno y lo apendeamos a una lista nueva, con un while o if si la lista nueva no tiene
#el mismo tamano que la original siga iterando entre numeros y cuando en cuentre erl mas pequeno elimine
# ese elemento de la l;ista original
def sort(lista): # notamos que al pasar por valo9r la copia de la lista elimina suis elems al igual que la original
    res = []
    tamanoog = len(lista)
    aux = lista[0]
    while len(res) != tamanoog:
        for num in lista:
            if num < aux:
                aux = num 
        res.append(aux)
        lista.remove(aux)
        if len(lista) == 0:
            aux = 0
        else:
            aux = lista[0]
    return res
a = list(range(10000))
random.shuffle(a)
print(a)
print(sort(a))
print ("My program took", time.time() - start_time, "to run")
