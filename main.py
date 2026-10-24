from books import show_book, save_books, load_books
import os
from dotenv import load_dotenv
load_dotenv()


name = input("hi may i know your name pls: ")
print("hello welcome in", name)


admin_mode = input("would you like to enter admin mode? yes/no: ")
if admin_mode == "yes":
    asking = input("pls enter the admin password: ")
    if asking == os.getenv("password"):
        print("welcome to admin mode", name)
    else:
        print("oops", name, "wrong password")
else:
    print("oh ok")

amount = int(input("how many books do you want?: "))
book = load_books()


for i in range (amount):
    how_many_books = input("enter the book you want: ")
    book.append(how_many_books)
show_book(book) 
save_books(book)


