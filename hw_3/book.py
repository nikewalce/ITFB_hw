class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'pages': self.pages,
            'genre': self.genre
        }
