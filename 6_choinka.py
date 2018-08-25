a = int(input('Podaj liczbe wierszy: '))
wiersz_numer = 1

while a >= wiersz_numer:
    print(' '*(a-wiersz_numer), end='')
    print('*'*(2*wiersz_numer-1), end='')
    print(' '*(a-wiersz_numer))
    wiersz_numer += 1
#while a <= wiersz_numer + wiersz_numer/5
    p