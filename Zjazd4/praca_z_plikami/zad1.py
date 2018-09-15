import sys

# try:
wejscie = sys.argv[1]   #mozna ponizej wpisac wyjscie zamiast sys.argv[1]. To sys.argv[1] odwoluje sie do argumentu w liscie utworzonej przez wpisanie z konsoli
                        # w konsoli Rafal wpisywal 'python zad1.py pliki_wejsciowe\emails.txt  - to tworzylo liste z argumentami [zad1.py, pliki_wejsciowe\emails.txt]. Mozna tu dodac
                        # kolejne argumenty ktore na przyklad beda wyjsciem i w ktorych bedzie zapisywany wynik dzialania na pliku.
with open(sys.argv[1]) as f:
    dane = f.read()
    dane = dane.splitlines()
    for i, linia in enumerate(dane, start=1):
        print(f'{i}: linia')

