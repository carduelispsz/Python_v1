lista_liczb = []

while len(lista_liczb)<10:
    a = int(input('Podaj liczbę: '))
    lista_liczb.append(a)

print(lista_liczb[::])
srednia = sum(lista_liczb)/len(lista_liczb)
print(f'Srednia z podanych liczb to: {srednia}')