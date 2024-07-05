
class Person:
    def __init__(self, name_pm:str, langueg_pm:str):
        self.name = name_pm
        self.langueg = langueg_pm
    def itroduse(self, ):
        if self.langueg == "ru":
            print(f"Здраствуйте меня зовут {self.name}")
        elif self.langueg == "kg":
            print(f"Cаламатсызбы менин атым {self.name}")
        else:
            print(f"Helo my name is {self.name}")

class BankAccount(Person):
    def __init__(self, name_pm: str, langueg_pm: str, account_number_pm: int, balance_pm: int):
        self.name = name_pm
        self.langueg = langueg_pm
        self.account_namber = account_number_pm
        self.__balance = balance_pm

    def depozit(self, set_balance):
        if self.__balance > 0:
            self.__balance = self.__balance + set_balance
            return self.__balance

    def withdraw(self, get_balance):
        if self.__balance > 0:
            self.__balance = self.__balance - get_balance
            return self.__balance

worker = Person(name_pm="Бека", langueg_pm="ru")
bankAccount = BankAccount("Бека", "ru",2637324239824, 1000)
worker.itroduse()

print(bankAccount.depozit(10000))
print(bankAccount.withdraw(10))