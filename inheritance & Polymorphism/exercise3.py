"""
Exercise 3: Polymorphism with Duck Typing Instruction:

Create classes Dog, Cat, and Bird, each with a method make_sound().
Implement different behaviors for make_sound() in each class.
Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.


"""


class Dog:
    def make_sound(self):
        return "barking..."


class Cat:
    def make_sound(self):
        return 'meowing...'


class Bird:
    def make_sound(self):
        return 'chirping...'


def let_them_speak(animals):
    sounds = []
    for animal in animals:
        sounds.append(animal.make_sound())
    return sounds


animals = let_them_speak([Dog(), Cat(), Bird()])

print(type(animals))

for i in animals:
    print(i)
