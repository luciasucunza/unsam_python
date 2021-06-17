# documentacion.py

def valor_absoluto(n):
    '''
    Calcula el valor absoluto del número real
    
    Pre: Recibe dos números reales.
    Pos: Devuelve un número real, con el valor absoluto del argumento.
    '''
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    '''
    Calcula la sumatoria de los numeros pares de la lista.
    Si la lista esta vacia devuleve 0.
    
    Pre: La lista debe estar formada por números
    Pos: Devuelve un número, con la sumatoria de los números pares. Si la lista esta vacia devuleve 0.
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res


def veces(a, b):
    '''
    Calcula el producto entre ambos números.
    
    Pre: Recibe dos números enteros. (a podría llegar a ser un número real, pero b no)
    Pos: Devuelve un número, con el producto entre ambos valores.
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    '''
    Traté de entender el objetivo de esta función pero no pude.
    Agruegé algunos prints pero tampoco lo logré
    
    Pre: Recibe un número entero mayor que 0.   
    Pos: Devuelve un número, con la cantidad de veces que entró al wihle más uno.
    '''
    res = 1

    while n!=1:
        # print('Valor de n:',n)
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
        # print('Valor de res:',res)
    return res