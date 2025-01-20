"""
Exercise 2: Magic Methods (str and repr) Instructions:

Create a Book class with attributes like title, author, and pages.
Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.

"""


class Book:
    title = 'Harry Potter And The Chamber of Secrets'
    author = "J.K Rowling"
    pages = 2068

    def __str__(self) -> str:
        return f"The Book '{self.title}' by '{self.author}', has  {self.pages} pages"

    def __repr__(self) -> str:
        return f"Book Title: {self.title}, Book Author: {self.author}, Book Page-count: {self.pages}"


book1 = Book()


print(repr(book1))
print()
print(book1)


# print(repr(book1))
# print()
# print(book1)
