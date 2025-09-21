
from library import Library

library = Library()  
print("Book Borrow / Return System")
print("1. Borrow Book")
print("2. Return Book")
choice = input("Enter your choice: ")

if choice == '1':
    member_id = int(input("Enter Member ID: "))
    book_id = int(input("Enter Book ID to borrow: "))
    library.borrow_book(member_id, book_id)
elif choice == '2':
    member_id = int(input("Enter Member ID: "))
    book_id = int(input("Enter Book ID to return: "))
    library.return_book(member_id, book_id)
else:
    print("Invalid choice.")
