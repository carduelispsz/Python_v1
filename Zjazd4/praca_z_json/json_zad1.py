import json


class Employee():
    def __init__(self, imie, nazwisko, rok_urodzenia, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok_urodzenia = rok_urodzenia
        self.pensja = pensja


def dane_do_zapisu():
    imie = input('Imie: ')
    nazwisko = input('Nazwisko: ')
    rok_urodzenia = int(input('Rok urodzenia: '))
    pensja = float(input('Pensja: '))

    dane = {
        'imie': imie,
        'nazwisko': nazwisko,
        'rok_urodzenia':rok_urodzenia,
        'pensja':pensja
    }

    return dane

def zapisz(wklad):#ten 'wklad' to wynik
    with open('pracownicy.json', 'w') as f:
        json.dump(wklad, f)

def wypisz(wklad):
    for nr, pracownik in enumerate(employees, start=1)
        print(
            f" [nr] "
        )

#    def add_entry(self):


# new = ['Jan', 'Nowak', '1980', '5000']
#
# with open('employees.json', 'w') as f:
#     json.dump(new, f)

# with open('employees.json') as f:
#     dane = json.load(f)

try:
    with open(employees.json) as f:
        employees = json.load(f)
except FileNotFoundError:
    employees = []


komenda = input('Co chcesz zrobic: ')
if komenda == 'w':  # print
    wypisz(employees)
elif komenda == 'd':
    dane = dane_do_zapisu()
    employees.append(dane)
    zapisz(employees)#to employees jest wsadem do komendy zapisz. Tam jest to nazwane 'wklad'.

# if komenda == 'w':
#     with open('employees.json') as f:
