"""
Exercise 2: Static Method for Utility Calculation Instruction:

Create a class Calculator with static methods for basic mathematical operations like addition and multiplication.
Implement static methods add() and multiply() to perform these operations.

"""

# Decorators
# gives a function more functionality


class Calculator:

    count = 0

    @staticmethod
    def add(x, y):
        print(x + y)

    @classmethod
    def multiply(cls, x, y):
        cls.count += 1
        print(x * y)


# Calculator.add(5, 4)

Calculator.multiply(5, 4)
Calculator.multiply(5, 4)
Calculator.multiply(5, 4)
Calculator.multiply(5, 4)
Calculator.multiply(5, 4)

print(Calculator.count)
