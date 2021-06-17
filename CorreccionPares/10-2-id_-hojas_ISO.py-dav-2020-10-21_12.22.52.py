# hojas_ISO.py
# Alumno = David Pazos

def hojas_iso(n):

    if n == 0:
        largo = 1189
        ancho = 841
                
        return largo,ancho
    else:
        ancho,largo = hojas_iso(n-1)
        ancho = ancho//2
        return largo,ancho