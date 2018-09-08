a = int(input('Podaj  liczbe wierszy: ')
liczbaznakow = a
wiersz_numer = 1


while a <= wiersz_numer:
    if liczbaznakow == 1:
        print('', end='')
    elif 1 < liczbaznakow < (2 * a - 2):
        print('*', end='')
    else:
        print('')
    wiersz_numer += 1
