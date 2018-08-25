from random import randint
licznik = 0
a=randint(0,1000)
#b=int(input('Zgadnij jaka liczba została wylosowana: '))

while True:
    b=int(input('Zgadnij jaka liczba została wylosowana: '))
    #b=int(input('Zgadnij kolejny raz: '))
    licznik +=1
    if a>b:
        print(f'Wylosowana liczba jest większa od {b}')
    elif a<b:
        print(f'Wylosowana liczba jest mniejsza od {b}')
    else:
        print(f'Gratulacje!!! Odgadłes ze wylosowana liczba to {b}\nUdało się w {licznik} próbach')
        break
