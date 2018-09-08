class Product:
    def __init__(self, id, typ, cena):
        self.id = id
        self.typ = typ
        self.cena = cena

    def print_info(self):
        print(f'"{self.typ}", id: {self.id}, cena: {self.cena}PLN')


def test_product_exist():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.typ == 'Woda'
    assert product.cena == 10.99

def test_print_info(capsys):
    product = Product(1, 'Woda', 10.99)
    product.print_info()
    out, _ = capsys.readouterr()
    assert out == '"Woda", id: 1, cena: 10.99PLN\n' #To \n jest potrzebne bo funkcja print dodaje nowa linię z defaultu
    #assert product.print_info() == '"Woda", id: 1, cena: 10.99PLN'