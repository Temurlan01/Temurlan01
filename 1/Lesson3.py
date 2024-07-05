number=int(input("Введите сумму"))
number2=input("Введите имя курса")
dollar_kurs=88
evro_kurs=97
if number2=="доллар":
    result=number//dollar_kurs
    print(result)
elif number2=="евро":
    result2=number//evro_kurs
    print(result2)
else:
    print("Такого курса нет")

