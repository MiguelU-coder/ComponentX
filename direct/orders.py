# Crud creation for 'ComponentX' direct access operations
# This crud will help with the Orders organizations and inventory

# 'os' is used to check whether the data files already exist
# before creating them (files are only created when an action runs).
import os

## Function for building a length order register
## @params: active, id, client_id, shop_id, date, total, status, product_id
## @return: length order register
def build_order(active, id, client_id, shop_id, date, total, status, product_id):
    return (
        str(active).ljust(1) +
        str(id).zfill(4) +
        str(client_id).zfill(4) +
        str(shop_id).zfill(4) +
        str(date)[:10].ljust(10) +
        str(total).zfill(10) +
        str(status)[:15].ljust(15) +
        str(product_id).zfill(4) +
        "\n"
    )

# Width of each field in the register (in bytes):
# active = 1
# id = 4
# client_id = 4
# shop_id = 4
# date = 10
# total = 10
# status = 15
# product_id = 4
# newline = 1
# Total length of a register: 1+4+4+4+10+10+15+4+1 = 53.

ORDER_REGISTER_LEN = 53

## Function for checking if an order ID exists using direct access
## @params: id_searched
## @return: True if the order exists, False otherwise
def check_order_exists(id_searched):
    with open('Orders_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id_searched - 1) * ORDER_REGISTER_LEN)
        register = file.read(ORDER_REGISTER_LEN)

# If the file is shorter than a full register, the id does not exist.
        if not register or len(register) < ORDER_REGISTER_LEN:
            print(f"\nError: Order ID {id_searched} does not exist.")
            return False

        active = register[0:1]

        if active == "0":
            print(f"\nError: Order ID {id_searched} was deleted.")
            return False

    return True

## Function for creating a new order using direct access
## @params: id, client_id, shop_id, date, total, status, product_id
## @return: True if the order was created, False otherwise
def create_order_direct(id, client_id, shop_id, date, total, status, product_id):
# Create the file only when the create action runs,
# and only if it does not exist
    if not os.path.exists('Orders_direct.txt'):
        open('Orders_direct.txt', 'w', encoding='utf-8').close()

# Try/except for client validation
# the client of the order must exist
    try:
        with open('Clients_direct.txt', 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("\nError: Clients_direct.txt does not exist.")
        return False

# Try/except for shop validation
# the shop of the order must exist
    try:
        with open('Shops_direct.txt', 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("\nError: Shops_direct.txt does not exist.")
        return False

# Try/except for product validation
# the product of the order must exist
    try:
        with open('Products_direct.txt', 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("\nError: Products_direct.txt does not exist.")
        return False

    register = build_order(1, id, client_id, shop_id, date, total, status, product_id)

    with open('Orders_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * ORDER_REGISTER_LEN)
        file.write(register)
    print(f"\nOrder {id} was created.")

## Function for reading a specific order using direct access
## @params: id
## @return: None
def read_order_direct(id):
# If the file was never created there is nothing to read.
    if not os.path.exists('Orders_direct.txt'):
        print(f"\nError: Orders_direct.txt does not exist.")
        return

    with open('Orders_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id - 1) * ORDER_REGISTER_LEN)
        register = file.read(ORDER_REGISTER_LEN)
# IF statement for checking if the order ID exists
        if not register or len(register) < ORDER_REGISTER_LEN:
            print(f"\nOrder with ID {id} was not found.")
            return

        active = register[0:1]
# IF statement for checking if the order is deleted
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")
            return

        order_id = register[1:5].strip()
        client_id = register[5:9].strip()
        shop_id = register[9:13].strip()
        date = register[13:23].strip()
        total = register[23:33].strip()
        status = register[33:48].strip()
        product_id = register[48:52].strip()

        print("\nOrder found:")
        print("ID:", order_id)
        print("Client ID:", client_id)
        print("Shop ID:", shop_id)
        print("Date:", date)
        print("Total:", total)
        print("Status:", status)
        print("Product ID:", product_id)

## Function for reading all orders from the file
## @params: None
## @return: None
def read_orders_direct():
# If the file was never created there is nothing to read.
    if not os.path.exists('Orders_direct.txt'):
        print(f"\nError: Orders_direct.txt does not exist.")
        return

    with open('Orders_direct.txt', 'r', encoding='utf-8') as file:
# While loop for reading the entire file
        while True:
            register = file.read(ORDER_REGISTER_LEN)
            if not register:
                break
            if len(register) < ORDER_REGISTER_LEN:
                break
            active = register[0:1]
            if active == "0":
                continue

            order_id = register[1:5].strip()
            client_id = register[5:9].strip()
            shop_id = register[9:13].strip()
            date = register[13:23].strip()
            total = register[23:33].strip()
            status = register[33:48].strip()
            product_id = register[48:52].strip()
            print(order_id, "-", client_id, "-", shop_id, "-", date, "-", total, "-", status, "-", product_id)

## Function for updating an order using direct access
## @params: id, client_id, shop_id, date, total, status, product_id
## @return: True if the order was updated, False otherwise
def update_order_direct(id, client_id, shop_id, date, total, status, product_id):
# If the file was never created there is nothing to update.
    if not os.path.exists('Orders_direct.txt'):
        print(f"\nError: Orders_direct.txt does not exist.")
        return False

    with open('Orders_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * ORDER_REGISTER_LEN)
        register = file.read(ORDER_REGISTER_LEN)

        if not register or len(register) < ORDER_REGISTER_LEN:
            print(f"\nOrder with ID {id} was not found.")
            return False

        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        new_register = build_order(active, id, client_id, shop_id, date, total, status, product_id)
        file.seek((id - 1) * ORDER_REGISTER_LEN)
        file.write(new_register)
    print(f"\nOrder {id} was updated.")

## Function for deleting an order using direct access
## @params: id
## @return: True if the order was deleted, False otherwise
def delete_order_direct(id):
# If the file was never created there is nothing to delete.
    if not os.path.exists('Orders_direct.txt'):
        print(f"\nError: Orders_direct.txt does not exist.")
        return False

    with open('Orders_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * ORDER_REGISTER_LEN)
        register = file.read(ORDER_REGISTER_LEN)

        if not register or len(register) < ORDER_REGISTER_LEN:
            print(f"\nOrder with ID {id} was not found.")
            return False
        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        file.seek((id - 1) * ORDER_REGISTER_LEN)
        file.write("0")
    print(f"\nOrder {id} was deleted.")

# We used return false at the end of an statement for close the process