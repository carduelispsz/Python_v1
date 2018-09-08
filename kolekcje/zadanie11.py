zbior = set()
zbior_0_100 = set(range(0, 101, 2))

#print(zbior_0_100)

while True:
    liczba = int(input('wprowadz liczbe: '))
    if liczba == 00:
        break
    zbior.add(liczba)

'''
w petli mozna napisac
    komenda = input("podaj lub k zeby zakonczyc")
    if komenda == k:
        break
    else:
        liczba= int(komenda)
        liczby
'''


print(len(zbior))
print(zbior)
print(len(zbior & zbior_0_100))

