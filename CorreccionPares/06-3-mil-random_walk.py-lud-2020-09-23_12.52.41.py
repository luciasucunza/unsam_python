# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:12:15 2020

@author: User
"""
#%% ejercicio 6.10

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
mat=[randomwalk(N) for i in range(0,12)] #mat tiene 12 listas randomwalk

#busco la que mas se aleja del cero y la que menos se aleja
maximos=[max(mat[i],key=abs) for i in range(0,12)] #da el punto mas lejano de cada caminata
mas_lejos=maximos.index(max(maximos,key=abs)) # busco la que mas se aleja como el maximo de los maximos
menos_lejos=maximos.index(min(maximos,key=abs)) # busco la q menos se aleja como el minimo de los maximos


fig = plt.figure(figsize=(8,6),dpi=80)
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot(mat[0], c="b")#
plt.plot(mat[1], c="r")
plt.plot(mat[2], c="g")
plt.plot(mat[3], c="c")#cian
plt.plot(mat[4], c="m")#magenta
plt.plot(mat[5], c="y")
plt.plot(mat[6], c="k")#negro
plt.plot(mat[7], c="orange")
plt.plot(mat[8], c="grey")
plt.plot(mat[9], c="brown")
plt.plot(mat[10], c="pink")
plt.plot(mat[11], c="violet")
#plt.xlabel('tiempo'), plt.ylabel('distancia al origen')
plt.title('12 caminatas al azar')
plt.ylim(-1000,1000)
plt.yticks([-500,0,500])
plt.xticks([]) # saca las marcas en el eje x

plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot(mat[mas_lejos]) #grafico el que mas se aleja
plt.title('La caminata que mas se aleja')
plt.ylim(-1000,1000)
plt.yticks([-500,0,500])
plt.xticks([])

plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot(mat[menos_lejos])
plt.title('La caminata que menos se aleja')
plt.ylim(-1000,1000)
plt.yticks([-500,0,500])
plt.xticks([]) 

plt.show()