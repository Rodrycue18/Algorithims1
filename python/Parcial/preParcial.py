def caballos (caballos,dicc) -> dict:
    dict = {}
    for caballo in caballos: # Creamos dicc con 
        listaPosiciones = [0] * len(caballos) #[0,0,0]
        dict[caballo] = listaPosiciones

    for caballo,valor in dict.items():
        for carreras in dicc.values(): #recorremos las listas
            i = 0
            for lista in carreras: # recorremos la lista
                if lista == caballo:
                    valor[i] = valor[i]+1
                i = i + 1
    
    return dict
#print(caballos(["a","b","c","d"],{"1":["b","a","c","d"],"2":["a","c","b","d"]}))
# a:[1,1,0],b:[1,0,1],c:[0,1,1]

def intercalado(lista1, lista2)->list:
    nuevaLista = []
    for i in range(len(lista1)):
        nuevaLista.append(lista1[i])
        for j in range(len(lista2)):
            if i == j:
                nuevaLista.append(lista2[j])
    return nuevaLista
#[1,2,3] , [4,5,6] -> [1,4,2,5,3,6]
#print(intercalado([1,2,3],[4,5,6]))
def ej3(lista,n,elem):

    for i in range(len(lista)):
        if lista[i]==elem:
            n = n - 1
        if n == 0:
            return i
    return -1
print(ej3([-1,1,1,5,3,1,2,8],3,1))
# lista = [-1,1,1,5,3,1,2,8]
# n = 2
# elem = 1

# debería devolver res = 2
# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#  ]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(f"{i},{j} = {a[i][j]}")

# print(a[1][2])
# b = [1,1,2,1,1]
# nueva = []
# for i in range((len(b)-1),-1,-1):
#     nueva.append(b[i])
#     print(nueva)
# print(b==nueva)