import json

ob1 = ['aaa', 'eu', 3, 5, ['tra', 'ku']]

print(type(json.dumps(ob1)))

#zapis pliku
with open('example.json', 'w') as f:
    json.dump(ob1, f)

#otwieranie pliu
with open("example.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))
    data.append('dodany nowy element')

print(data)

with open('example.json', 'w') as f:
    json.dump(data, f)


