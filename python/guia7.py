import math
#lista:list=input("agrega la lista")
def pertenece (lista , elem:int) -> bool:
    for i in range(len(lista)):
        if elem == lista[i]:
            return True
   
    return False
#print(pertenece([1,2,3],4))

def pertence2(lista,elem):
    return elem in lista

#print(pertence2([1,2,3],2))

def sumatotal (lista):
    suma=0
    for i in lista:
        suma = suma+i
    print(suma)

#sumatotal([1,2,3,1])

def divideAtodos(lista:list, numero:int) -> bool:
    a=[]
    for i in range(len(lista)):
        if lista[i]%numero == 0:
            a.append(lista[i])
            print(a)
    
    if len(a)==len(lista):
        return True
    else:
        return False

#print(divideAtodos([2,6,8],2))

def divideAtodos1 (lista:list, numero:int) -> bool:
    for i in range(len(lista)):
        if lista[i]%numero != 0:
            return False
    return True

#print(divideAtodos1([2,5,8],2))

def ordenados (lista:list)->bool:
    for i in range(len(lista)-1):

        if lista[i]>lista[i+1]:
            return False
        
    return True

#print(ordenados([2,8,10]))

def palabraGrande (lista:list):
    for i in range(len(lista)):
        
        if len(lista[i])>=7:
            return True
        
    return False

#print(palabraGrande(["12345","12345","123456"]))

# p = "hola"
# for i in range(len(p)):
#     print(p[i])

######Ejercicio 7
def contrasena(contra):
    if len(contra) > 8 and mayuscula(contra) and minuscula(contra) and digito(contra):
        return "verde"
    elif len(contra) < 5:
        return "rojo"
    else: 
        return "amarillo"

def mayuscula(contra):
    for i in range(len(contra)):
        if (contra[i]>='A') and (contra[i]<='Z'):
            return True
    return False  
#'A'<=contra[i]<='Z'
def minuscula(contra):
    for i in range(len(contra)):
        if (contra[i]>='a') and (contra[i]<='z'):
            return True
    return False
#'a'<=contra[i]<='z'
def digito (contra):
    for i in range(len(contra)):
        if (contra[i]>='0') and (contra[i]<='9'):
            return True
    return False
#'0'<=contra[i]<='9'
#print(contrasena("Hola"))
#print(contrasena("HolasoyRodrigo708"))
#print(contrasena("Holasor"))

#####Ejercicio 8
def appBanco(lista):
    dineroCuenta=0
    for i in range(len(lista)):
        if ((lista[i])[0])=='I':
            dineroCuenta = ((lista[i])[1]) + dineroCuenta         
        elif((lista[i])[0])=='R':
            dineroCuenta = dineroCuenta - ((lista[i])[1])

    return dineroCuenta

#print(appBanco([('I',2000),('R',1000),('R',20),('I',300)]))

####Ejercicio 9
def vocales(palabra):
    vocal = 1
    for i in range(len(palabra)-1):
        if palabra[i] == palabra[i+1]:
            vocal = vocal + 1

    if vocal>=3:
        return False
    else:
        return True

#print(vocales("hooooooo"))

#Estamos modificando una variable GLOBAL
def borrarPares (lista:list) ->list:
    for i in range(0,len(lista),2):
        lista[i] = 0  

lista1 = [1,2,3,4,5,6] #valor original de la variable global
borrarPares(lista1)
#print(lista1)# valor actual despues de haber aplicado la funcion borrarPares

def borrarVocales(cadena):
    a = ""
    for i in range(len(cadena)):
        if (cadena[i]!="a" and cadena[i]!="e" and cadena[i]!="i" and cadena[i]!="o" and cadena[i]!="u"):
          a = a + cadena[i]
    return a
#print("borrarVocales:", borrarVocales("hola como estas Muriana"))

def perteneceACadaUno(lista, numero):
    a = []
    b = True
    c = False
    for i in range(len(lista)):
        a.append(numero in lista[i])
        # if numero in lista[i]:
        #     a.append(b)
        # else:
        #     a.append(c)
    return a

#print(perteneceACadaUno([[1,2,3],[2,1]], 3))

#Ejercicio 9
#ejem bubleSort
#ESTA MAL EL EJERCICIO xd
vocal = list("aeiou")
def vocalesRepitidas (palabra):
    a=[]
    for i in palabra:
        for j in vocal:
            if i==j:
                a.append(i)
    if a.count('a') >= 2 or a.count('e') >= 2 or a.count('i') >= 2 or a.count('o') >= 2 or a.count('u') >= 2:
        return False
    return True
#print(vocalesRepitidas("holatyytytei"))

