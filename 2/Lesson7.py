class Car:
    def __init__(self,  make_pm: str, mode_pm: str, year_pm: int, mileage_pm: int, ):
        self.make = make_pm
        self.mode = mode_pm
        self.year = year_pm
        self.__mileage = mileage_pm
    def drive(self, distence):
        self.__mileage += distence
        return self.__mileage

class Fleet:
    def __init__(self):
        self.cars = []

    def add_car(self, new_car: Car):
        self.cars.append(new_car)
        return self.cars
    def  remove_car(self, make: str, model:str):
     pass

car1 = Car(make_pm="BMV", mode_pm="M5", year_pm=4, mileage_pm=1000)
car2 = Car(make_pm="MER", mode_pm="E38", year_pm=6, mileage_pm=2300)

cars = Fleet()
print(car1.drive(100))
print(cars.add_car(car1))