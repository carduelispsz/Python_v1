# def formatuj(*napisy):
#
#     return napisy
#
#
# def test_formatuj_napisbezznacznikow():
#     assert formatuj("Hello World") == "Hello World"
#
# def test_formatuj_wiele_napisow():
#     assert formatuj("Hello World", "jestem Przemek", "blah blah") == "Hello World"


def formatuj(*napisy):
    pass


def test_formatowanie1():
    assert formatuj('koszta $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto')