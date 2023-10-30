from queue import Queue as Cola
def generador_de_cola_pacientes():
    cola = Cola()
    for i in range(5):
        prioridad,nombre,especialidad=input("Agrega info de pacientes ").split()
        tupla = (int(prioridad),str(nombre),str(especialidad))
        cola.put(tupla)
    return cola

#colaPacientes = generador_de_cola_pacientes()

def n_pacientes_urg(cola:Cola()):
    cont_urgencia = 0
    while not cola.empty():
        paciente = cola.get()
        if paciente[0]==1 or paciente[0]== 2 or paciente[0]==3:
            cont_urgencia = cont_urgencia + 1
    return f"La cantidad de pacientes urgentes es {cont_urgencia}"
 
#print(n_pacientes_urg(colaPacientes))

def generador_de_cola_banco():
    cola = Cola()
    for i in range(6):
        nombre,dni,cuenta,prioridad=input("Agrega info de pacientes ").split()
        tupla = (str(nombre),int(dni),bool(cuenta),bool(prioridad))
        cola.put(tupla)
    return cola

#colaBanco = generador_de_cola_banco()
colaBanco1 = Cola()
colaBanco1.put(("rodri",123,True,False))
colaBanco1.put(("pablo",123,False,True))
colaBanco1.put(("juan",123,False,False))
colaBanco1.put(("cielo",123,False,False))
colaBanco1.put(("pablo",123,False,True))
colaBanco1.put(("paola",123,True,False))
def _a_clientes(cola:Cola()):
    tamanoColaclientes = cola.qsize()
    colaNueva = Cola()
    colaPrioridad = Cola()
    colaPreferencial = Cola()
    colaOtros = Cola()
    while not cola.empty():
        cliente = cola.get()
        if cliente[3] == True: #Prioridad
            colaPrioridad.put(cliente)
        elif cliente[2] == True: #Cuenta Preferencial
            colaPreferencial.put(cliente)
        else:
            colaOtros.put(cliente)
    
    while colaNueva.qsize()<tamanoColaclientes:
        while not colaPrioridad.empty():
            clientePrioridad = colaPrioridad.get()
            colaNueva.put(clientePrioridad)
        while not colaPreferencial.empty():
            clientePreferen = colaPreferencial.get()
            colaNueva.put(clientePreferen)
        while not colaOtros.empty():
            clienteOtro = colaOtros.get()
            colaNueva.put(clienteOtro)
    
    return f"la cola es{colaNueva} y los elem {list(colaNueva.queue)}"

colaClientes = _a_clientes(colaBanco1)
colaClientes1 = print(colaClientes)