def agrupar_por_longitud(nombre_archivo: str) -> dict:
    resultado: dict = {}
 
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo.readlines(): # linea = ['a hola agruparPorLongitud\n']
            palabras = linea.split()      # palabras = ['a', 'hola', 'agruparPorLongitud']
            for palabra in palabras:      # palabra = 'a'
                longitud = len(palabra)
                if longitud in resultado:
                    #resultado[longitud] += 1
                    resultado[longitud] = resultado[longitud] + 1
                else:
                    resultado[longitud] = 1
 
    return resultado

archivo = "/home/clinux01/Escritorio/rodrigo/ejDicc.txt"
agrupar_por_longitud(archivo)

def frecuencias(nombre_archivo : str) -> dict:
    d: dict = {} # inicializando/creando el diccionario
 
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo.readlines(): # linea = ['a hola agruparPorLongitud\n']
            palabras = linea.split()      # palabras = ['a', 'hola', 'agruparPorLongitud']
            for palabra in palabras:      # palabra = 'a'
                if palabra in d:
                    # la palabra ya existe
                    # entonces incremento en 1 la cantidad de apariciones
                    d[palabra] = d[palabra] + 1
                    #d[palabra] += 1
                else:
                    # aparece por primera vez palabra
                    # la agrego al diccionario
                    d[palabra] = 1
    return d

def la_palabra_mas_frec(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        diccFrec = frecuencias(nombre_archivo)
        aux = 0
        for clave,valor in diccFrec.items():
            if valor > aux:
                aux = valor
                palabraFrec = clave
        return f"LA palabra mas frec es {palabraFrec}"

#print(la_palabra_mas_frec("/home/clinux01/Escritorio/rodrigo/ejFrecuencias.txt"))

def leer_csv(archivoOrigen):
    archivo = open(archivoOrigen,'r')
    contenido = []
    for lineas in archivo.readlines():
        palabras = lineas.split(',')
        contenido.append(palabras)
    return contenido

print(leer_csv("/home/clinux01/Escritorio/rodrigo/ejALum.csv"))