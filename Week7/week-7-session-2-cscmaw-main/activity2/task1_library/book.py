class Book:
    def __init__(self, title, author, year, edition):
        self.title = title
        self.author = author
        self.year = year
        self.edition = edition

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Year must be a positive integer")
        self._year = value

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.edition} edition"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.edition}')"


