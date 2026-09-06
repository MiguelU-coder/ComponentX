# Crud creation for 'ComponentX' direct access operations
# This crud will help with the Shops organizations and inventory

# 'os' is used to check whether the data files already exist
# before creating them (files are only created when an action runs).
import os

## Function for building a length shop register
## @params: active, id, name, description, admin_user_id
## @return: length shop register
def build_shop(active, id, name, description, admin_user_id):
    return (
        str(active).ljust(1) +
        str(id).zfill(4) +
        str(name)[:30].ljust(30) +
        str(description)[:50].ljust(50) +
        str(admin_user_id).zfill(4) +
        "\n"
    )

# Width of each field in the register (in bytes):
# active = 1
# id = 4
# name = 30
# description = 50
# admin_user_id = 4
# newline = 1
# Total length of a register: 1+4+30+50+4+1 = 90.

SHOP_REGISTER_LEN = 90

## Function for checking if a shop ID exists using direct access
## @params: id_searched
## @return: True if the shop exists, False otherwise
def check_shop_exists(id_searched):
    with open('Shops_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id_searched - 1) * SHOP_REGISTER_LEN)
        register = file.read(SHOP_REGISTER_LEN)

# If the file is shorter than a full register, the id does not exist.
        if not register or len(register) < SHOP_REGISTER_LEN:
            print(f"\nError: Shop ID {id_searched} does not exist.")
            return False

        active = register[0:1]

        if active == "0":
            print(f"\nError: Shop ID {id_searched} was deleted.")
            return False

    return True

## Function for creating a new shop using direct access
## @params: id, name, description, admin_user_id
## @return: True if the shop was created, False otherwise
def create_shop_direct(id, name, description, admin_user_id):
# Create the file only when the create action runs,
# and only if it does not exist
    if not os.path.exists('Shops_direct.txt'):
        open('Shops_direct.txt', 'w', encoding='utf-8').close()

# Try/except for user validation
# the admin user of the shop must exist
    try:
        with open('Users_direct.txt', 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("\nError: Users_direct.txt does not exist.")
        return False

    register = build_shop(1, id, name, description, admin_user_id)

    with open('Shops_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * SHOP_REGISTER_LEN)
        file.write(register)
    print(f"\nShop {id} was created.")

## Function for reading a specific shop using direct access
## @params: id
## @return: None
def read_shop_direct(id):
# If the file was never created there is nothing to read.
    if not os.path.exists('Shops_direct.txt'):
        print(f"\nError: Shops_direct.txt does not exist.")
        return

    with open('Shops_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id - 1) * SHOP_REGISTER_LEN)
        register = file.read(SHOP_REGISTER_LEN)
# IF statement for checking if the shop ID exists
        if not register or len(register) < SHOP_REGISTER_LEN:
            print(f"\nShop with ID {id} was not found.")
            return

        active = register[0:1]
# IF statement for checking if the shop is deleted
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")
            return

        shop_id = register[1:5].strip()
        name = register[5:35].strip()
        description = register[35:85].strip()
        admin_user_id = register[85:89].strip()

        print("\nShop found:")
        print("ID:", shop_id)
        print("Name:", name)
        print("Description:", description)
        print("Admin User ID:", admin_user_id)

## Function for reading all shops from the file
## @params: None
## @return: None
def read_shops_direct():
# If the file was never created there is nothing to read.
    if not os.path.exists('Shops_direct.txt'):
        print(f"\nError: Shops_direct.txt does not exist.")
        return

    with open('Shops_direct.txt', 'r', encoding='utf-8') as file:
# While loop for reading the entire file
        while True:
            register = file.read(SHOP_REGISTER_LEN)
            if not register:
                break
            if len(register) < SHOP_REGISTER_LEN:
                break
            active = register[0:1]
            if active == "0":
                continue

            shop_id = register[1:5].strip()
            name = register[5:35].strip()
            description = register[35:85].strip()
            admin_user_id = register[85:89].strip()
            print(shop_id, "-", name, "-", description, "-", admin_user_id)

## Function for updating a shop using direct access
## @params: id, name, description, admin_user_id
## @return: True if the shop was updated, False otherwise
def update_shop_direct(id, name, description, admin_user_id):
# If the file was never created there is nothing to update.
    if not os.path.exists('Shops_direct.txt'):
        print(f"\nError: Shops_direct.txt does not exist.")
        return False

    with open('Shops_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * SHOP_REGISTER_LEN)
        register = file.read(SHOP_REGISTER_LEN)

        if not register or len(register) < SHOP_REGISTER_LEN:
            print(f"\nShop with ID {id} was not found.")
            return False

        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        new_register = build_shop(active, id, name, description, admin_user_id)
        file.seek((id - 1) * SHOP_REGISTER_LEN)
        file.write(new_register)
    print(f"\nShop {id} was updated.")

## Function for deleting a shop using direct access
## @params: id
## @return: True if the shop was deleted, False otherwise
def delete_shop_direct(id):
# If the file was never created there is nothing to delete.
    if not os.path.exists('Shops_direct.txt'):
        print(f"\nError: Shops_direct.txt does not exist.")
        return False

    with open('Shops_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * SHOP_REGISTER_LEN)
        register = file.read(SHOP_REGISTER_LEN)

        if not register or len(register) < SHOP_REGISTER_LEN:
            print(f"\nShop with ID {id} was not found.")
            return False
        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        file.seek((id - 1) * SHOP_REGISTER_LEN)
        file.write("0")
    print(f"\nShop {id} was deleted.")

# We used return false at the end of an statement for close the process