napis = 'ala ma jebanego kotaeettt'

litery = {}

for i in napis:
    if i in litery:
        litery[i] += 1
    else:
        litery[i] = 1

ilerazy = 3

print(litery)

for i in litery:
    if litery[i] > ilerazy:
        print(i)



def test_wiecej_niz_dla_pustego_napisu():
    assert ilerazy("", 1) == set()  # tworze funkcje ktora sprawdza czy w tym secie po lewej (nie ma w nim znakow, wiec jest pusty)
                                        # i przyrownuje go do zbioru (setu) po prawej. Zeby wyrazenie bylo spelnione 'True' to po prawej
                                        # musze utworzyc pusty zbior