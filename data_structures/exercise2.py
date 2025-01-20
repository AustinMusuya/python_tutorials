"""
Exercise 2: Define a dictionary to store information about your favorite book,
including title, author, and genre. Use the method to retrieve the genre.

"""

favourite_book = {
    "title" : "Stranger in The Mirror",
    "author" : "Sydney Sheldon",
    "genre" : "Drama"
                  }

# print(favourite_book.keys())
# print(favourite_book.values())

print(favourite_book.get('genre', 'Hskell'))

