class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
