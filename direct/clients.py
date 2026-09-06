# Crud creation for 'ComponentX' direct access operations
# This crud will help with the Clients organizations and inventory

# 'os' is used to check whether the data files already exist
# before creating them (files are only created when an action runs).
import os

## Function for building a length client register
## @params: active, id, name, mail, shop_id
## @return: length client register
def build_client(active, id, name, mail, shop_id):
    return (
        str(active).ljust(1) +
        str(id).zfill(4) +
        str(name)[:30].ljust(30) +
        str(mail)[:20].ljust(20) +
        str(shop_id).zfill(4) +
        "\n"
    )

# Width of each field in the register (in bytes):
# active = 1
# id = 4
# name = 30
# mail = 20
# shop_id = 4
# newline = 1
# Total length of a register: 1+4+30+20+4+1 = 60.

CLIENT_REGISTER_LEN = 60

## Function for checking if a client ID exists using direct access
## @params: id_searched
## @return: True if the client exists, False otherwise
def check_client_exists(id_searched):
    with open('Clients_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id_searched - 1) * CLIENT_REGISTER_LEN)
        register = file.read(CLIENT_REGISTER_LEN)

# If the file is shorter than a full register, the id does not exist.
        if not register or len(register) < CLIENT_REGISTER_LEN:
            print(f"\nError: Client ID {id_searched} does not exist.")
            return False

        active = register[0:1]

        if active == "0":
            print(f"\nError: Client ID {id_searched} was deleted.")
            return False

    return True

## Function for creating a new client using direct access
## @params: id, name, mail, shop_id
## @return: True if the client was created, False otherwise
def create_client_direct(id, name, mail, shop_id):
# Create the file only when the create action runs,
# and only if it does not exist
    if not os.path.exists('Clients_direct.txt'):
        open('Clients_direct.txt', 'w', encoding='utf-8').close()

# Try/except for shop validation
# the shop the client belongs to must exist
    try:
        with open('Shops_direct.txt', 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("\nError: Shops_direct.txt does not exist.")
        return False

    register = build_client(1, id, name, mail, shop_id)

    with open('Clients_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * CLIENT_REGISTER_LEN)
        file.write(register)
    print(f"\nClient {id} was created.")

## Function for reading a specific client using direct access
## @params: id
## @return: None
def read_client_direct(id):
# If the file was never created there is nothing to read.
    if not os.path.exists('Clients_direct.txt'):
        print(f"\nError: Clients_direct.txt does not exist.")
        return

    with open('Clients_direct.txt', 'r', encoding='utf-8') as file:
        file.seek((id - 1) * CLIENT_REGISTER_LEN)
        register = file.read(CLIENT_REGISTER_LEN)
# IF statement for checking if the client ID exists
        if not register or len(register) < CLIENT_REGISTER_LEN:
            print(f"\nClient with ID {id} was not found.")
            return

        active = register[0:1]
# IF statement for checking if the client is deleted
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")
            return

        client_id = register[1:5].strip()
        name = register[5:35].strip()
        mail = register[35:55].strip()
        shop_id = register[55:59].strip()

        print("\nClient found:")
        print("ID:", client_id)
        print("Name:", name)
        print("Mail:", mail)
        print("Shop ID:", shop_id)

## Function for reading all clients from the file
## @params: None
## @return: None
def read_clients_direct():
# If the file was never created there is nothing to read.
    if not os.path.exists('Clients_direct.txt'):
        print(f"\nError: Clients_direct.txt does not exist.")
        return

    with open('Clients_direct.txt', 'r', encoding='utf-8') as file:
# While loop for reading the entire file
        while True:
            register = file.read(CLIENT_REGISTER_LEN)
            if not register:
                break
            if len(register) < CLIENT_REGISTER_LEN:
                break
            active = register[0:1]
            if active == "0":
                continue

            client_id = register[1:5].strip()
            name = register[5:35].strip()
            mail = register[35:55].strip()
            shop_id = register[55:59].strip()
            print(client_id, "-", name, "-", mail, "-", shop_id)

## Function for updating a client using direct access
## @params: id, name, mail, shop_id
## @return: True if the client was updated, False otherwise
def update_client_direct(id, name, mail, shop_id):
# If the file was never created there is nothing to update.
    if not os.path.exists('Clients_direct.txt'):
        print(f"\nError: Clients_direct.txt does not exist.")
        return False

    with open('Clients_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * CLIENT_REGISTER_LEN)
        register = file.read(CLIENT_REGISTER_LEN)

        if not register or len(register) < CLIENT_REGISTER_LEN:
            print(f"\nClient with ID {id} was not found.")
            return False

        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        new_register = build_client(active, id, name, mail, shop_id)
        file.seek((id - 1) * CLIENT_REGISTER_LEN)
        file.write(new_register)
    print(f"\nClient {id} was updated.")

## Function for deleting a client using direct access
## @params: id
## @return: True if the client was deleted, False otherwise
def delete_client_direct(id):
# If the file was never created there is nothing to delete.
    if not os.path.exists('Clients_direct.txt'):
        print(f"\nError: Clients_direct.txt does not exist.")
        return False

    with open('Clients_direct.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * CLIENT_REGISTER_LEN)
        register = file.read(CLIENT_REGISTER_LEN)

        if not register or len(register) < CLIENT_REGISTER_LEN:
            print(f"\nClient with ID {id} was not found.")
            return False
        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")

        file.seek((id - 1) * CLIENT_REGISTER_LEN)
        file.write("0")
    print(f"\nClient {id} was deleted.")

# We used return false at the end of an statement for close the process