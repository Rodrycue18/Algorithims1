from queue import LifoQueue as Stack
historiales = {}
historiales_adelante = {}


def vaciar_pila(s: Stack):
    while not s.empty():
        s.get()


def ver_historiales(usuario: str):
    print(" - historial:", list(historiales[usuario].queue))
    print(" - historial_del:", list(historiales_adelante[usuario].queue))


def visitar_sitio(historiales: [str, Stack], usuario: str, sitio: str):
    print(usuario, ": ( >>> goto ) ", sitio)
    # si no existe crearlo
    if not usuario in historiales.keys():
        historiales[usuario] = Stack()
        historiales_adelante[usuario] = Stack()

    # sabiendo que si existe,
    #   anterior al historial
    #   no queda nada "delante"
    historiales[usuario].put(sitio)
    vaciar_pila(historiales_adelante[usuario])

    ver_historiales(usuario)

    return


def navegar_atras(historiales: [str, Stack], usuario: str):
    print(usuario, ": (  <  back ) ")

    if not usuario in historiales.keys():
        return

    if historiales[usuario].qsize() == 1:
        print("\t - No puedes ir atras")
        return

    historiales_adelante[usuario].put(historiales[usuario].get())
    ver_historiales(usuario)

    return


def navegar_adelante(historiales: [str, Stack], usuario: str):
    print(usuario, ": (  >  forw ) ")

    if historiales_adelante[usuario].empty():
        print("\t - No puedes ir adelante")
        return

    historiales[usuario].put(historiales_adelante[usuario].get())
    ver_historiales(usuario)

    return


print("USER: marino ---------------------------------")

visitar_sitio(historiales, "marino", "www.mundogaturro.com")
visitar_sitio(historiales, "marino", "www.youtube.com")
visitar_sitio(historiales, "marino", "www.google.com")

navegar_atras(historiales, "marino")
navegar_atras(historiales, "marino")
navegar_atras(historiales, "marino")

navegar_adelante(historiales, "marino")
navegar_adelante(historiales, "marino")
navegar_adelante(historiales, "marino")

visitar_sitio(historiales, "marino", "www.discord.gg")
navegar_adelante(historiales, "marino")

print("USER: rodri ----------------------------------")

visitar_sitio(historiales, "rodri", "www.steam.com")
visitar_sitio(historiales, "rodri", "www.youtube.com")

navegar_adelante(historiales, "rodri")
navegar_atras(historiales, "rodri")
navegar_adelante(historiales, "rodri")

print("USER: Juan -----------------------------------")
visitar_sitio(historiales, "Juan", "google.com")
visitar_sitio(historiales, "Juan", "facebook.com")
navegar_atras(historiales, "Juan")
visitar_sitio(historiales, "Pedro", "youtube.com")
navegar_adelante(historiales, "Juan")

visitar_sitio(historiales,"Rodrigo","youtube.com")
visitar_sitio(historiales,"Pablo","youtube.com")
visitar_sitio(historiales,"Rodrigo","ig.com")
visitar_sitio(historiales,"Pablo","gaturro.com")
navegar_atras(historiales,"Rodrigo")
navegar_atras(historiales,"Pablo")
navegar_adelante(historiales,"Rodrigo")
pass