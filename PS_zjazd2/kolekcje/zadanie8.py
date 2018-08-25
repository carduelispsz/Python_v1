# Napisz program zliczajacy liczbe liter pomiezdzy nawiasamo <> Nawiasy moga wystapic tylko raz

text = 'Ala ma <kota> a kot ma Ale'

start = text.find('<')
stop = text.find('>')

print(len(text[start+1:stop]))
print(stop-start-1)

# 2gie rozwiazanie

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