"""
Exercise 2: Multiple Inheritance Instruction:

Create two parent classes Bird and Mammal with methods fly() and run(), respectively.
Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods

"""


class Bird:
    def fly(cls):
        return "Bird is flying"


class Mammal:
    def run(cls):
        return "Mammal is running"


class Bat(Mammal, Bird):
    pass
