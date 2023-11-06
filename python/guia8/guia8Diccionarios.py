from queue import LifoQueue as Pila
def convertir_a_dicc(lista):
    res = {}
    for i in lista:
        if i in res:
            res[i]= res[i]+1
        else:
            res[i] = 1
    return res
lista = [-1, 0, 4, 100, 100, -1, -1]
#print(convertir_a_dicc(lista))

historiales = {}

def visitarSito(historial,usuario,sitio):
    pilasites = Pila()
    if usuario in historial.keys():
        historial[usuario] = pilasites.put(sitio)
    else:
        historial[usuario] = pilasites
        historial[usuario] = pilasites.put(sitio)
    return historial
a = visitarSito(historiales,"rodrigo","www.youtu.com")
b = visitarSito(historiales,"rodrigo","www.amazon.com")
c = visitarSito(historiales,"pablo","www.instagram.com")
print(historiales)