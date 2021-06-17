# hojas_ISO.py

def hoja_ISO(n):
    '''
    Precondición: n debe ser un número entero mayor a 0
        Devuelve: el ancho y el largo de la hoja A(N) en milimetros
    '''
    
    if n == 0:
        ancho = 841
        largo = 1189
        
    else:
        pre_ancho, pre_largo = hoja_ISO(n-1)
        
        # Se invierten las dimensiones y la que era mayor se divide por dos
        if pre_ancho > pre_largo:
            largo = pre_ancho//2
            ancho = pre_largo
        else:
            largo = pre_ancho
            ancho = pre_largo//2
        
    return ancho, largo


#%%
n = 5
print('Primeros', n, 'tamaños de hoja:')
for i in range(n):
    ancho, largo = hoja_ISO(i)
    print('Hoja A', i, ':', ancho, 'x', largo, 'mm')
