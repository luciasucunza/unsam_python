#figuritas.py

import random
import numpy as np
import matplotlib.pyplot as plt


#%% 
'''
En este bloque de codigo se encuentran todas las funciones pedidas
'''

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(A):
    return 0 in A

def comprar_figu(figus_total):
    return random.randint(0, figus_total-1)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        album[comprar_figu(figus_total)] +=1
        compras += 1        
    return compras

def comprar_paquete(figus_total, figus_paquete):
    return np.array([comprar_figu(figus_total) for i in range(figus_paquete)])

def cuantos_paquetes(figus_total, figus_paquete): 
    album = crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        for figu in comprar_paquete(figus_total, figus_paquete):
            album[figu] +=1
            compras += 1        
    return compras

#Función comprar_paquete sin repeticiones
def comprar_paquete_sin_repes(figus_total, figus_paquete):
    return random.sample(list(range(figus_total)), k=5)

def cuantos_paquetes_sin_repes(figus_total, figus_paquete): 
    album = crear_album(figus_total)
    compras = 0
    while album_incompleto(album):
        for figu in comprar_paquete_sin_repes(figus_total, figus_paquete):
            album[figu] +=1
            compras += 1        
    return compras

def albumes_incompletos_cooperativos(A, amigues):
    return min(A) < amigues

def cuantos_paquetes_cooperativos(figus_total, figus_paquete, amigues): 
    album = crear_album(figus_total)
    compras = 0
    while albumes_incompletos_cooperativos(album, amigues):
        for figu in comprar_paquete(figus_total, figus_paquete):
            album[figu] +=1
            compras += 1        
    return compras

#%% 4.19
n_repeticiones = 1000
figus_total = 6
l = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
promedio = np.mean(np.array(l))

print(f'En base a {n_repeticiones} repeticiones se estima que para completar un album de {figus_total} figuritas se necesitan comprar {promedio} figuritas')
plt.hist(l, 50 )

#%% 4.20
n_repeticiones = 100
figus_total = 670
l = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
promedio = np.mean(np.array(l))

print(f'En base a {n_repeticiones} repeticiones se estima que para completar un album de {figus_total} figuritas se necesitan comprar {promedio} figuritas')
plt.hist(l, 30 )

#%% 4.24
n_repeticiones = 100
figus_total = 670
figus_paquete = 5
l = [cuantos_paquetes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(np.array(l))

print(f'En base a {n_repeticiones} repeticiones se estima que para completar un album de {figus_total} figuritas se necesitan comprar {promedio} paquetes de {figus_paquete} cada uno')
plt.hist(l, 50 )

#%% 4.25
l_850 = [cant for cant in l if cant <= 850]
prob = len(l_850)/n_repeticiones

print(f'En base a {n_repeticiones} repeticiones se estima que la probabilidad de completar el album de {figus_total} figuritas comprando 850 paquetes de {figus_paquete} cada uno es {prob}')


#%% 
'''
4.26: En cada apartado grafico el histograma
4.27: FALTA    
'''

#%% 4.28
n_repeticiones = 100
figus_total = 670
figus_paquete = 5
l = [cuantos_paquetes_sin_repes(figus_total, figus_paquete) for i in range(n_repeticiones)]
promedio = np.mean(np.array(l))
print(f'En base a {n_repeticiones} repeticiones se estima que para completar un album de {figus_total} figuritas se necesitan comprar {promedio} paquetes de {figus_paquete} cada uno')

l_850 = [cant for cant in l if cant <= 850]
prob = len(l_850)/n_repeticiones
print(f'En base a {n_repeticiones} repeticiones se estima que la probabilidad de completar el album de {figus_total} figuritas comprando 850 paquetes de {figus_paquete} cada uno es {prob}')


#%% 4.29
amigues = 5
n_repeticiones = 100
figus_total = 670
figus_paquete = 5
l = [cuantos_paquetes_cooperativos(figus_total, figus_paquete, amigues) for i in range(n_repeticiones)]
promedio = np.mean(np.array(l))

print(f'En base a {n_repeticiones} repeticiones se estima que para que los {amigues} amigues complenten cooperativamente sus albumes de {figus_total} figuritas se necesitan comprar {promedio} paquetes de {figus_paquete} figuritas cada uno')
print(f'Es decir que, en promedio, necesitan {promedio/amigues} paquetes para completar un ablum ')


