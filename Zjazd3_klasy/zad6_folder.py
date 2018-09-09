from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  #other nie musi byc tego samego typu co self i to dalej moze dzialac. Trzeba to tylko obsluzyc w implementacji
        return Vector(self.x + other.x, self.y + other.y)

    #mozna to tez zapisac tak:
    #new_x = self.x + other.x
    #new_y = self.y + otehr.y
    #v_ret = Vector(new_x, new_y)
    #return v_ret

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    @property
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __ne__(self, other):
        return self.length != other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __str__(self):
        return f'V({self.x},{self.y}):{self.length:.2f}'



def test_create():
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    assert v1.x == 1
    assert v1.y == 2

def test_dodawanie_wektorow():
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6

def test_odejmowanie_wektorow():
    v1 = Vector(1,2)
    v2 = Vector(3,4)
    v3 = v1 - v2
    assert v3.x == -2
    assert v3.y == -2

def test_mnozenie_przez_liczbe():
    v1 = Vector(1,2)
    v3 = v1 * 3
    assert v3.x == 3
    assert v3.y == 6

def test_len():
    v1 = Vector(3,4)
    assert v1.length == 5

def test_equal():
    v1 = Vector(2,3)
    v2 = Vector(2, 3)
    assert v1 == v2

def test_equal2():
    v1 = Vector(-2,3)
    v2 = Vector(2, 3)
    assert v1 == v2

def test_equal():
    v1 = Vector(3,4)
    v2 = Vector(0, 5)
    assert v1 == v2

def test_greater_than():
    v1 = Vector(3,6)
    v2 = Vector(0, 5)
    assert v1 > v2


def test_sorting():
    v1 = Vector(3,3)
    v2 = Vector(0, 5)
    v3 = Vector(0, 1)
    lista = [v1, v2, v3]
    assert sorted(lista) == [v3, v1, v2]

def test_liczby():
    a = 5
    b = 4
    c = a + b
    assert c == 9