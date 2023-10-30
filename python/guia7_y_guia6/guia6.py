import math
def suma (a: int , b:int):
    res:int = a + b
    return res

#print(suma(2,2))

#Guia 6 IMPERATIVO CON PYTHON
def imprimir_un_verso() -> None:
    p = "Somebody once told me \n The world is gonna roll me \n I ain't the sharpest tool in the shed \n She was looking kind of dumb \n With her finger and her thumb \n In the shape of an L on her forehead \n Well, the years start coming \n And they dont stop coming \nFed to the rules and I hit the ground running \n Didnt make sense not to live for fun \n Your brain gets smart, but your head gets dumb"
    print(p)

raizDeDos = round(math.sqrt(2),4)
#print(raizDeDos)

fact= math.factorial(2)
#print(fact)

perimetro = 2 * math.pi
#print(perimetro)

def imprimir_saludo (nombre:str):
    print("hola " + nombre)

#imprimir_saludo("juan")

def raiz_cuadrada(num:int):
    print(math.sqrt(num))

#raiz_cuadrada(10)

def fahrenheit_to_celsius(tempFar:float):
    print(((tempFar-32)*5)/9)

#fahrenheit_to_celsius(120)

def imprimir2vecesEstribillo(t:str):
    t*=2
    print(t)

#imprimir2vecesEstribillo(p)


def esMultiplo(n:int,m:int):
    if (n%m==0):
        return True
    else: 
        return False
#print(esMultiplo(4,2))
#print(esMultiplo(5,2))

def esPar(n:int):
    if(esMultiplo(n,2)):
        return True
    else:
        return False

#print(esPar(44444))

def cantidad_de_pizzas(comensales,min_cant_porciones):
    cantDePorciones = comensales * min_cant_porciones
    print(math.ceil(cantDePorciones/8))

#cantidad_de_pizzas(4,3)

#EJERCICIO 3
def alguno_es_cero(num1,num2):
    if num1==0 or num2==0:
        if num1==0:
            print("num1 es cero") 
        if num2==0:
            print("num2 es cero")


#alguno_es_cero(0,1)

def ambos_son_0(num1,num2):
    if num1==0 and num2==0:
        print("ambos son cero")

#ambos_son_0(0,0)

def es_nombre_largo(nombre):
    p = len(nombre)
    if (p>=3) and (p<=8):
        return True
    else:
        return False

#print(es_nombre_largo("hola"))

def es_bisiesto(ano):
    if (ano%4==0):
        print("es año bisiesto")
    else:
        print("no es año bisiesto")

#es_bisiesto(2024)

#EJERCICIO 4
def peso_pino(alturaMetros):
    alturaCm = alturaMetros * 100
    peso = min(alturaCm,300) * 3 + max(alturaCm-300,0)
    return peso

def peso_util(peso):
    if (peso>=400) and (peso<=1000):
        return True
    else:
        return False
    
def peso_util_alternativo(peso):
    res=min(max(peso,400),1000)
    return res==peso
    
def sirve_pino(altura):
    peso1 = peso_pino(altura)
    return peso_util_alternativo(peso1)
#version con if
#    if (peso_util(peso1)):
#        print("Pino que sirve")
#    else:
#        print("Pino que no sirve")

#print(sirve_pino(5))
#print(sirve_pino(2))

#EJERCICIO 6
def printNumeros():
    i=1
    while(i<=10):
        print(i)
        i=i+1

def print10al20():
    i=10
    while(i<=20):
        print(i)
        i=i+2

#print10al20()

def printeco():
    i=1
    while(i<=10):
        print("eco")
        i=i+1
#printeco()

def cuentaRegresiva (n:int):
    while(n>=1):
        print(n)
        n=n-1
    print("despeguen")
    
#cuentaRegresiva(10)
def viajeTiempo (anoInicio,anoFinal):
    ano = anoFinal
    anoContador = anoInicio
    while (ano<anoInicio):
        ano=ano+1
        anoContador=anoContador-1
        print("Viajo un ano al pasado, estamos en el año: ", anoContador)

#viajeTiempo(2022,2020)

def viajeAristoteles (anoInicio,anoAristoteles):
    anoAristoteles = 384
    anoContador = anoInicio
    while (anoAristoteles<anoInicio):
        anoAristoteles=anoAristoteles+20
        anoContador=anoContador-20
        print("Viajo un ano al pasado, estamos en el año: ", anoContador)
viajeAristoteles(2020,0)

    