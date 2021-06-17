# rebotes.py
altura      = 100
cant_saltos = 0

while cant_saltos < 10:
    altura = round(altura * 3 / 5, 4)
    cant_saltos +=1
    print(cant_saltos, altura)