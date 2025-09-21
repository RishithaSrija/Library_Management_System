# read.py
from library import Library

library = Library()
choice = input("1. List all books  2. Search books  3. List members: ")

if choice == '1':
    library.list_books()
elif choice == '2':
    keyword = input("Enter title/author/category to search: ")
    library.search_books(keyword)
elif choice == '3':
    library.list_members()
else:
    print("Invalid choice")
