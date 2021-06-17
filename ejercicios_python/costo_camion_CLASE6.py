# costo_camion.py
import informe 

#------------Función:cost_camion()------------
def costo_camion(nombre_archivo):
    '''
    Calcula el costo total (cajones*precio) de un camión
    '''
    costo_total = 0    
    camion = informe.leer_camion(nombre_archivo)
    for fila in camion:
        costo_total += fila['cajones'] * fila['precio']
    return costo_total

#------------Función Principal------------
def main(parametros):
    # Analizar la línea de comandos, usando la variable parámetros en lugar de sys.argv
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    costo_total = costo_camion(parametros[1])
    print('Costo total: ', costo_total)

#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
    