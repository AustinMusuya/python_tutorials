"""
Exercise 3: Class Inheritance Instructions:

Create a base class Animal with methods like eat and sleep.
Create a subclass Dog that inherits from Animal and adds a method bark.
Create instances of both classes and demonstrate method inheritance.

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal):
    pass


animal1 = Animal("Monkey")

dog1 = Dog("Luffy")

print(animal1.eat())
print(animal1.sleep())
print(dog1.eat())
print(dog1.sleep())
