from data_loader import load_books, load_users, save_result
from book_distributor import distribute_books

BOOKS_FILE = "books.csv"
USERS_FILE = "user.json"
RESULT_FILE = "result.json"

books = load_books(BOOKS_FILE)
users = load_users(USERS_FILE)
distributed_users = distribute_books(books, users)
save_result(distributed_users, RESULT_FILE)

print(f"Книги успешно распределены! Результат сохранён в {RESULT_FILE}")