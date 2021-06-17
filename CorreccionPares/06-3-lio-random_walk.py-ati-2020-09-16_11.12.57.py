#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:45:03 2020

@author: atilio
"""

import numpy as np
import matplotlib.pyplot as plt

#%%Algunas funciones
def cm2inch(value):
    return value/2.54

def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()

#%%Corrida
N = 100000
Ncorridas = 12
x = 10000
Dist_en_x = []


#Corro Ncorridas veces
corridas = [randomwalk(N) for _ in range(Ncorridas)]

for corrida in corridas:
    Dist_en_x.append(abs(corrida[x]))

#%%Gráfica
fig = plt.figure()

plt.subplot(2, 1, 1)
for corrida in corridas:
    plt.plot(corrida)
plt.title('12 corridas aleatorias')
plt.xlabel('Tiempo')
plt.ylabel('Distancia')

plt.subplot(2, 2, 3)
plt.plot(corridas[Dist_en_x.index(max(Dist_en_x))], alpha = 0.65)
plt.scatter(x,corridas[Dist_en_x.index(max(Dist_en_x))][x] , color='red')
plt.annotate(f'({x},{corridas[Dist_en_x.index(max(Dist_en_x))][x]})',
             xy=(x,corridas[Dist_en_x.index(max(Dist_en_x))][x]), xycoords='data',
             xytext=(30, -20), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.title(f'Corrida que más se aleja en ({x},{corridas[Dist_en_x.index(max(Dist_en_x))][x]})')
plt.xlabel('Tiempo')
plt.ylabel('Distancia')

plt.subplot(2, 2, 4)
plt.plot(corridas[Dist_en_x.index(min(Dist_en_x))], alpha = 0.65)
plt.scatter(x,corridas[Dist_en_x.index(min(Dist_en_x))][x] , color='red')
plt.annotate(f'({x},{corridas[Dist_en_x.index(min(Dist_en_x))][x]})',
             xy=(x,corridas[Dist_en_x.index(min(Dist_en_x))][x]), xycoords='data',
             xytext=(30, -20), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.title(f'Corrida que menos se aleja en ({x},{corridas[Dist_en_x.index(min(Dist_en_x))][x]})')
plt.xlabel('Tiempo')
plt.ylabel('Distancia')

plt.show()
