# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:30:21 2020

@author: sucun
"""

class Lote:
    def __init__(self, f, c, p):
        self.nombre = f
        self.cajones = c
        self.precio = p
        
    def __repr__(self):
        return f'Lote()'
    def __str__(self):
        return f'Lote:'
    def vender(self,n):
        return n
    
class Lote_inf(Lote):
    def vender(self):
        return 1.24