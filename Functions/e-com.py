product = []
cart = []

def add_product():
    new_product = input("enter product name:")
    product.append(new_product)
    print(new_product,"Added to your collection")

def view_products():
    if product:
        print("Here are your added products")
        for i in product:
            print(i)
    else:
        print("No products added, Please Try to add products")

def add_to_cart():
    cart_product=input("enter product to add to cart:")
    if cart_product in product:
        cart.append(cart_product)
        print(cart_product,"Added to cart")
    else:
        print("Please Select from view products")

def view_cart():
    if cart:
        print("Here are your products in your cart")
        for i in cart:
            print(i)
    else:
        print("No products added, Please Try to add products")

def remove_from_cart():
    remove_name = input("enter product to remove from cart:")
    if remove_name in cart:
        cart.remove(remove_name)
        print(remove_name,"is Removed from cart")
    else:
        print("Please enter a valid product name from your cart")

def main():
    while True:
        print("======WELCOME TO AMAZON======")
        print("1. Add Product")
        print("2. View Product")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Remove from cart")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            add_product()
        elif choice == 2:
            view_products()
        elif choice == 3:
            add_to_cart()
        elif choice == 4:
            view_cart()
        elif choice == 5:
            remove_from_cart()

main()

