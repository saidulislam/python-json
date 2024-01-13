import json
import os

books_file = "books.json"

# Initialize an empty json file
def initialize_file():
    if os.path.exists(books_file) == False:
        with open(books_file, "w") as file:
            json.dump([], file)

# Reading from a json file
def read_json(filename: str):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

# Write to json file
def write_json(data, filename: str):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        
def get_all_books():
    return read_json(books_file)

def insert_book(name, author):
    books = get_all_books()
    books.append({"name": name, "author": author, "read": False})
    write_json(books, books_file)
    
def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    write_json(books, books_file)
    
def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    write_json(books, books_file)