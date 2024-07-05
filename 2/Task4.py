#Задание 4: «Музыкальный инструмент»
#Создайте класс Instrument с атрибутами для имени и стоимости инструмента.
#Создайте подкласс Guitar, который добавляет атрибут number_of_strings.
#Напишите метод для игры на гитаре (`play`).
#Создайте несколько объектов классов Instrument и Guitar и протестируйте их методы.

class Total:
    def __init__(self, name_pm: str, price_pm: int):
        self.name = name_pm
        self.price = price_pm
class Instrument(Total):
    def into_info (self):
        print(f"Название {self.name} ,стоимость {self.price}")
class Guitar(Total):
    def number_of_strings (self):
        print(12)
    def play(self):
        print("Дзннн")
drums = Instrument(name_pm="Барабаны", price_pm=20_000)
gitara = Guitar(name_pm="Гитара", price_pm=30_000)
drums.into_info()
gitara.play()
