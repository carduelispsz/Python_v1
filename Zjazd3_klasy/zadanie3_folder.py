class ElectricCar:
    def __init__(self, max_range):
        self.range = max_range
        self.range_max = max_range
        self.driven = 0

    def car_drive(self, driven):
        if driven <= self.range:
            self.driven += driven
            self.range -= driven
        else:
            self.driven = self.range
            self.range = 0
        return self.driven

    def charge(self): # jak zrobic chargowanie na raty?
        self.range = self.range_max
        return self.range


def test_drive():
    car = ElectricCar(100)
    assert car.car_drive(70) == 70

def test_charge():
    car = ElectricCar(120)
    assert car.charge() == 120

def test_drive_many():
    car = ElectricCar(100)
    car.car_drive(40)
    car.car_drive(50)
    assert car.car_drive(70) == 10

print('Hurrey! Hurrey!')