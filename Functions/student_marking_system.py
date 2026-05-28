# welcome msg ----> 1
def welcome():
    print("==========WELCOME TO HOGWARTS MARKING SYSTEM==========")

# total marks ----> 2
def total_marks(mark1,mark2,mark3):
    print(f"Total marks is:{mark1+mark2+mark3}")

#passing  marks  ---> 3
def passing_marks():
    return 33

#average marks ----> 4
def average_marks(mark1,mark2,mark3):
    return (mark1+mark2+mark3)/3

def main():
    welcome()
    maths = int(input("Enter Maths Mark:"))
    science = int(input("Enter science Mark:"))
    chemistry = int(input("Enter chemistry Mark:"))
    total_marks(maths,science,chemistry)
    passing = passing_marks()
    print(f"Passing mark per subject is:{passing}")
    avg = average_marks(maths,science,chemistry)
    print(f"Percentage is {avg}:")

main()

