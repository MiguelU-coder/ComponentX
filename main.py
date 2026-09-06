from crud_products import create_product, read_products, update_product, delete_product
from crud_user import create_user, read_users, update_user, delete_user
from crud_client import create_client, read_clients, update_client, delete_client
from crud_order import create_order, read_orders, update_order, delete_order
from crud_shop import create_shop, read_shops, update_shop, delete_shop

def menu_clients():
    while True:
        print("\n===== CLIENTS =====")
        print("1. Create client")
        print("2. Read clients")
        print("3. Update client")
        print("4. Delete client")
        print("0. Back")

        option = input("Select an option: ")

        match option:

            case "1":
                id = int(input("Enter the client's ID: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                shop_id = int(input("Enter the shop's ID: "))
                create_client(id, name, mail, shop_id)

            case "2":
                read_clients()

            case "3":
                id_searched = int(input("Enter the client's ID to update: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                shop_id = int(input("Enter the shop's ID: "))
                update_client(id_searched, name, mail, shop_id)

            case "4":
                id_searched = int(input("Enter the client's ID to delete: "))
                delete_client(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")
def menu_products():
    while True:
        print("\n===== PRODUCTS =====")
        print("1. Create product")
        print("2. Read products")
        print("3. Update product")
        print("4. Delete product")
        print("0. Back")

        option = input("Select an option: ")

        match option:

            case "1":
                id = int(input("Enter the product's ID: "))
                name = input("Enter the name: ")
                category = input("Enter the category: ")
                stock = int(input("Enter the stock: "))
                price = float(input("Enter the price: "))
                shop_id = int(input("Enter the shop's ID: "))
                description = input("Enter the description: ")
                create_product(id, name, category, stock, price, shop_id, description)

            case "2":
                read_products()

            case "3":
                id_searched = int(input("Enter the product's ID to update: "))
                name = input("Enter the name: ")
                category = input("Enter the category: ")
                stock = int(input("Enter the stock: "))
                price = float(input("Enter the price: "))
                shop_id = int(input("Enter the shop's ID: "))
                description = input("Enter the description: ")
                update_product(id_searched, name, category, stock, price, shop_id, description)

            case "4":
                id_searched = int(input("Enter the product's ID to delete: "))
                delete_product(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")
def menu_users():
    while True:
        print("\n===== USERS =====")
        print("1. Create user")
        print("2. Read users")
        print("3. Update user")
        print("4. Delete user")
        print("0. Back")

        option = input("Select an option: ")

        match option:

            case "1":
                id = int(input("Enter the user's ID: "))
                name = input("Enter the name: ")
                email = input("Enter the email: ")
                password = input("Enter the password: ")
                shop_id = int(input("Enter the shop's ID: "))
                create_user(id, name, email, password, shop_id)

            case "2":
                read_users()

            case "3":
                id_searched = int(input("Enter the user's ID to update: "))
                name = input("Enter the name: ")
                email = input("Enter the email: ")
                password = input("Enter the password: ")
                shop_id = int(input("Enter the shop's ID: "))
                update_user(id_searched, name, email, password, shop_id)

            case "4":
                id_searched = int(input("Enter the user's ID to delete: "))
                delete_user(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")
def menu_orders():
    while True:
        print("\n===== ORDERS =====")
        print("1. Create order")
        print("2. Read orders")
        print("3. Update order")
        print("4. Delete order")
        print("0. Back")

        option = input("Select an option: ")

        match option:

            case "1":
                id = int(input("Enter the order's ID: "))
                client_id = int(input("Enter the client's ID: "))
                shop_id = int(input("Enter the shop's ID: "))
                date = input("Enter the date: ")
                total = float(input("Enter the total: "))
                status = input("Enter the status: ")
                product_id = int(input("Enter the product's ID: "))
                create_order(id, client_id, shop_id, date, total, status, product_id)

            case "2":
                read_orders()

            case "3":
                id_searched = int(input("Enter the order's ID to update: "))
                client_id = int(input("Enter the client's ID: "))
                shop_id = int(input("Enter the shop's ID: "))
                date = input("Enter the date: ")
                total = float(input("Enter the total: "))
                status = input("Enter the status: ")
                product_id = int(input("Enter the product's ID: "))
                update_order(id_searched, client_id, shop_id, date, total, status, product_id)

            case "4":
                id_searched = int(input("Enter the order's ID to delete: "))
                delete_order(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")
def menu_shops():
    while True:
        print("\n===== SHOPS =====")
        print("1. Create shop")
        print("2. Read shops")
        print("3. Update shop")
        print("4. Delete shop")
        print("0. Back")

        option = input("Select an option: ")

        match option:

            case "1":
                id = int(input("Enter the shop's ID: "))
                name = input("Enter the name: ")
                description = input("Enter the description: ")
                admin_user_id = int(input("Enter the admin user's ID: "))
                create_shop(id, name, description, admin_user_id)

            case "2":
                read_shops()

            case "3":
                id_searched = int(input("Enter the shop's ID to update: "))
                name = input("Enter the name: ")
                address = input("Enter the address: ")
                update_shop(id_searched, name, address)

            case "4":
                id_searched = int(input("Enter the shop's ID to delete: "))
                delete_shop(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")

def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Clients")
        print("2. Products")
        print("3. Users")
        print("4. Orders")
        print("5. Shops")
        print("0. Exit")

        option = input("Select an option: ")

        match option:

            case "1":
                menu_clients()

            case "2":
                menu_products()

            case "3":
                menu_users()

            case "4":
                menu_orders()

            case "5":
                menu_shops()

            case "0":
                break

            case _:
                print("Invalid Option")

if __name__ == "__main__":
    main()