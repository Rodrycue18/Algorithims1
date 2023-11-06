from queue import LifoQueue as Pila
def agrupar_por_long(archivoOrigen):
    archivo = open(archivoOrigen,"r",'utf8')
    contenido = []
    for lineas in archivo.readlines.split():
        contenido.append(lineas)
    return contenido

archivo = "ejdiccionario.txt"

# print(agrupar_por_long(archivo))
# pilaRodri = Pila()
# pilaPablo = Pila()
# historiales = {
#     "Rodrigo":pilaRodri,
#     "pablo":pilaPablo
# }
historiales1={}
historiales_adelante={}
def visitar_sitio(historiales:dict,usuario,sitio):
    
    if usuario in historiales.keys():
        # pilaAntigua:Pila = pilaNueva
        registeredUserPila = historiales.get(usuario)
        registeredUserPila.put(sitio)
    else:
        a = creadorDePilas(historiales,usuario)
        pila_user = a.get(usuario)
        pila_user.put(sitio)

def creadorDePilas(historial,usuario):
    pila = Pila()
    historial[usuario] = pila
    return historial
# def visitar_sitio1(historiales,usuario,sitio):
#     for user in historiales.keys():
#         if user == usuario:
#             pila = historiales.get(user)
#             pila.put(sitio)
def navegar_atras(historial,usuario):
    pilaaux = Pila()
    pilauser = historial.get(usuario)
    sitio = pilauser.get()
    pilaaux.put(sitio)

def navegar_adelante(historial,usuario):
    
    pass
visitar_sitio(historiales1,"Rodrigo","youtube.com")
visitar_sitio(historiales1,"Pablo","youtube.com")
visitar_sitio(historiales1,"Rodrigo","ig.com")
visitar_sitio(historiales1,"Pablo","gaturro.com")
navegar_atras(historiales1,"Rodrigo")
navegar_atras(historiales1,"Pablo")
pass
