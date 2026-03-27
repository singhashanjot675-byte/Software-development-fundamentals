# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


# Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added to library")

    def add_member(self, member):
        self.members.append(member)
        print(member.name, "added as member")

    def borrow_book(self, member, book):
        if book.available == True:
            book.available = False
            member.borrowed_books.append(book)
            print(member.name, "borrowed", book.title)
        else:
            print(book.title, "is not available")

    def return_book(self, member, book):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(member.name, "returned", book.title)
        else:
            print("Book not found in member record")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            if book.available == True:
                status = "Available"
            else:
                status = "Borrowed"
            print(book.title, "by", book.author, "-", status)


# ----------- TESTING ------------

# Create library
library = Library()

# Create books
book1 = Book("Python Basics", "Ashanjot Singh")
book2 = Book("OOP Concepts", "Amrit Singh")

# Add books
library.add_book(book1)
library.add_book(book2)

# Create member
member1 = Member("Anuj")

# Add member
library.add_member(member1)

# Display books
library.display_books()

# Borrow book
library.borrow_book(member1, book1)

# Display again
library.display_books()

# Return book
library.return_book(member1, book1)

# Final display
library.display_books()