class StringManipulator:
    """Docstring of StringManipulator"""

    category = 'Manipulator'

    def __init__(self, original):
        self.string = original

    def reverse_words(self):
        words = self.string.split() #mampy podzielic napis i odwrocic kolejnosc slow.
                                    # Domyslnie split dzieli po 'bialych znakach', czyli spacje, tabulacje, etc/ Jak podamy
                                    # argumenty to bedzie dzielil po tym co chcemy.
        self.string = ' '.join(reversed(words))

    def make_title(self):
        self.string = self.string.title()   #przypisujemy bo tak jest napisany test. Mozna tez zwrocic zmieniony wynik bez
                                            # przypisywania, gdyby test byl napisany inaczej.
    def stripped_title(self):
        self.string = self.string.strip()


    def get_manipulated(self):
        return self.string


assert StringManipulator.__doc__ == 'Docstring of StringManipulator'
assert StringManipulator.category == 'Manipulator'

str_manip = StringManipulator('cOOL pyThON')

str_manip.reverse_words()
assert str_manip.get_manipulated() == 'pyThON cOOL'

str_manip.make_title()
assert str_manip.get_manipulated() == 'Python Cool'

str_manip = StringManipulator('  cOOL pyThON   ')
str_manip.stripped_title()
str_manip.reverse_words()
assert str_manip.get_manipulated() == 'pyThON cOOL'

print('well done')