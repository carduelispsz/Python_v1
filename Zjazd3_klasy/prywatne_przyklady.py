class Product:
    def __init__(self, id, name, price): #jesli dopuszczamy discount jako zmienna na wejsciu wtedy tu dajemy discount. Jezeli ustawiamy wartosc jako 0 dla nowych produktow to mozna to ustawic w init
        self._id = id
        self._name = name
        self.price = price
        self._discount = 0

    @property
    def full_name(self):
        return 'Product: ' + self._name

    @property
    def discount_price(self):
        return self.price * 0.8

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if type(value) == float: #type mozna napisac type(value) == type(0.1)
            self._id = value
        else:
            print('podaj wartosc numeryczna')

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if 0 <= value <= 0.3:
            self._discount = value
        else:
            print('Nie dajemy takich znizek')

    @discount.deleter
    def discount(self):
        self.discount = 0
        #del self.discount  - taka komenda kasuje atrybut i juz nie mozna sie do niego odwolac

pr1 = Product(1, 'bułka', 10, 1)

print (pr1.price)

pr1.id = 5.0
print(pr1.id)
pr1.id = 'ala'
print(pr1.id)

print(pr1.discount)
pr1.discount = 0.9
print(pr1.discount)
pr1.discount = 0.6
print(pr1.discount)


pr1.name = 'abrakadabra'
print(pr1.name)
pr1.name = 'aa'
print(pr1.name)
pr1.name = 'aarr'
print(pr1.name)