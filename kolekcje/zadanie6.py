liczby = [5, 2, 1, 4, 3]

'''
#drukuje indeksy liczb
print(list(range(len(liczby))))

for i in range(len(liczby)):
    print (i, liczby[i])

'''

# mozna jakos funkcja min i max wyszukujac index takich liczb i przepisujac je w 2ga strone

i = max(liczby)
j = min(liczby)

print(i)
print(j)

print(liczby)
#print (liczby.index(max(liczby)))

a = liczby.index(max(liczby))
b = liczby.index(min(liczby))

liczby[a], liczby[b] = liczby[b], liczby[a]

print(liczby)

#print(i)
#print(j)