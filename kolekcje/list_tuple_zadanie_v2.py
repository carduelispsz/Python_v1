lista_liczb = []

while len(lista_liczb)<10:
    a = input('Podaj liczbę lub wpisz "k" by zakonczyc: ')
    if a == 'k':
        break
    else:
        a = int(a)
        lista_liczb.append(a)

print(lista_liczb[::])
srednia = sum(lista_liczb)/len(lista_liczb)
print(f'Srednia z podanych liczb to: {srednia}')