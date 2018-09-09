'''Zaimplementuj klase CashMachine umozliwiajaca wplacanie i wyplacanie pieniedzy. Zadbaj o to ay stan bankomatu przetrzymywany byl w zmienncyh przywatnych.'''


class CashMachine:
    def __init__(self):
        self._bills = dict()

    def is_available(self):
        return sum(self._bills.values()) > 0  # nie trzeba tu if bo w tej komendzie o sprawdz czy ta suma jest 'True'

    def put_money(self, list_of_money):
        for bill in list_of_money:
            self._bills[bill] = self._bills.get(bill, 0) + 1  # self._bills.get(bill, 0) - przeszukuje klucze slownika 'self.bills' i porownuje do wartosci w liscie ktora dostalismy. Jak znajdzie '100'; to dodaje do klucza '100' w slowniku, dla klucza '200' do dwusetek

    def withdraw_money(self, amount):
        list_of_bill = sorted(self._bills.keys(), reverse=True)
        ret_value = []
        for bill in list_of_bill:
            while self._bills[bill] > 0 and amount - bill >= 0:
                ret_value.append(bill)
                ret_value[bill] -= 1
                amount -= bill
        if amount ==0:
            return ret_value
        else:
            self.put_money(ret_value)
            return[]

def test_create():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()  # moznaby napisac ze assert .... == False, ale to ponoc slabe jest i lepiej napisac assert not

def test_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()

def test_withdraw():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]

def test_withdraw_more_than_available():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(500) == []

def test_withdraw_after_not_complete_withdrawal():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()

def test_withdraw_after_not_complete_withdrawal():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available(330) == []

def test_withdraw_after_not_complete_withdrawal():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50, 20, 20, 20, 10, 20, 20, 20])
    assert cash_machine.is_available(330) == [200, 100, 20, 10]