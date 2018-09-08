class Employee:
    def __init__(self, name, lastname, wage):
        self.name = name
        self.lastname = lastname
        self.wage = wage
        self.registered_time = 0

    def register_time(self, hours):
        self.registered_time += hours

    def pay_salary(self):
        if self.registered_time <= 8:
            self.salary = self.registered_time * self.wage
        else:
            self.salary = (self.registered_time-8) * self.wage *2 + 8 * self.wage
        self.registered_time = 0
        return self.salary


def test_employee_pay_salary():
   employee = Employee('Jan', 'Nowak', 100)
   employee.register_time(5)
   employee.register_time(5)
   assert employee.pay_salary() == 1200
   employee.register_time(12)
   assert employee.pay_salary() == 1600
