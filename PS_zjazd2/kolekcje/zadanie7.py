ile_samoglosek = 0
SAMOGLOSKI = 'aeiouy'

tekst = input('Napisz zdanie, najlepiej dlugie:\n')

# if y == '':
#   y = ('Miałes napisac jakies dlugie zdanie, ale niech bedzie ze uzyjemy tego.')

# print(tekst)

for i in tekst:
    if i.lower() in SAMOGLOSKI:
        ile_samoglosek += 1

print(f'Znalezione {ile_samoglosek} samoglosek')
