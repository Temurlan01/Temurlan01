from function import (calculate_sum,calculate_difference,
                      calculate_product,calculate_div)


chislo1=int(input("ведите первое число:"))
chislo2=int(input("ведите второе число:"))

operator= input("Введите оператора")

if operator=="+":
    summa=calculate_sum(chislo1, chislo2)
    print(summa)
elif operator=="-":
    summa2=calculate_difference(chislo1, chislo2)
    print(summa2)
elif operator=="*":
    summa3=calculate_product(chislo1, chislo2)
    print(summa3)
elif operator=="/":

    summa4=calculate_div(chislo1,chislo2)
    print(summa4)

