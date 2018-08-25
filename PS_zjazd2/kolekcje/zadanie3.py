listaliczb = [5, 3, 1, 3, 45, -1, -5, -2]
dodatnie = 0
ujemne = 0

'''
for i in listaliczb:
    if listaliczb[i]>0
        dodatnie += 1
    else:
        ujemne += 1

print(f'W liscie jest {dodatnie} liczb dodatnich')
print(f'W liscie jest {ujemne} liczb ujemnych')

'''

for i in listaliczb:
    if i > 0:
        dodatnie += 1
    if i < 0:
        ujemne += 1

print(f'W liscie jest {dodatnie} liczb dodatnich')
print(f'W liscie jest {ujemne} liczb ujemnych')


'''
for liczba in listaliczb:
    if liczba > 0:
        dodatnie += 1
    if liczba < 0:
        ujemne += 1

print(f'W liscie jest {dodatnie} liczb dodatnich')
print(f'W liscie jest {ujemne} liczb ujemnych')

'''