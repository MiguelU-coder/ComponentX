# Crud creation for 'ComponentX' direct access operations
# This crud will help with the Users organizations and inventory

# 'os' is used to check whether the data files already exist
# before creating them (files are only created when an action runs).
import os

## Function for building a length user register
## @params: active, id, name, mail, rol, shop_id
## @return: length user register
def build_user(active, id, name, mail, rol, shop_id):
    return (
        str(active).ljust(1) +
        str(id).zfill(4) +
        str(name)[:30].ljust(30) +
        str(mail)[:20].ljust(20) +
        str(rol)[:15].ljust(15) +
        str(shop_id).zfill(4) +
        "\n"
    )

# Width of each field in the register (in bytes):
# active = 1
# id = 4
# name = 30
# mail = 20
# rol = 15
# shop_id = 4
# newline = 1
# Total length of a register: 1+4+30+20+15+4+1 = 75.

USER_REGISTER_LEN = 75

## Function for checking if a user ID exists using direct access
## @params: id_searched
## @return: True if the user exists, False otherwise
def check_user_exists(id_searched):
    with open('Users_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id_searched - 1) * USER_REGISTER_LEN)
        register = file.read(USER_REGISTER_LEN)

# If the file is shorter than a full register, the id does not exist.
        if not register or len(register) < USER_REGISTER_LEN:
            print(f"\nError: User ID {id_searched} does not exist.")
            return False

        active = register[0:1]

        if active == "0":
            print(f"\nError: User ID {id_searched} was deleted.")
            return False

    return True

## Function for creating a new user using direct access
## @params: id, name, mail, rol, shop_id
## @return: True if the user was created, False otherwise
def create_user_direct(id, name, mail, rol, shop_id):
# Create the file only when the create action runs,
# and only if it does not exist
    if not os.path.exists('Users_direct.txt'):
        open('Users_direct.txt', 'w', encoding='utf-8').close()

# Prevent duplicate ids
    if check_user_exists(id):
        print(f"\nError: User ID {id} already exists.")
        return False

# Try/except for shop validation
# the shop the user belongs to must exist
    try:
        with open('Shops_direct.txt', 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("\nError: Shops_direct.txt does not exist.")
        return False

    register = build_user(1, id, name, mail, rol, shop_id)

    with open('Users_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * USER_REGISTER_LEN)
        file.write(register)
    print(f"\nUser {id} was created.")

## Function for reading a specific user using direct access
## @params: id
## @return: None
def read_user_direct(id):
# If the file was never created there is nothing to read.
    if not os.path.exists('Users_direct.txt'):
        print(f"\nError: Users_direct.txt does not exist.")
        return

    with open('Users_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id - 1) * USER_REGISTER_LEN)
        register = file.read(USER_REGISTER_LEN)
# IF statement for checking if the user ID exists
        if not register or len(register) < USER_REGISTER_LEN:
            print(f"\nUser with ID {id} was not found.")
            return

        active = register[0:1]
# IF statement for checking if the user is deleted
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")
            return

        user_id = register[1:5].strip()
        name = register[5:35].strip()
        mail = register[35:55].strip()
        rol = register[55:70].strip()
        shop_id = register[70:74].strip()

        print("\nUser found:")
        print("ID:", user_id)
        print("Name:", name)
        print("Mail:", mail)
        print("Rol:", rol)
        print("Shop ID:", shop_id)

## Function for reading all users from the file
## @params: None
## @return: None
def read_users_direct():
# If the file was never created there is nothing to read.
    if not os.path.exists('Users_direct.txt'):
        print(f"\nError: Users_direct.txt does not exist.")
        return

    with open('Users_direct.txt', 'r', encoding='utf-8') as file:
# While loop for reading the entire file
        while True:
            register = file.read(USER_REGISTER_LEN)
            if not register:
                break
            if len(register) < USER_REGISTER_LEN:
                break
            active = register[0:1]
            if active == "0":
                continue

            user_id = register[1:5].strip()
            name = register[5:35].strip()
            mail = register[35:55].strip()
            rol = register[55:70].strip()
            shop_id = register[70:74].strip()
            print(user_id, "-", name, "-", mail, "-", rol, "-", shop_id)

## Function for updating a user using direct access
## @params: id, name, mail, rol, shop_id
## @return: True if the user was updated, False otherwise
def update_user_direct(id, name, mail, rol, shop_id):
# If the file was never created there is nothing to update.
    if not os.path.exists('Users_direct.txt'):
        print(f"\nError: Users_direct.txt does not exist.")
        return False

    with open('Users_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * USER_REGISTER_LEN)
        register = file.read(USER_REGISTER_LEN)

        if not register or len(register) < USER_REGISTER_LEN:
            print(f"\nUser with ID {id} was not found.")
            return False

        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        new_register = build_user(active, id, name, mail, rol, shop_id)
        file.seek((id - 1) * USER_REGISTER_LEN)
        file.write(new_register)
    print(f"\nUser {id} was updated.")

## Function for deleting a user using direct access
## @params: id
## @return: True if the user was deleted, False otherwise
def delete_user_direct(id):
# If the file was never created there is nothing to delete.
    if not os.path.exists('Users_direct.txt'):
        print(f"\nError: Users_direct.txt does not exist.")
        return False

    with open('Users_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * USER_REGISTER_LEN)
        register = file.read(USER_REGISTER_LEN)

        if not register or len(register) < USER_REGISTER_LEN:
            print(f"\nUser with ID {id} was not found.")
            return False
        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        file.seek((id - 1) * USER_REGISTER_LEN)
        file.write("0")
    print(f"\nUser {id} was deleted.")

# We used return false at the end of an statement for close the process