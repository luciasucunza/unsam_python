# fibonacci_envuelto.py

def fibonacci(n):
    '''
    Precondición: n debe ser un número entero positivo
        Devuelve: el n-ésimo número de Fibonacci, donde F(0)=0 y F(1)=1
    '''
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva utilizando 
        un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            Fn2, dict_fibo = fibonacci_aux(n-2, dict_fibo) # Obtiene F(n-2)
            Fn1, dict_fibo = fibonacci_aux(n-1, dict_fibo) # Obtiene F(n-1)
            F = Fn1 + Fn2                                  # Calcula F(n)
            dict_fibo[n] = F                               # Lo agrego al dict
            
        return F, dict_fibo
    
    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F   


#%%
n = 13

print('Primeros', n, 'números de la serie de Fibonacci:')
for i in range(n):
    print(fibonacci(i), end='  ')
print('...')