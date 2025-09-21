# update.py
from library import Library

library = Library()
choice = input("1. Update Member Email  2. Update Book Stock: ")

if choice == '1':
    member_id = int(input("Enter member ID: "))
    new_email = input("Enter new email: ")
    library.update_member_email(member_id, new_email)
elif choice == '2':
    book_id = int(input("Enter book ID: "))
    new_stock = int(input("Enter new stock: "))
    library.update_book_stock(book_id, new_stock)
else:
    print("Invalid choice")
