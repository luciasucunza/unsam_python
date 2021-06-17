#envido.py

import random

def repartir():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    
    return random.sample(naipes, k=3)
    
def buen_envido():
    mano = repartir()
    mano_h = []
    # La lista mano_h convierte las figuras en 0 para poder sumar luego en el envido
    # Se podría haber hecho al momento de la suma pero se me ocurrió esta forma primero
    for carta in mano:
        if carta[0] > 7:
            mano_h.append((0, carta[1]))
        else:
            mano_h.append(carta)
    
    # Ya sea por flor o no lo lo importante es que dos cartas del mismo palo sumen 31 o más
    if mano_h[0][1] == mano_h[1][1]:
        envido = mano_h[0][0] + mano_h[1][0] + 20
        if envido >= 31:
            return True
    elif mano_h[0][1] == mano_h[2][1]:
        envido = mano_h[0][0] + mano_h[2][0] + 20
        if envido >= 31:
            return True
    elif mano_h[1][1] == mano_h[2][1]:
        envido = mano_h[1][0] + mano_h[2][0] + 20
        if envido >= 31:
            return True
    return False

N = 100000
G = sum([buen_envido() for i in range(N)])
prob = G/N
print(f'Repartí {N} manos, de las cuales {G} saqué envido de 31, 32 o 33.')
print(f'Podemos estimar la probabilidad de sacar un envido de 31, 32 o 33 mediante {prob:.6f}.')