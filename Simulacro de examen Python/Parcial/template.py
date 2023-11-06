# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s: list, e: int) -> int:
    for i in range(len(s)): # Otra manera seria recorrer desde atras for in in range(len(s),-1,-1)
        if s[i] == e:   #Agregamos la posicion cuando encontramos el elemento en una variable y esa variable va cambiando a medida
            aux = i     # de que encontramos el elemento
    return aux

lista = [-1,4,0,4,100,0,100,-1,-1]
print(ultima_aparicion(lista,0))
##########################################################################
##########################################################################

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }unittest.main(verbosity=2)

#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def elementos_exclusivos(s: list, t: list) -> list:
    res = []
    res_sin_reps=[]
    for i in s:
        if i not in t:
            res.append(i)
    for i in t:
        if i not in s:
            res.append(i)
    for i in res: #Eliminamos repetidos de la lista con elementos exclusivos
        if i not in res_sin_reps:
            res_sin_reps.append(i)
    
    return res_sin_reps

s = [1,5,7,2,3,7]
t = [1,2,3,4]
print(elementos_exclusivos(s,t))
##########################################################################
##########################################################################

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    cont = 0
    for clave, valor in ingles.items():
        for clave1, valor1 in aleman.items():
            if clave == clave1 and valor == valor1:
                cont = cont + 1
    return cont

aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht","Hola": "alo"}
ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand","nose":"dont know", "Hola": "alo"}
print(contar_traducciones_iguales(ingles,aleman))
##########################################################################
##########################################################################

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def convertir_a_diccionario(lista: list) -> dict:
    claves = [] #Primero eliminamos repetidos para las claves
    dicc = {}
    for i in lista: #Eliminamos repetidos de la lista con elementos exclusivos
        if i not in claves:
            claves.append(i)
    for clave in claves:
        cont = 0
        for j in lista:
            if clave == j:
                cont = cont + 1
        dicc[clave]= cont
        
    return dicc

print(convertir_a_diccionario(lista))