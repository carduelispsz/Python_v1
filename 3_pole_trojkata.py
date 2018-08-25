from math import sqrt

a = float(input('Podaj dlugosc pierwszego boku: '))
b = float(input('Podaj dlugosc drugiego boku: '))
c = float(input('Podaj dlugosc trzeciego boku: '))
p = (a+b+c)/2

if a+b>c and b+c>a and c+a>b:
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print (f'Pole powierzchni trojkata o takich bokach to {s}')
else:
    print ('Z odcinków o takich długościach nie da się zbudowac trójkąta')