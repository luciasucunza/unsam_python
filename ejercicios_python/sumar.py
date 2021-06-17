# sumar_enteros.py
'''
En realidad no se pedía guardar este archivo pero por las dudas

La función de resta de triangulos esta copada
'''

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    # El invariante es que suma contiene el valor de la sumatoria a partir de 'desde' hasta el índice de iteración 
    for i in range(desde, hasta+1, 1):
        suma += i
    return suma

def sumar_enteros2(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    t_desde = (desde-1)*((desde-1)+1) / 2
    t_hasta = hasta*(hasta+1) / 2
    
    return t_hasta - t_desde

def potencia(base, exp):
    'Calcula la potencia exp del número base, con exp entero mayor que 0.'
    resultado = 1
    for i in range(exp):
        print(i)
        resultado *= base
    return resultado