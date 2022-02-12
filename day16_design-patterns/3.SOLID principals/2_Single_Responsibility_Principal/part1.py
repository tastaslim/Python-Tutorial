class Book:
    def __init__(self, name):
        self.book = name

    @staticmethod
    def list_books():
        return [{}, {}]

    @staticmethod
    def create_book(name):
        return f"Book created: {name}"


class SaveInformation:
    @staticmethod
    def save_book(name):
        print(f"Book saved: ${name}")
