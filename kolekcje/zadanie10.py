napis = 'ala ma kota'

litery = {}

for i in napis:
    if i in litery:
        litery[i] += 1
    else:
        litery[i] = 1

for i in litery:
    print(f' {i} wystapila {litery[i]} razy')

'''
for i in napis:
    liczniki[i] = liczniki.get(1, 0) + 1

liczniki[i] to przypisanie dla licznika[i] (przy kazdym obrocie petli to i to kolejna litera z napisu) wiec dla kolejnej litery jest poprawiany licznik

efekt ten sam co if/else powyzej.
'''

