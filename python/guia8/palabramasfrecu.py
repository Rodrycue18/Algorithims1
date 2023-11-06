
def cantDeApariciones(origendeArchivo):
    archivo = open(origendeArchivo,"r")
    dicc= {}

    for linea in archivo.readlines():
        palabras = linea.split()
        for palabra in palabras:
            if palabra in dicc:
                dicc[palabra] = dicc[palabra] + 1
            else:
                dicc[palabra] = 1
    archivo.close()
    return dicc

def palabraFrecuente(origenArchivo):
    dicc = cantDeApariciones(origenArchivo)
    aux = 0
    for clave, valor in dicc.items():
        
        if valor > aux:
            aux = valor
            palabrafrec = clave
        
    return f"la palabra frecuente es {palabrafrec} y su cant es {aux}"
print(palabraFrecuente("D:\IntroProgra\python\guia8\palabrasFrec.txt"))