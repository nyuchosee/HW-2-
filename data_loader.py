import csv
import json

def load_books(filename):
    books = []
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            books.append(row)
    return books

def load_users(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

def save_result(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)