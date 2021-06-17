# -*- coding: utf-8 -*-
"""
animal.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""
import random


class Animal(object):
    """docstring for Animal"""
    
    def __init__(self):
        super(Animal, self).__init__()
        self.reproducciones_pendientes = 4
        self.edad = 0
        self.sexo = None # Posible mejora para que no se puedan reproducir dos del mismo sexo
        self.energia = self.energia_maxima
        self.es_reproductore = False

    def pasar_un_ciclo(self):
        self.energia -= 1 # Se puede restar si no llega a comer
        self.edad += 1
        if self.reproducciones_pendientes > 0 and self.edad > 1: # Debe tener dos años 
            self.es_reproductore = True

    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.energia > 0

    def tiene_hambre(self):
        return self.energia < self.energia_maxima 

    def es_leon(self):
        return False

    def es_antilope(self):
        return False

    def puede_reproducir(self):
        return self.es_reproductore

    def tener_cria(self):
        # Si tiene una cría ya no puede ser reproductor hasta el siguiente cíclo
        self.es_reproductore = False
        self.reproducciones_pendientes -= 1

    def reproducirse(self, vecinos, lugares_libres):
        ''' 
        Para mi en este punto se debería verificiar:
        
        '''
        pos = None
        # Me fijo si el animal puede reproducirse
        if self.es_reproductore:
            if lugares_libres:
                # Uso un while en lugar de un if ya que tengo que verificar que
                #  el animal vecino pueda reproducirse, si no puede lo elimino 
                #  de la lista y continuo en el ciclo probando con los otros
                # Si encuentro un animal que pueda reproducirse pos toma un 
                #  valor y salgo del ciclo con el 'break'
                while(vecinos):
                    animal = random.choice(vecinos)
                    if animal.es_reproductore:
                        animal.tener_cria()
                        self.tener_cria()
                        pos = random.choice(lugares_libres)
                        break
                    else:
                        vecinos.remove(animal)
        return pos

    def alimentarse(self, animales_vecinos = None):
        self.energia = self.energia_maxima
        return None

    def moverse(self, lugares_libres):
        pos = None
        if lugares_libres:
            pos = random.choice(lugares_libres)

        return pos

    def fila_str(self):
        return f"{self.edad:>3d}    {self.energia:>3d}/{self.energia_maxima:<3d}       {self.es_reproductore!s:<5}"

    def __format__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


class Leon(Animal):
    """docstring for Leon"""
    
    def __init__(self):
        self.energia_maxima = 6
        self.edad_maxima = 10
        super(Leon, self).__init__()

    def es_leon(self):
        return True

    def alimentarse(self, animales_vecinos):
        # Se alimenta si puede e indica la posición del animal que se pudo comer
        pos = None
        if self.tiene_hambre(): # no está lleno
            presas_cercanas = [ (pos,animal) for (pos, animal) in animales_vecinos if animal.es_antilope() ]
            if presas_cercanas: # y hay presas cerca
                super(Leon, self).alimentarse()
                (pos, animal) = random.choice(presas_cercanas)

        return pos

    def __repr__(self):
        # return "León"
        return "L{}".format(self.edad)


class Antilope(Animal):
    """docstring for Antilope"""
    
    def __init__(self):
        self.energia_maxima = 10
        self.edad_maxima = 6
        super(Antilope, self).__init__()
        self.reproducciones_pendientes = 3

    def es_antilope(self):
        return True

    def __repr__(self):
        # return "A"
        return "A{}".format(self.edad)
        