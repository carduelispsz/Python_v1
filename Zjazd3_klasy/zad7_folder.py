from Zjazd3_klasy.zadanie2_folder import Employee


class PremiumEmployee(Employee):    #moznaby to zrobic przez dodanie funkcji w klasie employee. Ale dodanie nowej klasy pozwala na oddzielenie tego. Na przyklad jezeli projekt employee oddalismy

    count = 0 #klasa moze miec swoje zmienne dostepnej dla calej klsy

    def __init__(self, name = 'Jan', lastname = 'Kowalski', wage = 500, bonus = 0):
        super().__init__(name, lastname, wage)
        self.bonus = bonus
        sself.__class__.count += 1

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sal = super(PremiumEmployee, self).pay_salary()  #super.pay_salary()
        sal += self.bonus
        self.bonus = 0
        return sal

    @classmethod
    def emp_from_string(cls, str_param):
        list_param = str_param.split(';')
        return PremiumEmployee(list_param[0], list_param[1], int(list_param[2]), int(list_param[3]))

    @staticmethod  #nie korzysta ze stanu obiektu i nie potrzebuje dlatego selfa. Mozna to wywolywas???
    def say_hello():
        return 'Hello'

def test_import_from_text():
    param = 'Henryk;Zdun;50;0'
    emp = PremiumEmployee.emp_from_string(param)
    assert emp.name == 'Henryk'
    assert emp.lastname == 'Zdun'
    assert emp.wage == 50
    assert emp.bonus == 0

    @classmethod
    def create_hero(cls):
        return PremiumEmployee('pracownik', 'miesiaca', 0, 0)


def test_create_premium():
    emp = PremiumEmployee('Jan', 'Nowak', 100)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.wage == 100
    assert emp.bonus == 0


def test_register():
    emp = PremiumEmployee('Jan', 'Nowak', 100, 1000)
    emp.register_time(5)
    emp.give_bonus(1000)
    emp.give_bonus(500)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.bonus == 2500
    assert emp.pay_salary() == 3000

