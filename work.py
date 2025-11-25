import math

num1 = int(input("Enter the number on which you want to perform some operation: "))
operator = input("Enter a character to perform the operation: " )

if operator == "sqrt":
    var = math.sqrt(num1)
else:
    num2 = int(input("Enter the second number: "))
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
            var = "division by zero error"
    elif operator == "*":
        var = num1 * num2
    elif operator == "**":
        var = num1 ** num2
    else:
        var = "invalid operator"

print("Your answer:", var)



