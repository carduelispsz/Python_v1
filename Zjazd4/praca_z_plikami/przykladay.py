#with open('pliki_wejsciowe/dane.txt') as plik:


with open(r'C:\Users\kurs', 'w') as f:  #r - 'raw text' mam na mysli to co jest napisane. Inaczej moze pokazywac '\n\ jako nowa linie w pycharmie.
                                        #  'w' - plik otwarty do odczytu; 'a' - plik otwarty do dodawania append
    f.write('To jest nowy plik')

