import os
FILE_NAME="books.txt"

def add_book():
    book_id=input("Enter Book ID to add:")
    book_title=input("Enter Book Title to add:")
    book_author=input("Enter Book Author to add:")

    with open(FILE_NAME,"a") as file:
        file.write(f"{book_id},{book_title},{book_author}\n")

    print("Book Added Successfully")

def view_book():
    if not os.path.exists(FILE_NAME):
        print("No Record Found")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No Book Content Found")
        return

    print("========Book Record========")
    for i in data:
        book=i.strip().split(",")

        print(f"Book ID:{book[0]}")
        print(f"Book Title:{book[1]}")
        print(f"Book Author:{book[2]}")
        print("-"*40)

def update_book():
    book_id=input("Enter Book ID to update:")

    if not os.path.exists(FILE_NAME):
        print("No Book Record Found")
        return

    new_data1=[]
    found=False

    with open(FILE_NAME,"r") as file:
        for i in file:
            book=i.strip().split(",")
            if book[0]==book_id:
                found=True

                new_title=input("Enter New Book Title to update:")
                new_author=input("Enter New Book Author to update:")

                new_data1.append(f"{book_id},{new_title},{new_author}\n")

            else:
                new_data1.append(i)

    if found:
        with open(FILE_NAME,"w") as file:
            file.writelines(new_data1)

        print("Book Updated Successfully")

    else:
        print("No Book Record matched with this ID")


def search_book():
    book_id=input("Enter Book ID to search:")

    found=False

    if not os.path.exists(FILE_NAME):
        print("No Record Found")
        return

    with open(FILE_NAME,"r") as file:
        for i in file:
            book=i.strip().split(",")
            if  book[0]==book_id:
                found=True
                print("Book Found")
                print(f"Book ID:{book[0]}")
                print(f"Book Title:{book[1]}")
                print(f"Book Author:{book[2]}")

    if not found:
        print("No Book Record Found. Please Enter the valid Book ID")

def remove_book():
    book_id=input("Enter Book ID to remove:")

    if not os.path.exists(FILE_NAME):
        print("No Book Record Found")
        return

    new_data=[]
    found=False

    with open(FILE_NAME,"r") as file:
        for i in file:
            book=i.strip().split(",")
            if book[0]==book_id:
                found=True
            else:
                new_data.append(i)

    if found:
        with open(FILE_NAME,"w") as file:
            file.writelines(new_data)
            print("Book Removed Successfully")
    else:
        print("No Book Records Matched with this ID")


def main():
    while True:
        print("========Library Management System========")
        print("1. Add Book")
        print("2. View Book")
        print("3. Update Book")
        print("4. Search Book")
        print("5. Remove Book")
        print("6. Exit")

        choice=int(input("Enter Your Choice:"))

        if choice==1:
            add_book()
        elif choice==2:
            view_book()
        elif choice==3:
            update_book()
        elif choice==4:
            search_book()
        elif choice==5:
            remove_book()
        elif choice==6:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

main()