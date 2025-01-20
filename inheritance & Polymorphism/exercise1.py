"""
Exercise 1: Single Inheritance Instruction:

Create a base class Shape with a method calculate_area().
Create a subclass Rectangle that inherits from Shape 
and overrides calculate_area() to calculate the area of a rectangle.

"""


class Shape:
    def calculate_area(self):
        return 'Select a shape to calculate area'


class Rectangle(Shape):
    def calculate_area(self, l, w):
        return l * w


shape1 = Shape()
rectangle1 = Rectangle()

print(shape1.calculate_area())

print(rectangle1.calculate_area(5, 5))
