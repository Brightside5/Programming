# Define a Book class first (assuming it has title, author, year)
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

# Define a Library class with the following fields:
# (1) name - the name of a library, e.g., Laidlaw Library
# (2) books - a list of Book instances
# When an instance of Library is created, only the name field is required for the __init__ method.
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    # The Library class also has the following methods:
    # (1) add_book(book) - adds a Book instance to the library, i.e., add the Book instance to the books field
    # (2) __str__ - returning the library name and list of books titles in the format 
    #     Library: City Library\nBooks:\n- To Kill a Mockingbird by Harper Lee (1960)\n- 1984 by George Orwell (1949)
    def add_book(self,book):
        self.books.append(book)

    def __str__(self):
        books_str = "\n".join(f"- {book}" for book in self.books)
        return f"Library: {self.name}\nBooks:\n{books_str}"

# When complete, create 3 instances of Books for your 3 most favourite books
# Then, create an instance of Library with your most favourite library in Leeds University
# and add the 3 books to the library. Then, print the library you have created using the print method
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)  # Example favorite

library = Library("Laidlaw Library")  # Example favorite library in Leeds University
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)
