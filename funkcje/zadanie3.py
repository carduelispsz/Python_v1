def text(podany_tekst, znak_start, znak_stop):
        start = podany_tekst.find(znak_start)
        stop = podany_tekst.find(znak_stop)
        return(len(text[start+1:stop]))
    #print(stop-start-1)


podany_tekst = input('Podaj tekst: ', 'Ala ma <kota> aaattt')

    #('Ala ma <kota> a kot ma ale')

print(text(podany_tekst, '<', '>'))

# 2gie rozwiazanie
'''
czy_jest_pomiedzy_nawiasami =False
liczba_znakow_miedzy_nawiasami = 0

for l in text:
    if l == '<':
        czy_jest_pomiedzy_nawiasami = True
    elif l == '>':
        czy_jest_pomiedzy_nawiasami = False #break
    elif czy_jest_pomiedzy_nawiasami: # to wyrazenie sprowadza sie do 'if True' to podlicz a jak 'False' to nie licz
        liczba_znakow_miedzy_nawiasami += 1

print(liczba_znakow_miedzy_nawiasami)
'''
#def test():
#    assert ile_znakow(<aa>) == 2