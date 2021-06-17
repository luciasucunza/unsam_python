# burbujeo.py

# Ejercicio 11.2

#%% Ejemplo 11.2 Burbujeo   
def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbuja.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        
        #burbujear la lista hasta la posición n
        burbujear(lista, 0, n)
        print('DEBUG: ', lista)
        
        n = n-1

        
def burbujear(lista, a, b):
    '''Burbujea un segmento de la lista de elementos.
       Pre: la lista no debe estar vacia
            los elementos del segmento deben ser comparables 
            b y a deben corresponder a posiciones en la lista.
       Post: la lista con el mayor valor del segmento en la posición fin.'''
       
    for i in range(a, b):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]

#%% Probar con:
lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]

for l in [lista_1, lista_2, lista_3, lista_4, lista_5]:
    print('La lista:', l, end=' ')
    ord_burbujeo(l)
    print('queda ordenada así:', l)
    
    
'''La cantidad de comparaciones siempre es la misma, independientemente de como
esté ordenada a lista, primero son N-1 compraciones, en el siguiente paso N-2, 
luego N-3, etc. Es decir que son N^2 comparaciones
El peor caso posbile es una lista ordenada de mayor a menor, por ejemplo 
    [9, 8, 7, 6, 5, 4 ], 
en este caso se necesitan 15 intercambios para alcanzar el orden: 5+4+3+2+1,
la cantidad de intercambios será en el peor caso cont*N^2 y en el mejor de los 
casos 0.'''

