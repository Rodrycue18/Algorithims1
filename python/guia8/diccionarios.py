def agrupar_por_long(archivoOrigen):
    archivo = open(archivoOrigen,"r",encoding='utf8')
    contenido = []
    for lineas in archivo.readlines():
        contenido.append(lineas.split())
    archivo.close()
    return contenido

archivo = "D:\IntroProgra\python\guia8\ejDiccionario.txt"

print(agrupar_por_long(archivo))