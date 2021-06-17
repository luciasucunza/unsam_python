# larenga.py

def pascal(n, k):
    '''
    Precondición: n y k deben ser enteros positivos, k menor o igual a n para 
                  estar dentro del triangulo.
        Devuelve: El número en el triangulo de pascal alojado en fila n, 
                  columna k.
    '''
    # Caso base, los bordes del triángulo
    if k == 0 or k == n:
        return 1
    
    return pascal(n-1, k-1) + pascal(n-1, k)  

#%%
     
print('Triangulo Pascal primeras 5 filas')
print(' '        ,' '        ,' '        ,' '        ,pascal(0,0),' '        ,' '        ,' '        ,' '        )
print(' '        ,' '        ,' '        ,pascal(1,0),' '        ,pascal(1,1),' '        ,' '        ,' '        )
print(' '        ,' '        ,pascal(2,0),' '        ,pascal(2,1),' '        ,pascal(2,2),' '        , ' '	 )	
print(' '        ,pascal(3,0),' '        ,pascal(3,1),' '        ,pascal(3,2),' '        ,pascal(3,3), ' '       )
print(pascal(4,0),' '        ,pascal(4,1),' '        ,pascal(4,2),' '        ,pascal(4,3),' '        ,pascal(4,4))


print('Ejemplo propuesto:', pascal(5,2))