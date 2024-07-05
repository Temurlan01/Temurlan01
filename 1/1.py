def calculator(x,y,a,):
    if a == "+":
        result= x + y
    elif a == "-":
        result=x - y
    elif a == "*":
        result = x * y
    elif a == "/":
        result = x / y
        return result

total = calculator(10, 5, "+")

print(total)


