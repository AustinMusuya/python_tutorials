
# OOP

# Class blueprint of the object

# Object is the instance of the class. (instatiation)


# Person Class
# Attributes : name, age, occupation

# method
# speak (saying his/her name)


# destructor
# __del__ (it basically just deletes)


class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Occupation:{self.occupation}"

    def speak(self):
        print(f"Hi my name is {self.name}. Nice to meet you!")

    # Destructor
    def __del__(self):
        print(f"{self.name} says Bye bye")

# Inheritance


class Female(Person):
    pass


# Polymorphism (many forms) (method overriding)
class Male(Person):
    def __init__(self, name, age, build):
        self.name = name
        self.age = age
        self.build = build

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Build: {self.build}"

    def speak(self):
        print(f"Hi my name is {
              self.name}. Nice to meet you! I'm of build, {self.build}")
