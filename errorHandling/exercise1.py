number1 = int(input("Enter First Number: "))

number2 = int(input("Enter Second Number: "))


# result = division()


try:
    number1 / number2
except ZeroDivisionError as e:
    print("Division by zero not possible")
