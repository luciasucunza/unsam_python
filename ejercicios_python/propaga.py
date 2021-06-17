# propaga.py
"""
ESTADOS POSIBLES
     0 ---> Nuevo
     1 ---> Encendido
    -1 ---> Carbonizado
"""
def propagar(L):
    L_prop = []
    flag_nuevos = 0
    flag_encendido  = False
    for i, l in enumerate(L):
        if l == 0:
            if flag_encendido:
                L_prop.append(1)
            else:
                L_prop.append(l)
                flag_nuevos += 1
        elif l == -1:
            L_prop.append(l)
            flag_nuevos = 0
            flag_encendido = False
        else:
            L_prop.append(l)
            for a in range(0,flag_nuevos+1,1):
                L_prop[i-a] = 1
            flag_nuevos = 0
            flag_encendido = True
    return L_prop

# propagar([ 0, 0, 0, 1, 0, 0])
    # [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
# propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
    # [ 1, 1, 1, 1, 1, 1]