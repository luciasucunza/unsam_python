# 11_Ejercicios.py

#%% Ejemplo 11.1 Describir pasos para ordenar 09385324
'''
09385324
03853249
03532489
03324589
03234589
02334589
02334589
02334589
-----------
09385324
09385324
03985324
03895324
03589324
03358924
02335894
02334589
'''


#%% Ejemplo 11.2 Burbujeo   
def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbuja.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        
        #burbujear la lista hasta la posición n
        burbujear(lista, 0, n)
        print("DEBUG: ", lista)
        
        n = n-1

        
def burbujear(lista, inicio, fin):
    """Burbujea un segmento de la lista de elementos.
       Pre: la lista no debe estar vacia, los elementos del segmento deben ser 
       comparables e inicio y fin deben corresponder a posiciones en la lista.
       Post: la lista con el mayor valor del segmento en la posición fin."""
       
    for i in range(inicio, fin):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]

lista = [3, 2, -1, 5, 0, 2]
ord_burbujeo(lista)
        
        
