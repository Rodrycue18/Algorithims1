#ejemplos con diccionario
 
#creo un dicc con algunos pares de clave-valor
mi_dicc: dict[str, str] = {
    'auto': 'car',
    'sol': 'sun',
    'luna': 'moon'
}
 
#agrego clave-valor
mi_dicc['clave'] = "valor"
 
#reemplazo el valor de una clave
mi_dicc['clave'] = "nuevo valor"
 
#recupero un valor
v:str = mi_dicc['clave']
 
 
#recorro un dicc, lo imprimo y lo copio a otro diccionario
nuevo_dic: dict[str, str] = {} #creo un dicc vacio
claves:list[str] = mi_dicc.keys() 
 
for clave in claves:    
    valor:str = mi_dicc[clave]
    print(clave + ' - ' + valor)  
    #modo python es: print(f'{clave} - {valor}') 
    nuevo_dic[clave] = valor #lo agrego al nuevo diccionario
 
#otra forma de recorrer un dicc
for clave, valor in mi_dicc.items():    
    print(clave + ' - ' + valor)   
    #modo python es: print(f'{clave} - {valor}') 
    nuevo_dic[clave] = valor #lo agrego al nuevo diccionario