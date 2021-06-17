# 7_extras

#%%
'''
Escribí un programa que asista a los técnicos del canal indicándoles, al 
correr el programa el número que deben poner en la placa
'''

from datetime import date

def diasPrimavera():
    ''' Obtiene la cantidad de dìas que faltan para la primavera
    
        Pos: Devuelve un entero, con la cantidad de dìas que faltan
    '''
    fecha_hoy = date.today()    
    primavera = date(fecha_hoy.year,9,21)
    
    if (primavera-fecha_hoy).days >= 0:
    # No pasó la primavera de este año
        prox_primavera = primavera
    else:
    # Ya pasó la primavera de este año
        prox_primavera = date(fecha_hoy.year+1,9,21)
         
    return (prox_primavera-fecha_hoy).days 

#------------Función Main------------
def main(parametros):
    dias = diasPrimavera()
    print('FALTAN',dias,'DIAS PARA LA PRIMAVERA')

if __name__ == '__main__':
     import sys
     main(sys.argv)



#%%
'''
Si tenés una licencia por xaternidad que empieza el 26 de septiembre de 2020 y 
dura 200 días, ¿qué día te reincorporás al trabajo?
    >>>from datetime import date, timedelta
    >>>fecha_licencia = date(2020, 9, 26)  
    >>>fecha_reincorp = fecha_licencia + timedelta( days=200 ) 
    >>>print('La fecha de reincorporaciòn serà:', fecha_reincorp)

'''



#%%
'''
Calcule los días hábiles entre dos fechas dadas. 

Argumentos:  el día inicial
             el día final
             lista con las fechas correspondientes a los feriados que haya
             
Retornar:    lista con las fechas de días hábiles del período
             incluyendo la fecha inicial y la fecha final indicadas. 

Las fechas de entrada y salida deben manejarse en formato de texto.

PRUEBAS:
    
# feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
# a = diasHabiles('30/9/2020', '10/10/2020', feriados)
# b = diasHabiles('30/9/2020', '31/12/2020', feriados)

'''
from datetime import timedelta

def diasHabiles(inicio, fin, feriados):
    
    dias_habiles = []
    
    inicio = inicio.split('/')
    fin = fin.split('/')
    d_inicio = date( year=int(inicio[2]), month=int(inicio[1]), day=int(inicio[0]) )
    d_fin = date( year=int(fin[2]), month=int(fin[1]), day=int(fin[0]) )
    
    #recorro los días desdde inicio a fin
    for i in range((d_fin-d_inicio).days+1):
        fecha = d_inicio + timedelta( days=i )
        # Si es entre semana, 5 (sábado) y 6 (domingo)
        if fecha.weekday() < 5:
            # Si el día es entre semana me fijo si esta dentro de los feriados
            # pero primero lo paso a formato texto
            f = '/'.join([str(fecha.day), str(fecha.month), str(fecha.year)])
            if not f in feriados:
                dias_habiles.append(f)
    
    return dias_habiles
