def czy_jest_pierwsza(danaliczba):
    #danaliczba = int(input('Podaj liczbe '))
    for x in range(2, danaliczba/2):
        if danaliczba%x == 0:
            return False
        else:
            return True
    #return True - Rafal tak napisal, bez linii z else

    print(liczby_pierwsze)



#def test_czy_jest_pierwsza_dla_liczby_pierwszej():
#    assert czy_jest_pierwsza(3)  #tu powinno byc zwrocone True
#    assert czy_jest_pierwsza(7)
#
#def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
#    assert not czy_jest_pierwsza(4)  #tu powinno byc zwrocone False
#    assert not czy_jest_pierwsza(10)


#def test_czy_jest_pierwsza_dla_liczby_pierwszej
