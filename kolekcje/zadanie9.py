# kwota za zakupiony towar na podstawie wagi i nazwy. Uzyj slownika do przechowywania danych. Wypisz wszystkie dostepne produkty w sklepie

lista_produkty = {'chleb': 3, 'bulki': 1, 'piwo': 4, 'hulajnoga': 15, 'ogorki': 2, 'rzodkiewka': 2, 'cytryna': 3,
                  'ziemniaki': 2}

# print(lista_produkty)

#print(f'Mamy: {lista_produkty.keys()}')

for p in lista_produkty:
    print(f'- {p} -- {lista_produkty[p]}')

produkty = input(f'Jaki towar chcesz kupic\n')

ilosc = float(input('Ile tego porzebujesz?\n'))

cena = lista_produkty[produkty]

rachunek = cena * ilosc

print(f'Twoj rachunek to {rachunek}')
