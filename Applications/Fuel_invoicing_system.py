from datetime import datetime

def get_fuel_price(fuel_type):
    fuel_price={
        "Petrol":102,
        "Diesel":98,
        "CNG":82
    }
    return fuel_price.get(fuel_type)

def apply_discount(amount):
    current_hour=datetime.now().hour

    if 9 <= current_hour <= 10:
        discount=amount*0.05
    elif 21 <= current_hour <= 22:
        discount=amount*0.03
    else:
        discount=0
    return discount

def calculate_amount(price_per_litre,litres):
    base_amount=price_per_litre*litres
    discount=apply_discount(base_amount)
    final_total_amount=base_amount-discount

    return base_amount,discount,final_total_amount

def print_receipt(fuel_type,price,litres,base_amount,discount,final_total_amount):
    print("==================Petrol Pump Receipt=======================")
    print(f"Fuel Type: {fuel_type}")
    print(f"Price Per Litre: {price}")
    print(f"Litres Filled: {litres}")
    print("-------------------------------------------------------------")
    print(f"Base Amount: {base_amount}")
    print(f"Discount: {discount}")
    print(f"Final Amount: {final_total_amount}")
    print("=============================================================")

def main():
    fuel_type=input("Enter Fuel Type: ")
    litres=int(input("Enter Litres Filled: "))
    price=get_fuel_price(fuel_type)

    if price==0:
        print("Invalid Data")
    else:
        base_amount,discount,final_total_amount=calculate_amount(price,litres)
        print_receipt(fuel_type,price,litres,base_amount,discount,final_total_amount)

main()

