from files import BOOKS_CSV_FILE_PATH
from files import USER_FILE_PATH
from files import RESULT_FILE_PATH
from csv import DictReader
import json
from user import User
from book import Book

class BookDistributor:
    def __init__(self):
        self.users = []
        self.books = []

    def load_data(self):
        """Инициализация объектов пользователей и книг на основе данных из файлов"""
        with open(USER_FILE_PATH, 'r') as file:
            users_data = json.load(file)
        with open(BOOKS_CSV_FILE_PATH, newline='') as file:
            books_data = [row for row in DictReader(file)]

        self.users = [User(user['name'], user['gender'], user['address'], user['age']) for user in users_data]
        self.books = [Book(book['Title'], book['Author'], int(book['Pages']), book['Genre']) for book in books_data]

    def distribute_books(self):
        """раздача книг по принципу "максимально поровну"""
        user_count = len(self.users)
        book_count = len(self.books)

        books_per_user = book_count // user_count
        extra_books = book_count % user_count

        start_index = 0
        for i, user in enumerate(self.users):
            count = books_per_user + (1 if i < extra_books else 0)
            user.assign_books(self.books[start_index:start_index + count])
            start_index += count

    def save_result(self):
        """создаст result.json файл со структурой reference.json"""
        result = [user.to_dict() for user in self.users]

        with open(RESULT_FILE_PATH, 'w') as file:
            json.dump(result, file, indent=4)

    def run(self):
        self.load_data()
        self.distribute_books()
        self.save_result()


if __name__ == '__main__':
    distributor = BookDistributor()
    distributor.run()
