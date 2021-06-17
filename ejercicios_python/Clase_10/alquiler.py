# alquiler.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

#%%
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

x_recta = np.linspace(start = superficie.min(), stop = superficie.max(), num = 1000)
y_recta = a*x_recta + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('Ajuste lineal')
plt.plot(x_recta, y_recta, c = 'green')
plt.xlabel('Superficie [m^2]')
plt.ylabel('Alquiler [10^3 $]')
plt.show()

#%%

# Calculo del error cuadrático medio como se muestra en la clase
errores = alquiler - (a*superficie + b)
print('Listado de errores para cada valor:', errores)
print('Error Cuadrático Medio calculado:', (errores**2).mean())


# Calculo del error cuadrático medio utilizando la librería 'sklearn.metrics'
ecm = mean_squared_error(alquiler, a*superficie + b) 
print('Error Cuadrático Medio (usando librería sklearn):', ecm)