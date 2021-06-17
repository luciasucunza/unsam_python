#estimar_pi.py

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def punto_dentro():
    x, y = generar_punto()
    if (x**2+y**2) <= 1:
        return True
    return False

N = 100000
M = sum([punto_dentro() for i in range(N)])
prob = 4*M/N
print(f'Generamos {N} puntos, de las cuales {M} cayeron dentro del circulo de radio unitario.')
print(f'Podemos estimar pi mediante {prob:.6f}.')