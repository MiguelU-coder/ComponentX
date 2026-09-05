from sequential.products import create_product, read_products, update_product, delete_product
from sequential.users import create_user, read_users, update_user, delete_user
from sequential.clients import create_client, read_clients, update_client, delete_client
from sequential.orders import create_order, read_orders, update_order, delete_order
from sequential.shops import create_shop, read_shops, update_shop, delete_shop

from direct.products import create_product_direct, read_products_direct, update_product_direct, delete_product_direct
from direct.users import create_user_direct, read_users_direct, update_user_direct, delete_user_direct
from direct.clients import create_client_direct, read_clients_direct, update_client_direct, delete_client_direct
from direct.orders import create_order_direct, read_orders_direct, update_order_direct, delete_order_direct
from direct.shops import create_shop_direct, read_shops_direct, update_shop_direct, delete_shop_direct


def select_mode():
    while True:
        print("\n===== ACCESS MODE =====")
        print("1. Sequential access")
        print("2. Direct access")
        print("0. Exit")

        option = input("Select an option: ")

        match option:
            case "1":
                return "sequential"
            case "2":
                return "direct"
            case "0":
                return None
            case _:
                print("Invalid Option")

def menu_clients(mode):
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
                if mode == "direct":
                    create_client_direct(id, name, mail, shop_id)
                else:
                    create_client(id, name, mail, shop_id)

            case "2":
                if mode == "direct":
                    read_clients_direct()
                else:
                    read_clients()

            case "3":
                id_searched = int(input("Enter the client's ID to update: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                shop_id = int(input("Enter the shop's ID: "))
                if mode == "direct":
                    update_client_direct(id_searched, name, mail, shop_id)
                else:
                    update_client(id_searched, name, mail, shop_id)

            case "4":
                id_searched = int(input("Enter the client's ID to delete: "))
                if mode == "direct":
                    delete_client_direct(id_searched)
                else:
                    delete_client(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_products(mode):
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
                if mode == "direct":
                    create_product_direct(id, name, category, stock, price, shop_id, description)
                else:
                    create_product(id, name, category, stock, price, shop_id, description)

            case "2":
                if mode == "direct":
                    read_products_direct()
                else:
                    read_products()

            case "3":
                id_searched = int(input("Enter the product's ID to update: "))
                name = input("Enter the name: ")
                category = input("Enter the category: ")
                stock = int(input("Enter the stock: "))
                price = float(input("Enter the price: "))
                shop_id = int(input("Enter the shop's ID: "))
                description = input("Enter the description: ")
                if mode == "direct":
                    update_product_direct(id_searched, name, category, stock, price, shop_id, description)
                else:
                    update_product(id_searched, name, category, stock, price, shop_id, description)

            case "4":
                id_searched = int(input("Enter the product's ID to delete: "))
                if mode == "direct":
                    delete_product_direct(id_searched)
                else:
                    delete_product(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_users(mode):
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
                mail = input("Enter the mail: ")
                rol = input("Enter the rol: ")
                shop_id = int(input("Enter the shop's ID: "))
                if mode == "direct":
                    create_user_direct(id, name, mail, rol, shop_id)
                else:
                    create_user(id, name, mail, rol, shop_id)

            case "2":
                if mode == "direct":
                    read_users_direct()
                else:
                    read_users()

            case "3":
                id_searched = int(input("Enter the user's ID to update: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                rol = input("Enter the rol: ")
                shop_id = int(input("Enter the shop's ID: "))
                if mode == "direct":
                    update_user_direct(id_searched, name, mail, rol, shop_id)
                else:
                    update_user(id_searched, name, mail, rol, shop_id)

            case "4":
                id_searched = int(input("Enter the user's ID to delete: "))
                if mode == "direct":
                    delete_user_direct(id_searched)
                else:
                    delete_user(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_orders(mode):
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
                if mode == "direct":
                    create_order_direct(id, client_id, shop_id, date, total, status, product_id)
                else:
                    create_order(id, client_id, shop_id, date, total, status, product_id)

            case "2":
                if mode == "direct":
                    read_orders_direct()
                else:
                    read_orders()

            case "3":
                id_searched = int(input("Enter the order's ID to update: "))
                client_id = int(input("Enter the client's ID: "))
                shop_id = int(input("Enter the shop's ID: "))
                date = input("Enter the date: ")
                total = float(input("Enter the total: "))
                status = input("Enter the status: ")
                product_id = int(input("Enter the product's ID: "))
                if mode == "direct":
                    update_order_direct(id_searched, client_id, shop_id, date, total, status, product_id)
                else:
                    update_order(id_searched, client_id, shop_id, date, total, status, product_id)

            case "4":
                id_searched = int(input("Enter the order's ID to delete: "))
                if mode == "direct":
                    delete_order_direct(id_searched)
                else:
                    delete_order(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_shops(mode):
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
                if mode == "direct":
                    create_shop_direct(id, name, description, admin_user_id)
                else:
                    create_shop(id, name, description, admin_user_id)

            case "2":
                if mode == "direct":
                    read_shops_direct()
                else:
                    read_shops()

            case "3":
                id_searched = int(input("Enter the shop's ID to update: "))
                name = input("Enter the name: ")
                description = input("Enter the description: ")
                admin_user_id = int(input("Enter the admin user's ID: "))
                if mode == "direct":
                    update_shop_direct(id_searched, name, description, admin_user_id)
                else:
                    update_shop(id_searched, name, description, admin_user_id)

            case "4":
                id_searched = int(input("Enter the shop's ID to delete: "))
                if mode == "direct":
                    delete_shop_direct(id_searched)
                else:
                    delete_shop(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def main():
    mode = select_mode()
    if mode is None:
        return

    while True:
        print(f"\n===== MAIN MENU ({mode.upper()} ACCESS) =====")
        print("1. Clients")
        print("2. Products")
        print("3. Users")
        print("4. Orders")
        print("5. Shops")
        print("6. Change access mode")
        print("0. Exit")

        option = input("Select an option: ")

        match option:
            case "1":
                menu_clients(mode)
            case "2":
                menu_products(mode)
            case "3":
                menu_users(mode)
            case "4":
                menu_orders(mode)
            case "5":
                menu_shops(mode)
            case "6":
                mode = select_mode()
                if mode is None:
                    return
            case "0":
                break
            case _:
                print("Invalid Option")


if __name__ == "__main__":
    main()
