import os.path

FILES_DIR = os.path.dirname(__file__)

def get_path(filename: str) -> str:
    return os.path.join(FILES_DIR, filename)

REFERENCE_FILE_PATH = get_path(filename = 'reference.json')
BOOKS_CSV_FILE_PATH = get_path(filename = 'books.csv')
USER_FILE_PATH = get_path(filename = 'user.json')
RESULT_FILE_PATH = get_path(filename = 'result.json')