

lista = [x/10 for x in range(11)]
print(lista)

b = {(x, x**2, x**3) for x in range(-10, 11)}
print(b)

napisy = ['aa', 'yyyy', 'faewf', 'tedfgrs']
c = {x: len(x) for x in napisy}

print(c)