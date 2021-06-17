#-----------------------------------------
# Autor: Vanina Lanabere -----------------
# propaga.py-----------------------
#-----------------------------------------

#import busqueda_en_listas as busco ------
# Uso dos funciones que utilicé en -------
# busqueda_en_listas ---------------------

#-----------------------------------------
# Ejercicio 3.6 --------------------------
# Esta funcion recibe una lista y un -----
# elemento y devuelve la posición de la --
# última aparición del elemento (e) en la-
# lista ----------------------------------
#-----------------------------------------
def buscar_u_elemento(lista, e):
    pos = -1
    for i, z in enumerate(lista):
        if z == e:
            pos = i
    return pos
'''
lista = [1, 4, 54, 3, 0, -1]
e= 44
print('El elemento', e, 'aparece en la lista', lista, 'en la posicion', buscar_u_elemento(lista, e))
'''
#-----------------------------------------
# Esta funcion recibe una lista y un -----
# elemento y devuelve la cantidad de veces
# que aparece el elemento (e) en la lista-
#-----------------------------------------
def buscar_n_elemento(lista, e):
    n_veces = 0
    for z in lista:
        if z==e:
            n_veces += 1
    return n_veces
'''
lista = [1,2,3,2,3,4]
e = 2
print('El elemento',e, 'aparece en', lista, buscar_n_elemento(lista,e), 'veces')
'''

#-----------------------------------------
# Ejercicio 3.9 --------------------------
# Esta funcion recibe una lista y devuelve
# otra lista en el que los 1's se propagan
# a sus vecinos 0'------------------------
#   0: fosforo nuevo
#   1: fosforo encendido
#  -1: fosforo carbonizado
#-----------------------------------------
def propagar(lista):
    lista_nueva = lista.copy()
    n_encendidos = buscar_n_elemento(lista,1)
    print('Hay',n_encendidos, 'fosforos encendidos')
    for i in range(n_encendidos):
        encendido = buscar_u_elemento(lista,1)
        print('Fosforo encendido ubicado en', encendido)
        try:
            i = encendido
            while lista[i + 1]==0:
                lista_nueva[i+1]=1
                i +=1
        except IndexError:
            print('Llegue al final de la lista')
        i = encendido
        while lista[i-1]==0:
            lista_nueva[i-1]=1
            i -=1
        lista[encendido] = -1
    return lista_nueva


inicial = [0,1,0,-1,0,0]
print(propagar(inicial))

# inicial = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
# print('inicial:', inicial)
# print('final de la propagacion: ', propagar(inicial))
# print('-'*30)
# inicial = [ 0, 0, 0, 1, 0, 0]
# print('inicial:', inicial)
# print('final de la propagacion: ', propagar(inicial))

#%% 
'''
Creo que sería más correcto utilizar un if para reguntar si estás en el final de la lista, más que utilizar "try/except"
Probando el caso [0,1,0,-1,0,0] devuelve [1,1,1,-1,1,1], y debería volver [1,1,1,-1,0,0]. Por lo que vi con el debuger el problema es el segundo while, el i toma valores negativos, entonces cuando quema para atrás no frena en la primera posición, sigue analizando la lista desde la última posición y recorre para atrás.
'''
