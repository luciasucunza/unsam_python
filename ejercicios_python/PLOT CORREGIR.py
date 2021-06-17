# 

import numpy as np
from matplotlib import pyplot as plt

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
plt.figure(figsize=(8, 6), dpi=80)

# Crea un nuevo subplot, en una grilla de 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="coseno")

# Plotea el seno con una línea verde contínua de ancho 1 (en pixeles)
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="seno")

# Rango del eje x
plt.xlim(X.min() * 1.1, X.max() * 1.1)

# Ponemos marcas (ticks) en el eje x
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# Rango del eje y
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# Ponemos marcas (ticks) en el eje y
plt.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

# Podemos grabar el gráfico (con 72 dpi)
# plt.savefig("ejercicio_2.png)", dpi=72)

# gca es 'get current axis' ó 'tomar eje actual'
# Borramos el controno
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Pongo las leyenda arriba a la izquierda
plt.legend(loc='upper left')


# Función para hacer la linea punteada
t = 2 * np.pi / 3
# Pongo una linea punteada
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
# Pongo un puntito sobre la curva
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
# Pongo un cometario
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
              xy=(t, np.cos(t)), xycoords='data',
              xytext=(-90, -50), textcoords='offset points', fontsize=16,
              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# Pongo una linea punteada
plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
# Pongo el puntito sobre la curva
plt.scatter([t, ],[np.sin(t), ], 50, color='red')
# Pongo un cometario
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
              xy=(t, np.sin(t)), xycoords='data',
              xytext=(+10, +30), textcoords='offset points', fontsize=16,
              arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Agranda un poco la letras de las labels
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))


# Mostramos el resultado en pantalla
plt.show()

#%%
# Otra forma de hacer figuras

def cm2inch(value):
    return value/2.54

fig = plt.figure(figsize=(cm2inch(12.8), cm2inch(9.6)))

plt.axes([0.1,0.1,0.8,0.8]) 
plt.axes([0.2,0.2,0.3,0.3])

#%%
# Como hacer sublpots distintos

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 2x3
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la quinta figura si fuera una grilla regular de 2x3
plt.plot([0,1],[0.5,0.5])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la tercera de abajo, que sería la sexta figura si fuera una grilla regular de 2x3
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()

#%%
'''Gráfico de barras'''

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    
for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.ylim(-1.25, +1.25)

#%%
'''Gráfico en coordenadas polares'''

ax = plt.axes([0, 0, 1, 1], polar=True)

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

ax.set_xticklabels([])
ax.set_yticklabels([])

#%%
'''Scatter Plot'''
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

colors = np.arctan2(Y,X)

# S cambia el diametro de los circuitlos, c el color y alpha la transparencia
plt.scatter(X, Y, s=100,  c = colors, alpha = 0.75)
plt.xticks([]), plt.yticks([])
plt.xlim(-1.25, +1.25), plt.ylim(-1.25, +1.25)