liczby = [1, 3, 5, 7, 9, 11, 13, 15, 22, 123]



print('pierwszy: ',liczby[0])
print('przedostatni: ',liczby[-2])
print('Od 3 do 7: ',liczby[2:7])
print('pierwszy: ',liczby[-2])
print('Co trzeci: ',liczby[::3])
print('Co drugi od konca: ',liczby[::-2])
print('Co drugi od konca: ',liczby[::-2])
print(liczby[::])

liczby.append(12)

print(liczby[::])
liczby.pop()
print(len(liczby))

print(liczby[::])