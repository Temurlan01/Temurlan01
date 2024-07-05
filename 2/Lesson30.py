#1. В этом задании вам нужно создать простой класс Car, который будет представлять автомобиль. Класс должен иметь атрибуты для марки (*mark), модели (*model),
#года выпуска (*year) и цену (*price) автомобиля. Затем создайте три объекта этого класса, общую сумму этих автомобилей
class Car:
    def __init__(self, mark_pm, model_pm, year_pm, price_pm):
        self.mark = mark_pm
        self.model = model_pm
        self.year = year_pm
        self.price = price_pm
    def car_info (self):
        print(f"marka:{self.mark}, model:{self.model}, year:{self.year}, price:{self.price}")


car1 = Car(mark_pm="BMW", model_pm="Z4 M40i Roadster", year_pm=2023, price_pm=5_320_002)
car2 = Car(mark_pm="Mercedes", model_pm="C118/X118", year_pm=2022, price_pm=4_002_900)
car3 = Car(mark_pm="Toyota", model_pm="Supra GTR", year_pm=2021, price_pm=2_234_000)
all_car_price = car1.price + car2.price + car3.price

car1.car_info()
print(all_car_price)