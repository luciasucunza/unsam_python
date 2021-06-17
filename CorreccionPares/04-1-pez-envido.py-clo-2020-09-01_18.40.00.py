# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 18:08:11 2020

@author: cecil
"""
# Ejercicios sección 4.2 Random
# Elecciones con y sin reposición

# Autor: Ing. Cecilia López Weibel (FICH-UNL)

#%%
# Ejercicio 4.8: Envido
# Teniendo en cuenta las reglas del Truco, estimá la probabilidad de obtener 
# 31, 32 o 33 puntos de envido en una mano.
# ¿Son iguales estas tres probabilidades? ¿Por qué?
# Observación: como corresponde, en esta materia jugamos al truco sin flor.

import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']

naipes = [(valor,palo) for valor in valores for palo in palos]

def jugar ():
    
    def cartas_mano ():
        cartas = random.sample(naipes,k=3)
        return cartas
    
    def puntaje(valor):
        if valor in range(1,8):
            return valor
        else:
            return 0
        
    puntaje_por_palo = {}

    for palo in palos:
        puntaje_por_palo[palo] = []

    mano = cartas_mano()
     
    for valor, palo in mano:
        puntaje_por_palo[palo].append(puntaje(valor))    # agrego lista de puntaje por palo en diccionario

    max_cant_cartas=1
    for palo in puntaje_por_palo:
        if len(puntaje_por_palo[palo]) > max_cant_cartas:
            max_cant_cartas = len(puntaje_por_palo[palo])
            palo_mas_cartas = palo
    
    if max_cant_cartas == 2:
        suma_puntos = 20 + sum (puntaje_por_palo[palo_mas_cartas])
    elif max_cant_cartas == 3:
        suma_puntos = 20 + sum(puntaje_por_palo[palo_mas_cartas]) - min((puntaje_por_palo[palo_mas_cartas]))
    else:
        suma_puntos = 0 #Si sólo tengo una carta, el envido no va a llegar a 31 (no me interesan estos puntos)
    
    return suma_puntos 

# Cálculo de las probabilidades:

N = 1000000                        #Cantidad de jugadas

envido_31 = 0
envido_32 = 0
envido_33 = 0

for i in range(N):
    jugada = jugar()
    if jugada == 31:
        envido_31 += 1
    elif jugada == 32:
        envido_32 += 1
    elif jugada == 33:
        envido_33 += 1

prob_envido31 = envido_31/N
print(f'Barajé {N} veces, de las cuales {envido_31} saqué envido 31.')
print(f'Podemos estimar la probabilidad de sacar envido 31 mediante {prob_envido31:.3f}.')

prob_envido32 = envido_32/N
print(f'Barajé {N} veces, de las cuales {envido_32} saqué envido 32.')
print(f'Podemos estimar la probabilidad de sacar envido 31 mediante {prob_envido32:.3f}.')

prob_envido33 = envido_33/N
print(f'Barajé {N} veces, de las cuales {envido_33} saqué envido 33.')
print(f'Podemos estimar la probabilidad de sacar envido 33 mediante {prob_envido33:.3f}.')

prob = (envido_33+envido_31+envido_32)/N
print(f'Barajé {N} veces, de las cuales {envido_33} saqué envido 33.')
print(f'Podemos estimar la probabilidad de sacar envido 33 mediante {prob:.3f}.')

#%%
# Salidas:
# Barajé 1000000 veces, de las cuales 29387 saqué envido 31.
# Podemos estimar la probabilidad de sacar envido 31 mediante 0.029387.
# Barajé 1000000 veces, de las cuales 15043 saqué envido 32.
# Podemos estimar la probabilidad de sacar envido 31 mediante 0.015043.
# Barajé 1000000 veces, de las cuales 15554 saqué envido 33.
# Podemos estimar la probabilidad de sacar envido 33 mediante 0.015554.

# Barajé 100000000 veces, de las cuales 2958517 saqué envido 31.
# Podemos estimar la probabilidad de sacar envido 31 mediante 0.029585.
# Barajé 100000000 veces, de las cuales 1494057 saqué envido 32.
# Podemos estimar la probabilidad de sacar envido 31 mediante 0.014941.
# Barajé 100000000 veces, de las cuales 1538245 saqué envido 33.
# Podemos estimar la probabilidad de sacar envido 33 mediante 0.015382.

#%%
# ¿Son iguales estas tres probabilidades? ¿Por qué?
# Las tres probabilidades no son iguales. Pensando en las combinaciones de
# cartas necesarias para obtener las diferentes sumas, observamos que:
# Envido 31: combinación de 4+7 y 5+6
# Envido 32: combinación de 5+7
# Envido 33: combinación de 6+7 
# Para el caso de envido 33, la probabilidad es un poco mayor que para envido
# 32 porque puede darse el caso de tener 5+6+7 del mismo palo, y en ese caso
# conviene quedarse con 6+7 (entonces hay menos combinaciones para envido 32)