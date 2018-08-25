wiek = int(input('Podaj swój wiek: '))
liczba_nocy = int(input('Ile nocy spędzisz w hotelu?  '))

if wiek < 18:
    cena = 100 * liczba_nocy
elif 18<= wiek < 65:
    if liczba_nocy == 1:
        cena = 200
    elif 1 < liczba_nocy <= 4:
        cena = 180 * liczba_nocy
    else:
        cena = 150 * liczba_nocy
#if wiek>=65:
else:
    if liczba_nocy == 1:
        cena = 180
    elif 1 < liczba_nocy <= 4:
        cena = 162 * liczba_nocy
    else:
        cena = 135 * liczba_nocy
        
print (f'Cena za nocleg to {cena} PLN')