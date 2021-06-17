# plot_bbin_vs_bsec.py

import random
import matplotlib.pyplot as plt
import numpy as np

#%%
def generar_lista(n,m):
    l = random.sample(range(m),k=n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0,m-1)

def busqueda_binaria(lista, e):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    comps = 0 #inicializo en cero la cantidad de comparaciones
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        comps += 1 #sumo la comparación que estoy por hacer
        if lista[medio] == e:
            pos = medio     # elemento encontrado!
        comps += 1 #sumo la comparación que estoy por hacer
        if lista[medio] > e:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps

def busqueda_secuencial_(lista,e):
    '''Si e está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 #inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 #sumo la comparación que estoy por hacer
        if z == e:
            pos = i
            break
    return pos, comps

def experimento_binario_promedio(lista,m,k):
    comps_tot = 0
    for i in range(k):
        e = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,e)[1]

    comps_prom = comps_tot / k
    return comps_prom

def experimento_secuencial_promedio(lista,m,k):
    comps_tot = 0
    for i in range(k):
        e = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,e)[1]

    comps_prom = comps_tot / k
    return comps_prom

#%%
m = 10000
k = 1000

largos = np.arange(256)+1 #estos son los largos de listas que voy a usar
comps_promedio_bin = np.zeros(256) #aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_promedio_sec = np.zeros(256) #aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n,m)                                          # genero lista de largo n
    comps_promedio_bin[i] = experimento_binario_promedio(lista,m,k)     
    comps_promedio_sec[i] = experimento_secuencial_promedio(lista,m,k)

#ahora grafico largos de listas contra operaciones promedio de búsqueda, ambas en el mismo gráfico
plt.plot(largos,comps_promedio_bin,label='Búsqueda Binaria')
plt.plot(largos,comps_promedio_sec,label='Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()