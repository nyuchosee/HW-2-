from itertools import cycle

def distribute_books(books, users):
    users_cycle = cycle(users)
    for book in books:
        user = next(users_cycle)
        user.setdefault("books", []).append(book)
    return users