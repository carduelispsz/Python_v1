import urllib.request
import json
#import requests - jak to sie sciagnie zamiast utllib to upraszcza troche skladnie sciagania json.


#Weather = namedtuple("Weather", ["location"])

miasto = input('Podaj nazwe miasta: ')
#miasto = 'warsaw'
#print(f"http://www.metaweather.com/api/location/search/?query={miasto}")
with urllib.request.urlopen(f"http://www.metaweather.com/api/location/search/?query={miasto}") as f:
    data = f.read()
    data = json.loads(data)
    #woeid = data[0]['woeid']

with urllib.request.urlopen(f"http://www.metaweather.com/api/location/{data[0]['woeid']}") as f:
    data = f.read()
    data = json.loads(data)

#print(data)

pogoda = (data['consolidated_weather'])

#print(pogoda)

for p in pogoda:
    print(f"{p['applicable_date']} - {p['the_temp']}")

# print(f'Pogoda w {miasto}'
#       f'- temperatura: {pozycja na liscie}'
#       f'- cisnienie: {}'
#       f'- wilgotnosc: {}')

