# ma liczyc znaki miedzy nawiasami. Czyli jak 2gi poziom to kazdy znak liczy sie za 2


def policz_znaki(napis, arg1='<', arg2='>'):
    if arg1 == arg2:
        raise ValueError ('Znaki poczatku i konca nie moga byc takie same')
    ile_znakow = 0  # ustawiamy poczatkowe poziomy zmiennych
    poziom = 0
    for litera in napis:
        if litera == arg1:
            poziom += 1
            #continue
        elif litera == arg2:
            poziom -= 1
        elif poziom > 0:
            ile_znakow += poziom
    return ile_znakow

policz_znaki = ('ala ma <kota [a kot]> ma ale','[',']')

#napis = input('Podaj napis: ')
#arg1 = input('Podaj znak poczatku: ')
#arg2 = input('Podaj znak konca: ')
print(policz_znaki())

'''

def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki('') == 0

def test_policzznakigdybraknawiasow():
    assert policz_znaki('Ala ma kota') == 0

def test_nawiasy1poziom():
    assert policz_znaki('Ala <ma> kota') == 2

'''