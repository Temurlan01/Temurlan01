class Student:
    def __init__(self, name_pm: str, age_pm: int):
        self.name = name_pm
        self.age = age_pm

    def say_here(self):
        print(f"меня зовут {self.name} я здесь")

    def ask_qusetion(self, question: str):
        print(f" меня вопрос:{question}")

nur = Student(name_pm="Нуржигит", age_pm=20)
asan = Student(name_pm="Асан", age_pm=30)

nur.say_here()
asan.say_here()

nur.ask_qusetion("Что такое float")
asan.ask_qusetion("Что такое oon")


