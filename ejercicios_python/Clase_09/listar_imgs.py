# listar_imgs.py
'''
Desde la consola lo probé con:
    python listar_imgs.py C:\\Users\\........\\ejercicios_python\\Data
Previamente había probado la función desde el spyder con:
    >>>path = 'C:\\Users\\........\\ejercicios_python\\Data'
    >>>filesPNG = onlyPNG(path)
    >>>for i, file in enumerate(filesPNG):
    >>>    print(i, ':', file)
'''


import os

def onlyPNG(path):
    files_tot = []
    for root, dirs, files in os.walk(path):
        files_tot += files
        
    files_PNG = [ name for name in files_tot if name[-4:] == '.png']
    
    return files_PNG

#------------Función Principal------------
def main(parametros):
    # Analizar la línea de comandos, usando la variable parámetros en lugar de sys.argv
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {parametros[0]} ' 'directorio')
    path = parametros[1]
    filesPNG = onlyPNG(path)
    print('Todos los archivos PNG del directorio', path)
    for i, file in enumerate(filesPNG):
        print(i, ':', file)


#%%
if __name__ == '__main__':
     import sys
     main(sys.argv)


