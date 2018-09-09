class Product:
    def __init__(self, id, name, cena):
        self.id = id
        self.name = name
        self.price = cena

    def print_info(self):
        return f'"{self.name}", id: {self.id}, cena: {self.price} PLN'

class BasketEntry:
    def __init__(self, product, number):
        self.product = product
        self.number = number

    def count_entry_price(self):
        return self.product.price * self.number #wyciagam self.product a z niego .price


class Basket:
    def __init__(self):
        self.entries = []


    def add_product(self, product, number):
        #products_in_basket = [x[0] for x in self.entries] #wylistuje nazwy produktow bez liczby
        products_in_basket = [x.entries for x in self.entries]
        if product in self.entries:
            pass
        else:
            entry = BasketEntry(product, number)
            self.entries.append(entry)

    def count_total_price(self):
        suma = 0
        for entry in self.entries:
            suma += entry.count_entry_price()
        return suma


def test_product_exist():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99

def test_print_info(capsys):
    product = Product(1, 'Woda', 10.99)
    product.print_info()
    wyjscie = capsys.readouterr()
    out = wyjscie[0]
    assert out == '"Woda", id: 1, cena: 10.99 PLN\n'
    product = Product(1, 'Piwo', 10.99)
    product.print_info()
    wyjscie = capsys.readouterr()
    out = wyjscie[0]
    assert out == '"Piwo", id: 1, cena: 10.99 PLN\n'

def test_basket_initialization():
    basket = Basket()
    assert basket.entries == []

def test_basket_add_product():
    basket = Basket()
    product = Product(1, 'Piwo', 10)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1

def test_basket_add_two_products():
    basket = Basket()
    product1 = Product(1, 'Woda', 10)
    product2 = Product(1, 'Piwo', 10)
    basket.add_product(product1, 5)
    basket.add_product(product2, 5)
    assert len(basket.entries) == 2


def test_basket_add_product_twice():
    basket = Basket()
    product = Product(1, 'Piwo', 10)
    basket.add_product(product, 5)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1

def test_count_entry_price():
    product = Product(1, 'Piwo', 10)
    entry = BasketEntry(product, 10)
    assert entry.count_entry_price() == 10*10

def test_basket_count_total_price():
    basket = Basket()
    product1 = Product(1, 'Woda', 10)
    product2 = Product(1, 'Piwo', 10)
    basket.add_product(product1, 5)
    basket.add_product(product2, 5)
    assert basket.count_total_price() == 50+50