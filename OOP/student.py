class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_information(self):
        return f"This is student {self.name} who is {self.age} years old"

    def __str__(self) -> str:
        return f"Student Name: {self.name} Student age: {self.age}"


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value_of_products(self):
        total = self.price * self.quantity
        return total

    def __str__(self) -> str:
        return f"Product name: {self.name}\nProduct price: ${self.price:.2f}\nProduct quantity: {self.quantity:.2f}"


product1 = Product("Apple", 15, 10)

value = product1.total_value_of_products()

print(value)
print(product1)
