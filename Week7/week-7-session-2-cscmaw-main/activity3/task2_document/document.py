# define a base class called Document with the following fields:
# (1) title - the title of the document
# (2) author - the author of the document
# (3) date_created - the creation date of the document
class Document:
    def __init__(self,title,author,date_created):
        self.title = title
        self.author = author
        self.date_created = date_created

# this base class has the following methods:
# (1) view - prints a message indicating that the document is being viewed (e.g., Viewing the document...)
# (2) prints - prints a message indicating the the document is being printed (e.g., Printing the document...)
# (3) __str__ - returns a formatted summary of the document's title, author and date created 
#     e.g., 
#     Document: Monthly Report
#     Monthly Report by John Doe, created on 2023-08-01

    def view(self):
        print("Viewing the document...")

    def prints(self):
        print("Printing the document...")

    def __str__(self):
        return f"Document: {self.title}\n{self.title} by {self.author}, created on {self.date_created}"