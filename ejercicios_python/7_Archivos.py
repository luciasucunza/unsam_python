# 7_Archivos.py


import os
import datetime
import time

#%% Boludeces
os.getcwd()                     
os.chdir('..')
os.chdir('./ejercicios_python')
os.listdir()
os.mkdir('carpeta') 
os.rename('carpeta','test')
os.rmdir('test')  

#%%
'''
Dependiendo del sistema operativo, un archivo puede tener asociadas diferentes 
fechas:     de creación original
            de modificación del contenido
            de cambio en sus metadatos
            de acceso para lectura
Vamos a cambiar la fecha de modificación de un archivo. 
Para ello necesitás importar os y datetime. 
Luego, converís la fecha a timestamp y se la asocías al archivo con utime.
'''
camino = './rebotes.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))
