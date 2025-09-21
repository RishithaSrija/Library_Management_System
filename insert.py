# insert.py
from library import Library

library = Library()

choice = input("1. Add Member  2. Add Book: ")
if choice == '1':
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    library.add_member(name, email)
elif choice == '2':
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter category: ")
    stock = int(input("Enter stock quantity: "))
    library.add_book(title, author, category, stock)
else:
    print("Invalid choice")
