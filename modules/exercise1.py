"""
Exercise 1: Creating and Using Modules

Instructions:

Create a custom Python module named calculator.py that contains functions 

for basic arithmetic operations (addition, subtraction, multiplication, division).

Create functions add, subtract, multiply, and divide in the calculator.py module.

Import the calculator module into a separate Python script main.py and use its functions 

to perform arithmetic operations on numbers like 5 and 3.

"""

import calculator

sum = calculator.addition(5,4)

product = calculator.multiplication(5,4)

divide = calculator.division(5,4)

subtract = calculator.subtraction(5,4)


print(sum, product, divide, subtract)