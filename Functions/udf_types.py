#1. NO ARGUMENT AND NO RETURN TYPE -- > 0 , 0
def welcome_msg():
    print("Welcome to InfoLabz")
welcome_msg()

# 2. ARGUMENT WITH NO RETURN TYPE -- > 1, 0
def square(num):
    print(f"square of {num} is {num**2}")
square(10)

# 3. NO ARGUMENT WITH RETURN TYPE -- > 0,1
def fixed_salary():
    return 50000,80000
salary = fixed_salary()
print(f"fixed salary is {salary}")

# 4. ARGUMENT WITH RETURN TYPE -- > 1, 1
def division(a,b):
    return a/b

no1=int(input("enter no1:"))
no2=int(input("enter no2:"))

div=division(no1,no2)
print("Division is:",div)