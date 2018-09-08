class Dog:
    def __init__(self, energy = 10):    #funkcja ustawiajaca wejsciowe wartosci. Tu nie potrzebuje argumentu, bo nie chcemy go wprowadzac z bazy.
                                        # Jezeli chcemy to mozemy przypisac wartosc 'default'. Jezeli nie wprowadze atrybutu to
        #self.energy = 10
        self.energy = energy

    def bark(self):
        self.energy += -1

    def sleep(self):
        self.energy += + 2

    def get_energy(self):
        return self.energy


doge = Dog()
assert doge.get_energy() == 10

doge.bark()
doge.bark()
doge.bark()
assert doge.get_energy() == 7
