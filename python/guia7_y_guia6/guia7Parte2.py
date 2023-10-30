#ejercicio4
#vocales=list("aeiou")
# def reemplazaVocales(palabra):
# #    a = ""
#     for i in range(len(palabra)):
#         if palabra[i] == 'a' or palabra[i] == 'e' or palabra[i] == 'i' or palabra[i] == 'o' or palabra[i] == 'u':
#             palabra[i]= '_'
#     return palabra         

# palabra = list("hola Como estas")
# reemplazaVocales(palabra)
# print(palabra)

vocales = "aeiou"
def reemplazaVocales(palabra):
    palabraOut = ""
    for i in palabra:
        if i in vocales:
            palabraOut = palabraOut + '_'

        else:
            palabraOut = palabraOut + i

    return palabraOut


def esPalindromo (words):
    a = words[::-1]
    if a == words:
        return True
    else:
        return False
print(esPalindromo("opo"))

def daVueltaStr (palabra:str):
    reverseWord = ""
    for i in palabra:
        reverseWord =  i + reverseWord 
    return reverseWord

print(daVueltaStr("hola"))

def eliminarRepetidos (palabra):
    strsinrep = ""
    for i in palabra:
        if i in palabra:
            for j in palabra:
                if i == j:
                     strsinrep = strsinrep + '_'
        else:
            strsinrep = strsinrep + i
        
    return strsinrep
eliminarRepetidos(("holaaaa"))