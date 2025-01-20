"""
Exercise 1: Constructors and Destructors Instructions:

Create a Person class with attributes like name and age. 

Implement a constructor (__init__) to initialize these attributes.

Also, implement a destructor (__del__) method to print a farewell message when an object is deleted.

"""
import time


class Person:
    def __init__(self, name,  age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person name: {self.name}, Person age: {self.age}"

    def __del__(self):
        print("object is being deleted")
        print(f"Farwell {self.name}.")


person1 = Person("Justin", 25)

print(person1)
