# canguros_buenos.py


        
#%%
''' 
Clase definida por mi originalmente

NOTA: Codigo comentado para que no haya doble definicion de la clase
'''

# class Canguro ():
#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.contenido_marsupio = []
        
#     def __str__(self):
#         lista = [self.nombre + ' tiene en su marsupio:']
#         lista = lista + [ c.nombre for c in self.contenido_marsupio]
#         return '\n'.join(lista)
    
#     def meter_en_marsupio (self, objeto):
#         self.contenido_marsupio.append(objeto)
        
#%%
'''
Corrección de la clase definida en el ejemplo.
Junto con un comentario indicando dónde está el error y en qué conste:
    
El error estaba en la linea:
    >>>    self.contenido_marsupio = contenido
    
En la función 'meter_en_marsupio' lo que se hace es una append de la lista 
'contenido_marsupio', pero esta no es más que un puntero a la lista 'contenido'
como en ningun caso se pasa al constructor una lista para el contenido, todos
quedan apuntando al mismo lugar. Al hacer el append se refleja en todas las 
instancias.

Si por ejempo se hubiese instanciado de la siguiente manera este problema no 
habría salido a al luz:
    
    >>>    madre_canguro = Canguro('Madre', [])
    >>>    cangurito = Canguro('gurito', [])


En mi primera definición de la clase tome que incialmente el contenido siempre 
es nulo con lo cual no tuve este problema
'''

from copy import copy
        
class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = copy(contenido)

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
''' Bloque de testeo

Si se corre todo el bloque imprime:
    Madre tiene en su marsupio:
        'billetera'
        'llaves del auto'
        <__main__.Canguro object at 0x000002130D24D748>
    gurito tiene en su marsupio:
'''    
        
        
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)
print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.
print(cangurito)
