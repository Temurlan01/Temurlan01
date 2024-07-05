#3. Создайте класс MBankAccount, который включает атрибуты account_number и balance (с приватным доступом).
#Реализуйте методы для депозита (deposit), снятия средств (withdraw) и отображения баланса (get_balance). Убедитесь, что баланс не может стать отрицательным.
class MBankAccount:
    def __init__(self, account_number_pm: int, balance_pm: int,):
        self.__account_number = account_number_pm
        self.__balance = balance_pm

    def deposit_withdraw(self, sum_withdraw):
        if self.__balance > 0:
            sum = self.__balance - sum_withdraw
            print(sum)
        if self.__balance < 0:
            print("На вашем балансе недостаточно денег")

    def get_balance(self):

        return self.__balance


deposit = MBankAccount(account_number_pm=346124987193898, balance_pm=2000)

deposit.deposit_withdraw(3000)
deposit.get_balance()
