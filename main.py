import os

# Global Variables
products = [
    {"id": 1, "name": "Product 1", "price": 10.99, "category": "Category 1"},
    {"id": 2, "name": "Product 2", "price": 15.99, "category": "Category 1"},
    {"id": 3, "name": "Product 3", "price": 5.99, "category": "Category 2"},
    {"id": 4, "name": "Product 4", "price": 7.99, "category": "Category 2"},
    {"id": 5, "name": "Product 5", "price": 12.99, "category": "Category 3"},
]

categories = ["Category 1", "Category 2", "Category 3"]
bills = []
cart_details = []
cart = []
current_user = None
is_admin = False

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_products(category=None):
    clear_screen()
    if category:
        print(f"Products in {category}:")
    else:
        print("Available Products:")
    print("-------------------")
    for product in products:
        if not category or product["category"] == category:
            print(f"{product['id']}. {product['name']} - ${product['price']}")
    print()

def display_cart():
    clear_screen()
    if not cart:
        print("Your cart is empty.")
    else:
        total = 0
        print("Your cart:")
        print("-----------")
        for item in cart:
            product = get_product_by_id(item["product_id"])
            total += product["price"] * item["quantity"]
            print(f"{product['name']} x{item['quantity']} - ${product['price'] * item['quantity']}")
        print("----------------------")
        print(f"Total: ${total}")
    print()

def get_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def login():
    global current_user, is_admin
    clear_screen()
    print("Login")
    print("-----")
    username = input("Username: ")
    password = input("Password: ")
    # Your authentication logic goes here
    current_user = {"username": username}
    is_admin = True  # Set is_admin to True for demonstration purposes
    print(f"Welcome, {username}!")
    input("Press Enter to continue...")

def add_category():
    if not is_admin:
        print("You are not authorized to perform this action.")
        input("Press Enter to continue...")
        return
    clear_screen()
    print("Add Category")
    print("------------")
    category_name = input("Enter the category name: ")
    categories.append(category_name)
    print("Category added successfully!")
    input("Press Enter to continue...")

def add_product():
    if not is_admin:
        print("You are not authorized to perform this action.")
        input("Press Enter to continue...")
        return
    clear_screen()
    print("Add Product")
    print("-----------")
    product_name = input("Enter the product name: ")
    product_price = float(input("Enter the product price: "))
    product_category = input("Enter the product category: ")
    product_id = len(products) + 1
    products.append({"id": product_id, "name": product_name, "price": product_price, "category": product_category})
    print("Product added successfully!")
    input("Press Enter to continue...")


def add_to_cart():
    display_categories()
    category = input("Enter the category name (0 to cancel): ")
    if category == "0":
        return
    display_products(category)
    product_id = int(input("Enter the product ID to add to cart (0 to cancel): "))
    if product_id == 0:
        return
    product = get_product_by_id(product_id)
    if product:
        quantity = int(input("Enter the quantity: "))
        cart.append({"product_id": product_id, "quantity": quantity})
        cart_details.append({"product": product, "quantity": quantity})  # Store cart details
        print("Product added to cart.")
    else:
        print("Invalid product ID.")
    input("Press Enter to continue...")

def display_cart_details():
    if not is_admin:
        print("You are not authorized to perform this action.")
        input("Press Enter to continue...")
        return
    clear_screen()
    print("Cart Details")
    print("------------")
    if not cart_details:
        print("No products in the cart.")
    else:
        total = 0
        for item in cart_details:
            product = item["product"]
            quantity = item["quantity"]
            total += product["price"] * quantity
            print(f"Product: {product['name']}")
            print(f"Price: ${product['price']}")
            print(f"Quantity: {quantity}")
            print("--------------------")
        print(f"Total: ${total}")
    input("Press Enter to continue...")

def view_cart():
    display_cart()
    input("Press Enter to continue...")


def display_categories():
    clear_screen()
    print("Available Categories:")
    print("---------------------")
    for category in categories:
        print(category)
    print()
    selected_category = input("Enter the category name (0 to cancel): ")
    if selected_category == "0":
        return
    display_products_by_category(selected_category)
    input("Press Enter to continue...")

def display_product_details(product_id):
    clear_screen()
    product = get_product_by_id(product_id)
    if product:
        print("Product Details:")
        print("----------------")
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']}")
        print(f"Category: {product['category']}")
    else:
        print("Invalid product ID.")
    print()


def display_products_by_category(category):
    clear_screen()
    print(f"Products in {category}:")
    print("----------------------")
    category_products = [product for product in products if product["category"] == category]
    if not category_products:
        print("No products found in this category.")
    else:
        for product in category_products:
            print(f"{product['id']}. {product['name']} - ${product['price']}")
    print()

    product_id = int(input("Enter the product ID to view details (0 to cancel): "))
    if product_id != 0:
        display_product_details(product_id)
    input("Press Enter to continue...")

def calculate_total():
    total = 0
    for item in cart:
        product = get_product_by_id(item["product_id"])
        total += product["price"] * item["quantity"]
    return total
def display_all_bills():
    if not is_admin:
        print("You are not authorized to perform this action.")
        input("Press Enter to continue...")
        return
    clear_screen()
    print("All Bills")
    print("---------")
    if not bills:
        print("No bills found.")
    else:
        for bill in bills:
            print(f"User: {bill['user']}")
            print(f"Total Amount: Rs {bill['total_amount']}")
            print("--------------------")
    input("Press Enter to continue...")


def place_order():
    display_cart()
    confirmation = input("Confirm order (yes/no): ")
    if confirmation.lower() == "yes":
        total = calculate_total()
        if total > 10000:
            total -= 500
        # Your order processing logic goes here
        bill = {"user": current_user["username"], "total_amount": total}
        bills.append(bill)  # Store bill details
        print(f"Order placed successfully! Total amount: Rs {total}")
        global cart
        cart = []
    input("Press Enter to continue...")


def logout():
    global current_user
    current_user = None
    print("Logged out successfully!")
    input("Press Enter to continue...")

def exit_app():
    clear_screen()
    print("Thank you for using the e-commerce app!")
    exit()


def main():
    while True:
        clear_screen()
        print("E-commerce App")
        print("--------------")
        print("1. Login")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. View Products by Category")
        print("5. View Product Details")
        print("6. Place Order")
        if is_admin:
            print("7. Add Category")
            print("8. Add Product")
            print("9. View Cart Details")
            print("10. View All Bills")
            print("11. Logout")
            print("12. Exit")
        else:
            print("7. View Cart")
            print("8. Logout")
            print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            display_categories()
        elif choice == "5":
            display_product_details(int(input("Enter the product ID: ")))
        elif choice == "6":
            place_order()
        elif is_admin and choice == "7":
            add_category()
        elif is_admin and choice == "8":
            add_product()
        elif is_admin and choice == "9":
            display_cart_details()
        elif is_admin and choice == "10":
            display_all_bills()
        elif is_admin and choice == "11":
            logout()
        elif not is_admin and choice == "7":
            view_cart()
        elif not is_admin and choice == "8":
            logout()
        elif not is_admin and choice == "9":
            exit_app()
        elif is_admin and choice == "12":
            exit_app()
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()



