class Employee:
    def __init__(self, name_pm:str, working_hours_pm: int, wage_pm: int):
        self.name = name_pm
        self.working_hours = working_hours_pm
        self.__wage = wage_pm
    def get_Wage(self):
        return self.__wage

class Meneger(Employee):

    def increase_Personal(self, emploee_object:Employee ):
        emploee_object
    pass

Personal = Employee("Бека", 13,12_000)

zarplata = Personal.get_Wage()

Meneger.increase_Personal()

