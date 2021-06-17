#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:32:15 2020

@author: JMorganella
"""


class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
    def __len__(self):
        '''
            Devuelve la cantidad de elementos de la Cola
        '''
        return len(self.items)
    
    
    
    
class TorreDeControl():
    
    def __init__(self):
        self.arribo = Cola()
        self.partida = Cola()
    
    def nuevo_arribo(self, vuelo):
        self.arribo.encolar(vuelo)

    def nueva_partida(self, vuelo):
        self.partida.encolar(vuelo)
    
    def ver_estado(self):  
        row = 'Vuelos esperando para aterrizar: '
        row += ', '.join(self.arribo.items)
        row += '\n'
        row += 'Vuelos esperando para despegar: '
        row += ', '.join(self.partida.items)
        print(row)
        
    def asignar_pista(self):
        if (len(self.arribo) != 0):
            print (f'El vuelo {self.arribo.desencolar()} aterrizó con éxito.')
        elif (len(self.partida) != 0):
            print (f'El vuelo {self.partida.desencolar()} despegó con éxito.')
        else:
            print( 'No hay vuelos en espera.')
            
    
    
def main():
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()
    #Vuelos esperando para aterrizar: AR156, AR32
    #Vuelos esperando para despegar: KLM1267
    torre.asignar_pista()
#El vuelo AR156 aterrizó con éxito.
    torre.asignar_pista()
#El vuelo AR32 aterrizó con éxito.
    torre.asignar_pista()
#El vuelo KLM1267 despegó con éxito.
    torre.asignar_pista()
#No hay vuelos en espera.
