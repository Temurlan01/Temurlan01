#Задание 2: «Треугольник»
#Создайте класс Triangle с атрибутами для первой, второй и третьей стороны.
#Напишите метод который вернет периметр, и также метод для площади (*знайте все три стороны треугольника можно найти площадь с помощью специальной формулы*).

class Triangle:
    def __init__(self,first_side_pm, second_side_pm,third_side_pm):
        self.first_side = first_side_pm
        self.second_side = second_side_pm
        self.third_side = third_side_pm

    def calculate_perimeter(self):
        result = self.third_side + self.second_side + self.third_side
        return result
    def calculate_Ploshad(self):
        result = self.third_side + self.second_side * 2
        return result

Treugol = Triangle(first_side_pm=15, second_side_pm=15, third_side_pm=10)
perimetr = Treugol.calculate_perimeter()
ploshad = Treugol.calculate_Ploshad()
print(perimetr)
print(ploshad)