class Rectangle:

    def __init__(self, dlina_pm, shirina_pm):
        self.dlina = dlina_pm
        self.shirina = shirina_pm

    def calculate_perimeter(self):
        result = 2 * (self.dlina + self.shirina )
        return result

r1 = Rectangle(dlina_pm=4, shirina_pm=5)
r2 = Rectangle(dlina_pm=15, shirina_pm=2)
perimeter1 = r1.calculate_perimeter()
print(perimeter1)



