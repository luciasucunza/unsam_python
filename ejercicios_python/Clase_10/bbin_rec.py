# bbin_rec.py

def bbinaria_rec(lista, e):
    '''
    Precondición: la lista debe estar ordenada de mayor a menor
        Devuelve: True si el elemento está en la lista, False si no está.
    '''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        elif e < lista[medio]:
            res = bbinaria_rec(lista[:medio], e)
        else:
            res = bbinaria_rec(lista[-medio:], e)
            
    return res


#%%
l = [1,2,3,4,5,6,7]
print('En la lista:', l)
print('¿Está el 8?', bbinaria_rec(l, 8) )#False
print('¿Está el 0?', bbinaria_rec(l, 0) )#False
print('¿Está el 1?', bbinaria_rec(l, 1) )#True
print('¿Está el 7?', bbinaria_rec(l, 7) )#True
print('¿Está el 4?', bbinaria_rec(l, 4) )#True
