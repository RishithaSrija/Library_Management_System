# delete.py
from library import Library

library = Library()
choice = input("1. Delete Member  2. Delete Book: ")

if choice == '1':
    member_id = int(input("Enter member ID to delete: "))
    library.delete_member(member_id)
elif choice == '2':
    book_id = int(input("Enter book ID to delete: "))
    library.delete_book(book_id)
else:
    print("Invalid choice")
