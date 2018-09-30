class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self, sound = 'kncok kncok'):
        self.sound = sound
        return self.sound


# class Cat(Animal):
#     def __init__(self, name, age, sound):
#         super().__init__(self, name, age)
#         self.sound = sound


def test_nazwa_zwierza():
    animal = Animal('Strange thing', 1000)
    assert animal.name == 'Strange thing'
    assert animal.age == 1000
    assert animal.sound == 'kncok kncok'