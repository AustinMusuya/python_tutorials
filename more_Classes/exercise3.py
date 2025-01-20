"""
Exercise 3: Class Method for Factory Creation Instruction:

Create a class Person with attributes name and age.
Implement a class method create_child() to create a new instance representing a child with age set to 0.

"""


class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return f"This is {self.name} of {self.age} years old"

    @classmethod
    def create_child(cls):
        return cls(name="Child", age=0)


boy = Person("Jung", 25)

print(boy)


print(Person.create_child())
