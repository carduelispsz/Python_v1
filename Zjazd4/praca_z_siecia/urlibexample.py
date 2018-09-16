import urllib.request
import json

f = urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/a?format=json")

print(f.status)
print(f.read)

data = f.read()
data = json.loads(data)

print(type(data))

print(data[0]['rates'])

kursy = data[0]['rates']  # data[0] wybiera pierwszy element z listy bo dane w json'ie dostalismy w formie listy.
for kurs in kursy:
    print(f"{kurs['currency']} - {kurs['code']} - {kurs['mid']}")
