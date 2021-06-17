# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:35:40 2020

@author: Nacho
"""


# Ejercicio 3.9 propaga.py
# 0 = nuevo ; 1 = encendido ; -1 = carbonizado 
def propagar(fosforos):
    estado = [None] * len(fosforos)
    estadof = [None] * len (fosforos)

    a = fosforos[0]
    for i, n in enumerate(reversed(fosforos), start = 0):
        if a == 1 and n == 0:
            estado[i] = 1
        elif a == 1 and n == -1:
            a = -1
            estado[i] = n
        elif a != 1 and n == 1:
            a = 1
            estado[i] = n
        else:
            estado[i] = n
    
    for i, n in enumerate(reversed(estado), start = 0):
        if a == 1 and n == 0:
            estadof[i] = 1
        elif a == 1 and n == -1:
            a = -1
            estadof[i] = n
        elif a != 1 and n == 1:
            a = 1
            estadof[i] = n
        else:
            estadof[i] = n
            
    return estadof

propagar([1,0,-1,0])

propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
#[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
propagar([ 0, 0, 0, 1, 0, 0])
#[ 1, 1, 1, 1, 1, 1]
