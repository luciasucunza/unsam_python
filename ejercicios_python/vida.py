# vida.py
'''
Puede probarse la función desde la consola de spyder:
    >>>print( segundosVividos('10/11/1996') )
    753842327.94042

Desde la consola del sistem operativo, estando en la carpeta del archivo>
    >>>python vida.py 10/11/1996
    Viviste  753842087.665608  segundos
    
'''
from datetime import datetime

#%%
def segundosVividos(fecha):
    ''' Obtiene la cantidad de segundos desde una fecha a las 00:00 hasta el día de hoy.
    
        Pre: el formato de la cadena con la cual se da la fecha debe ser:
                dd/mm/aaaa
        Pos: Devuelve un flotante, con todos los segundos que transcurrieron,
            desde la fecha pasada como argumento hasta el momento.
    '''
    fecha_nacimiento = datetime.strptime(fecha, '%d/%m/%Y')    
    fecha_hoy = datetime.now() 
    vida_segundos = (fecha_hoy-fecha_nacimiento).total_seconds()
    return vida_segundos



#------------Función Principal------------
def main(parametros):
    # Analizar la línea de comandos, usando la variable parámetros en lugar de sys.argv
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'archivo_camion archivo_precios')
    fecha = parametros[1]
    vida = segundosVividos(fecha)
    print('Viviste ',vida,' segundos')


#%%
if __name__ == '__main__':
     import sys
     main(sys.argv)
    