dzien_start = int(input('W jakim dniu tygodnia zaczęła się naprawa u szefca? \nPon - 1, Wt - 2, Śr - 3, Czw - 4, Pt - 5, Sob - 6, Nd - 7\n\n'))
czas_naprawy = int(input('Ile dni będzie trwała naprawa?\n'))
dni_tyg = ('poniedziałek', 'wtorek', 'środę', 'czwartek', 'piątek', 'sobotę', 'niedzielę')

dzien_odbioru = (dzien_start + czas_naprawy)%7-1
print(f'Buty będą do odbioru w {dni_tyg[dzien_odbioru]}')
