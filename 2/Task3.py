#Задание 3: «Персонал»
#Создайте класс Employee с атрибутами для имени и стажа работы (*стаж/опыт измеряется в годах).
#Напишите метод для самопредставления сотрудника, то есть сотрудник должен сказать/напечатать свое имя и стаж работы. (*метод может ничего не возвращать)
#Напишите метод для повышения стажа работы.
#Унаследуйтесь от класса Employee  и создайте подкласс Manager
#Напишите для класса Manager метод fire, данный метод будет принимать объект класса  Employee . И будет печататься что-то вроде “Сотрудник Бека уволен менеджером Асан”.
#Создайте несколько объектов классов Employee и Manager и протестируйте их методы.

class Employee:
    def __init__(self, name_pm, working_hours_pm):
        self.name = name_pm
        self.working_hours = working_hours_pm

class Meneger(Employee):
    def fire(self,worker):
        print(f"Сотрудник {worker.name} уволен менеджером {self.name}")

worker1 = Employee(name_pm="Бека", working_hours_pm=5)
Meneger1 = Meneger(name_pm="Астан", working_hours_pm=10)

Meneger1.fire(worker=worker1)
