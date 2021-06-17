# random_walk.py

import numpy as np
import matplotlib.pyplot as plt

#%%
def cm2inch(value):
    ''' Calcula el valor en centimetros de la magnitud en pulgadas recibida
    
        Pre: Value debe ser un número real
        Pos: Devuelve un número real, con el valor de argumento en pulgadas pasado a centimetros 
    '''
    
    return value/2.54

def randomwalk(largo):
    ''' Calcula la trayectoria en cierta cantidad de pasos (n) de -1, 0 o 1
    
        Pre: Recibe un número entero con la cantidad de pasos.
        Pos: Devulve una lista de longitud n, con la posición alcanzada en cada paso
    '''
    pasos = np.random.randint(-1, 2, largo)    
    return pasos.cumsum()

#%%
N = 100000
# Cada una de las doce caminatas se guardará en una fila del siguiente array
caminatas = np.empty([12, N])

caminatas[0] = randomwalk(N)

# Analizada solo La primera caminata sería la que más y la que menos alcanza
i_lejos_max = 0
i_lejos_min = 0


for i in range(1, 12):
    # Nueva caminata y la distancia máxima alcanzada en la misma
    caminatas[i] = randomwalk(N)
    alejado = abs(caminatas[i]).max()
    
    # Se analiza si el valor máximo alcanzado en esta caminata es mayor que el
    #  valor alcanzado en las caminatas anteriores, si es se guarda el número 
    #  de indice de dicha caminata
    if alejado > abs(caminatas[i_lejos_max]).max():
        i_lejos_max = i
    # Mismo procedimiento para menor distancia alcanzada
    elif alejado < abs(caminatas[i_lejos_min]).max():
        i_lejos_min = i
            
    
#%%
# Comienzo con los gráficos, inciando una figura de un tamaño adecuado
fig = plt.figure(figsize=(cm2inch(18), cm2inch(14)))

# Superior: los 12 caminos, cada uno con un color disinto
# Se ponene nombre a los ejes y limites más ticks al eje de ordenadas 
plt.subplot(2, 1, 1)            
for i in range(12):
    plt.plot(caminatas[i] ) 
plt.title('12 Caminatas al azar')
plt.xlabel('tiempo'), plt.ylabel('Distancia al origen')
plt.ylim(-1000, 1000)
plt.xticks([]), plt.yticks([-500,0,500])  # saca las marcas

# Inferior izquierdo: la caminata del que alcanza a ir más lejos
# Se ponene nombre a los ejes y limites más ticks al eje de ordenadas
plt.subplot(2, 2, 3)            # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.title('La caminata que más se aleja')
plt.plot(caminatas[i_lejos_max])
plt.xlabel('tiempo'), plt.ylabel('Distancia al origen')
plt.ylim(-1000, 1000)
plt.xticks([]), plt.yticks([-500,0,500])

# Inferior derecho: la caminata del que alcanza a ir menos lejos
# Se ponene nombre a los ejes y limites al eje de ordenadas (los ticks no para no ensuciar)
plt.subplot(2, 2, 4)            # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.title('La caminata que menos se aleja')
plt.plot(caminatas[i_lejos_min])
plt.xlabel('tiempo'), plt.ylabel('Distancia al origen')
plt.ylim(-1000, 1000)
plt.xticks([]), plt.yticks([])

plt.show()