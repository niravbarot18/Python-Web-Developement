import random
from datetime import datetime

def place_order():
    order_id=random.randint(1000,9999)
    token_no=random.randint(1,5)

    customer=input("Enter Customer Name:")
    food=input("Enter Food Item Name:")
    quantity=int(input("Enter Quantity:"))
    address=input("Enter Address:")
    order_time=datetime.now()

    data=f"""
    ORDER ID:{order_id}
    CUSTOMER:{customer}
    FOOD ITEM:{food}
    QUANTITY:{quantity}
    ADDRESS:{address}
    TOKEN NO:{token_no}
    ORDER TIME:{order_time}"""

    file = open("zomato_order.txt","a")
    file.write(data)
    file.close()

    print("Order placed successfully")
    print(f"Order ID:{order_id}")
    print(f"Token No:{token_no}")

def view_order():
    file=open("zomato_order.txt","r")
    data=file.read()
    file.close()

    print("="*40)
    print(data)

def search_order():
    customer=input("Enter Customer Name:")
    file=open("zomato_order.txt","r")
    data=file.read()
    file.close()

    if customer.lower() in data.lower():
        print("Order found")
    else:
        print("Order not found")

def main():
    while True:
        print("==========Zomato==========")
        print("1. Place Order")
        print("2. View Order")
        print("3. Search Order")
        print("4. Exit")

        choice=int(input("Enter your choice: "))

        if choice==1:
            place_order()

        if choice==2:
            view_order()

        if choice==3:
            search_order()

        if choice==4:
            print("Thank You for using Zomato")
            break
main()
