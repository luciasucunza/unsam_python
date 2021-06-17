# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:04:29 2020

@author: Josefina
"""

# hojas_ISO.py
# Ejercicio 10.13: Hojas ISO y recursión


def calculo_hojaISO(N):
    ''' Para una entrada N, devuelva el ancho y el largo de la hoja A(N) en mm.
    Pre: N >0 y entero.
    Post: (ancho, largo) de A(N)'''
    #Definición Caso Base
    if N == 0:
        ancho = 841
        largo = 1189
        return ancho, largo
    #Caso Recursivo (converge a N==0)
    ancho = calculo_hojaISO(N-1)[1]//2
    largo = calculo_hojaISO(N-1)[0]
    
    return ancho, largo
    
    
#%%
N = 1    #(594, 841)
N = 2    #(420, 594)
N = 3    #(297, 420)
N = 4    #(210, 297)
calculo_hojaISO(N) 
