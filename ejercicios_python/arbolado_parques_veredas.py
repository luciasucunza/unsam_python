# arbolado_parques_veredas.py

import pandas as pd
import os

# Levantamos los archivos a dataframe
path = 'Data'
file_veredas = 'arbolado-publico-lineal-2017-2018.csv'
file_parques = 'arbolado.csv'
df_veredas = pd.read_csv( os.path.join(path, file_veredas) )
df_parques = pd.read_csv( os.path.join(path, file_parques) )

# Seleccionamos solo las filas correspondientes a las tipas y las columnas deseadas
col_v = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][col_v].copy()

col_p = ['nombre_cie', 'diametro', 'altura_tot']
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][col_p].copy()

# Renombramos las columnas de parques para que queden igual a las de vereda
df_tipas_parques = df_tipas_parques.rename( columns = {col_p[0]: col_v[0], 
                                                       col_p[1]: col_v[1], 
                                                       col_p[2]: col_v[2] } )
# Agregamos una nueva columna con 'ambiente'
df_tipas_veredas['ambiente'] = 'vereda'
df_tipas_parques['ambiente'] = 'parque'
col_v.append('ambiente')
# También sepodría cambiar para que en ambos df el nombre de la especie sea igual
# >>> df_tipas_parques['nombre_cientifico'] = 'Tipuana tipu'

# Concatenamos ambos dataframes para tener todos los datos de las Tipas juntos
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# Creamos un boxplot para los diametros a la altura del pecho, distinguiendo por ambiente
df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
# Creamos un boxplot para las alturas, distinguiendo por ambiente
df_tipas.boxplot('altura_arbol',by = 'ambiente')


#%%
'''
-Para hacer una función lo único que se tendría que tener en cuenta es como son
los nombres en cada dataframe:
    >>> a = analizarEspecie('Tipuana tipu','Tipuana Tipu' )
    >>> a.boxplot('diametro_altura_pecho', by='ambiente')
    
-Podrìa tambien pasarse los nombres de los archivos o los dataframes que quiero
usar para la busqueda.
-No pude dedicarle mucho tiempo a la clase así que lo dejo así

'''
def analizarEspecie(nom_cientifico_veredas, nom_cientifico_parques):
    ''' Obtiene los datos (altura, diametro, ambiente) para una cierta especie 
        de dos bases de datos distintas.
        
        Pre: los nombres usados para la misma especie tienen que peretenecer a 
            cada base de datos.
        Pos: Devuelve un dataframe, con los datos de diametro, altura y 
            ambiente de todos los arboles de una especie ubicados en la base de
            datos de las veredas y en la de los parques
    '''
    path = 'Data'
    file_veredas = 'arbolado-publico-lineal-2017-2018.csv'
    file_parques = 'arbolado.csv'
    df_veredas = pd.read_csv( os.path.join(path, file_veredas) )
    df_parques = pd.read_csv( os.path.join(path, file_parques) )

    col_v = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
    df_especie_veredas = df_veredas[df_veredas['nombre_cientifico'] == nom_cientifico_veredas][col_v].copy()
    col_p = ['nombre_cie', 'diametro', 'altura_tot']
    df_especie_parques = df_parques[df_parques['nombre_cie'] == nom_cientifico_parques][col_p].copy()

    df_especie_parques = df_especie_parques.rename(columns = {col_p[0]: col_v[0],
                                                              col_p[1]: col_v[1],
                                                              col_p[2]: col_v[2] } )
    df_especie_veredas['ambiente'] = 'vereda'
    df_especie_parques['ambiente'] = 'parque'
    col_v.append('ambiente')
    df_especie_parques['nombre_cientifico'] = nom_cientifico_veredas

    df_especie = pd.concat([df_especie_veredas, df_especie_parques])
    
    return df_especie

