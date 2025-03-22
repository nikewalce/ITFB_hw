class User:
    def __init__(self, name, gender, address, age):
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = []

    def assign_books(self, books):
        self.books.extend(books)

    def to_dict(self):
        return {
            'name': self.name,
            'gender': self.gender,
            'address': self.address,
            'age': self.age,
            'books': [book.to_dict() for book in self.books]
        }