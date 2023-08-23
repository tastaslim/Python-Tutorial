"""
# violation of Single Responsibility

class Book:
    def __init__(self, author):
        self.author = author

    def list_books(self):
        return {
            "author": self.author,
            "books": []
        }

    def get_book(self, book_id):
        print(book_id)
        return {
            "author": self.author,
            "book": []
        }

    def delete_book(self, book_id):
        print(book_id)
        return {
            "author": self.author,
            "message": "Deleted Book Successfully"
        }

    # violates Single Responsibility Principle as printing/organising book is a different responsibility that
    # showing information of book
    def print_book(self):
        print(f"Book Printing for author {self.author}")
"""


class Book:
    def __init__(self, author):
        self.author = author

    def list_books(self):
        return {
            "author": self.author,
            "books": []
        }

    def get_book(self, book_id):
        print(book_id)
        return {
            "author": self.author,
            "book": []
        }

    def delete_book(self, book_id):
        print(book_id)
        return {
            "author": self.author,
            "message": "Deleted Book Successfully"
        }


class BookInformation:
    def __init__(self, book_id):
        self.book_id = book_id

    def print_book(self):
        print(f"Book Printing for author {self.book_id}")
