import pandas as pd
import seaborn as sns
import os
import numpy as np

directorio = 'Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
cant_ejemplares = df['nombre_com'].value_counts()
cols = ['altura_tot', 'diametro', 'inclinacio'] 
df_jacarandas = df_jacarandas[cols]
df_jacarandas.tail()
df_jacarandas.describe()


sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')


# Acceder por indice 
df.loc[165]
cant_ejemplares.loc['Eucalipto']

# Acceder por posición
df_jacarandas.iloc[0]
cant_ejemplares.iloc[0]

# Acceder por rebanadas, de columnas, filas o columnas+filas
cant_ejemplares.iloc[0:3]
df_jacarandas.iloc[-5:,0:2]

# Acceder por columnas, una columna es una SERIE
df_jacarandas_diam = df_jacarandas['diametro']

# Crear series de tiempo:
pd.date_range('20200923', periods = 7)              #Separados por días
pd.date_range('20200923', periods = 7, freq='H')    #Separados por horas

pd.Series( [1, 2, 3, 4, 5, 6], index=pd.date_range('20200923 14:00', periods=6, freq='H') )

#%%
# Ejemplo caminatas
idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s2 = pd.Series(np.random.randint(-1,2,120).cumsum(), index = idx)
s3 = s2.rolling(3).mean()                   # con el valor puedo cambiar cuanto promedia
df_series_23 = pd.DataFrame([s2, s3]).T     # armo un dataframe con ambas series
df_series_23.plot()
#%%
# Otro ejemplo
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()
w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas para los datos suavizados
df_walk_suav.plot()

df_walk_suav.to_csv('caminata_apostolica.csv')

#%%
# Ultimo ejemplo 
# Levantamos el archivo a un dataframe
path = 'Data'
file = 'arbolado-publico-lineal-2017-2018.csv'
df = pd.read_csv( os.path.join(path, file) )

# Seleccionamos algunos campos 
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]

# Ploteamos las diez especies más frecuentes con sus cantidades
cant_ejemplares = df['nombre_cientifico'].value_counts()
print(cant_ejemplares.iloc[0:10])

# Seleccionamos algunas especies
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

# Gráfico del díametro y de las alturas por separado
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

# Gráicos pairplot
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
# ancho_acera no tiene lugar en el gráfico porque algunos datos faltan

