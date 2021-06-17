# costo_camion.py
'''Preparado para correr por consola, por ejemplo:
    python costo_camion.py Data/camion.csv 
'''

import informe 

#%%------------Función:cost_camion()------------
def costo_camion(nombre_archivo):
    '''
    Calcula el costo total (cajones*precio) de un camión
    '''
    camion = informe.leer_camion(nombre_archivo)
    return camion.precio_total()

#%%------------Función Principal------------
def main(parametros):
    # Analizar la línea de comandos, usando la variable parámetros en lugar de sys.argv
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion')
    costo_total = costo_camion(parametros[1])
    print('Costo total: ', costo_total)

#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
