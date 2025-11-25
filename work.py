import math

num1 = int(input("Введите число над которим хотите сделать какую-либо операцию: "))
operator = input("Введите знак для виполнения операции: " )

if operator == "sqrt":
    var = math.sqrt(num1)
else:
    num2 = int(input("Введите второе число: "))
    if operator == "+":
        var = num1 + num2
    elif operator == "-":
        var = num1 - num2
    elif operator == "%":
        var = num1 % num2
    elif operator == "/":
        if num2 != 0:
            var = num1 / num2
        else:
            var = "ошибка деления на ноль"
    elif operator == "*":
        var = num1 * num2
    elif operator == "**":
        var = num1 ** num2
    else:
        var = "неверный оператор"

print(var)




