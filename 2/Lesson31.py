#2. Создайте базовый класс Person, который включает атрибуты name и age, а также метод display_info. Затем создайте подкласс Teacher,
#который наследует класс Person и добавляет атрибут subject и метод display_teacher_info, который дополнительно выводит информацию о предмете преподавания.
class Person:
    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm

    def display_info(self):
        print(f"name:{self.name}, age:{self.age}")

class Teacher(Person):
    def __init__(self, name_pm: str, age_pm: int, subject_pm: str):
        self.name = name_pm
        self.age = age_pm
        self.subject = subject_pm

    def display_teacher_info(self):
        print(f"name:{self.name}, age:{self.age}, subject:{self.subject}")
aibek = Person(name_pm="Айбек", age_pm=25)
teacher = Teacher(name_pm="Marat", age_pm=40, subject_pm="Math")
aibek.display_info()
teacher.display_teacher_info()

