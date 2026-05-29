import os
FILE_NAME = "Employee.txt"

def add_employee():
    emp_id=input("Enter Employee ID:")
    name = input("Enter Employee Name:")
    department = input("Enter Employee Department Name:")
    salary=float(input("Enter Employee Salary:"))

    with open(FILE_NAME,"a") as file:
        file.write(f"{emp_id},{name},{department},{salary}\n")

    print("Employee Added Successfully")

def view_employee():
    if not os.path.exists(FILE_NAME):
        print("No File Record Found")
        return

    with open(FILE_NAME,"r") as file:
        data=file.readlines()

    if not data:
        print("No Employee Records Found")
        return

    print("================Employee Record==============")
    for i in data:
        emp = i.strip().split(",")

        if len(emp)<4:
            continue

        print(f"Employee ID: {emp[0]}")
        print(f"Employee Name: {emp[1]}")
        print(f"Employee Department: {emp[2]}")
        print(f"Employee Salary: {emp[3]}")
        print("-"*40)

def search_employee():
    emp_id=input("Enter Employee ID to search:")

    found = False

    if not os.path.exists(FILE_NAME):
        print("No File Record Found")
        return

    with open(FILE_NAME,"r") as file:
        for i in file:
            emp = i.strip().split(",")
            if emp[0] == emp_id:
                found = True
                print("Employee Found")
                print(f"Employee ID: {emp[0]}")
                print(f"Employee Name: {emp[1]}")
                print(f"Employee Department: {emp[2]}")
                print(f"Employee Salary: {emp[3]}")

    if not found:
        print("Employee Not Found")

def  delete_employee():
    emp_id=input("Enter Employee ID to delete:")

    if not os.path.exists(FILE_NAME):
        print("No File Record Found")
        return

    new_data=[]
    found = False

    with open(FILE_NAME,"r") as file:
        for i in file:
            emp=i.strip().split(",")
            if emp[0] == emp_id:
                found = True
            else:
                new_data.append(i)

    if found:
        with open(FILE_NAME,"w") as file:
            file.writelines(new_data)
        print("Employee Removed Successfully")
    else:
        print("No Employee matched of this ID")


def main():
    while True:
        print("==========BMW Employee Tracking===========")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice=int(input("Enter your choice:"))

        if choice==1:
            add_employee()
        elif choice==2:
            view_employee()
        elif choice==3:
            search_employee()
        elif choice==4:
            delete_employee()
        elif choice==5:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

main()