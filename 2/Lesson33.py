#4. Вам необходимо создать класс для представления треугольника. Класс должен уметь вычислять периметр и площадь треугольника по его сторонам.
#Требования:
#Создайте класс Triangle, который содержит следующие атрибуты: a, b,
#Реализуйте метод perimeter, который вычисляет периметр треугольника:
#Реализуйте метод area, который вычисляет площадь треугольника, используя формулу Герона. (*загуглите эту формулу)

class Triangle:
    def __init__(self, a_pm, b_pm,c_pm):
        self.a = a_pm
        self.b = b_pm
        self.c = c_pm
    def perimetr(self):
        sum = 2 * (self.a + self.b + self.c)
        print(sum)
    def area(self):
        sum = (self.a + self.b + self.c)
        print(sum)
triangle = Triangle(a_pm=4, b_pm=5, c_pm=3)
triangle.perimetr()
triangle.area()