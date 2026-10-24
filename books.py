import json
def show_book(book):
    for books in book:
        print(f"your book will be {books}")
def save_books(books):
    with open ("books.json", "w", encoding ="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)

def load_books():
    try:
        with open("books.json", "r", encoding ="utf-8") as file: 
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return[]