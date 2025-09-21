import sys
import os

while True:
    print("\n===== Library Management System =====")
    print("1. Create (Insert) -> Register new members / Add new books")
    print("2. Read (Select)   -> List/Search/Show members & borrowed books")
    print("3. Update          -> Update book stock / Update member info")
    print("4. Delete          -> Delete member / Delete book")
    print("5. Book            -> Borrow book / Return book")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        os.system("python insert.py")
    elif ch == '2':
        os.system("python read.py")
    elif ch == '3':
        os.system("python update.py")
    elif ch == '4':
        os.system("python delete.py")
    elif ch=='5':
        os.system("python book_borrow_return.py")
    elif ch == '6':
        print("Exiting Library Management System!")
        sys.exit(0)
    else:
        print("Invalid choice. Try again.")
