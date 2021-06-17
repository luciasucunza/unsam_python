#termometro.py

import random
import numpy as np


n = 999
mu = 0
sigma = 0.2
T_real = 37.5

random.normalvariate(mu, sigma)

valores_t = [ (T_real+random.normalvariate(mu,sigma)) for i in range(n)]
np.save('Data/Temperaturas', valores_t)


print('Listado de todos los valores medidos:', valores_t)
print('Temperatura Máxima Medida:', max(valores_t))
print('Temperatura Mínima Medida:', max(valores_t))
print('Promedio de las Temperaturas Medidas:', sum(valores_t)/n)
valores_t.sort()
print('Mediana de las Temperaturas Medidas:', valores_t[n//2])
