def contarLineas(origenArchivo):
    cont = 0
    archivo = open(origenArchivo, "r",encoding='utf8')
    for lineas in archivo.readlines():
        cont = cont + 1
    archivo.close()
    return f"La cantidad de lineas es {cont}"
#print(contarLineas("D:\IntroProgra\python\guia8\ej1contarLineas.txt"))

def existePalabra(palabra:str,origenArchivo:str)->bool:
    archivo = open(origenArchivo, "r",encoding='utf8')
    contenido = []
    for lineas in archivo.readlines():
        contenido.append(lineas)
    archivo.close()
    for palabras in contenido:
        if palabra in palabras:
            return True
        else:
            return False

#print(existePalabra("hola","D:\IntroProgra\python\guia8\ej1contarLineas.txt"))

def cantidad_de_palabras(palabra:str,origenArchivo:str)->bool:
    archivo = open(origenArchivo, "r",encoding='utf8')
    contenido = []
    cont = 0
    palabras = ""
    for letra in archivo.read(): #AGRUPAMOS TODAS LAS LEETRAS EN PALABRAS
        if letra == ' ' or letra == '\n': # TAMBIEN PODEMOS USAR el operador .split() Divide las cosas en palabras
            contenido.append(palabras.lstrip())
            palabras = ""
        palabras = palabras + letra
    archivo.close()

    for j in contenido: #Hacemos cuenteo de las veces que la palabra aparece
        if palabra in j:
            cont = cont + 1
    
    return f"la cantidad de apariciones de {palabra} es {cont}"

#print(cantidad_de_palabras("bien","D:\IntroProgra\python\guia8\ej1contarLineas.txt"))

def agregarFraseAlFinal(frase,archivoOrigen):
    archivo = open(archivoOrigen, "r",encoding='utf8')
    contenido = []
    for lineas in archivo.readlines():
        contenido.append(lineas)
    
    contenido.append("\n"+frase)
    archivo.close()

    archivoRescrito = open(archivoOrigen, "w",encoding='utf8')
    archivoRescrito.truncate()
    
    for linea in contenido:
        archivoRescrito.write(linea)
    
    archivoRescrito.close()

#agregarFraseAlFinal("yo tambien",'D:\IntroProgra\python\guia8\ej4agregar.txt')

def agregarFraseAlInicio(frase:str,archivoOrigen:str):
    archivo = open(archivoOrigen, "r",encoding='utf8')
    contenido = []
    for lineas in archivo.readlines():
        contenido.append(lineas)
    
    contenido.insert(0,frase + "\n")
    archivo.close()

    archivoRescrito = open(archivoOrigen, "w",encoding='utf8')
    archivoRescrito.truncate()
    
    for linea in contenido:
        archivoRescrito.write(linea)
    
    archivoRescrito.close()

#agregarFraseAlInicio("yo soy un kakahuate",'D:\IntroProgra\python\guia8\ej4agregar.txt')