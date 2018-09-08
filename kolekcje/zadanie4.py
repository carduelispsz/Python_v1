lista = list(range(1, 101))
ile_podzielnych = 0

#for liczba in range(101) - zamiast pierwszej linii powyzej

for liczba in lista:
    if liczba % 3 == 0 or liczba % 5 == 0:
        print(liczba)
        ile_podzielnych += 1

print(f'W przedziale 0-100 jest {ile_podzielnych} liczb podzielnych przez 3 lub 5')
#print(lista)
