# Crud creation for 'ComponentX' basic operations
# This crud will help with the users organizations and inventory

import os
# OS is imported to check if the file exists

## Function for checking if an ID exists in a file
## @params: filename, id_searched
## @return: None
def check_id_exists(filename, id_searched):
    if not os.path.exists(filename):
        return False
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            if fields and fields[1] == str(id_searched):
                return True
    return False

## Function for creating a new Shop
## @params: id, name, mail, rol, shop_id
def create_user(id, name, mail, rol, shop_id):
    if not check_id_exists('Shops.txt', shop_id):
        print(f"\nError: Shop ID {shop_id} does not exist.")
        return False
    with open('Users.txt', 'a', encoding='utf-8') as file:
        lines = (f"0,{id}, {name}, {mail}, {rol}, {shop_id}\n") 
        file.write(lines)
        print("A new line was written")

## Function for reading the Users file
## @params: None    
## @return: None
def read_users():
    with open('Users.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            print(f"Fields read are: {fields}")

## Function for updating the user information
## @params: id_searched, name, mail, rol, shop_id
## @return: None
def update_user(id_searched, name, mail, rol, shop_id):
    new_lines = []
    with open('Users.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
# The if function will help to identify if the id_searched is equal to the id of the shop
            if fields[1] == str(id_searched):
                fields[2] = str(name)
                fields[3] = str(mail)
                fields[4] = str(rol)
                fields[5] = str(shop_id)
            new_lines.append(','.join(fields))

    with open('Users.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line + '\n')

## Function for deleting a user
## @params: id_searched
## @return: None
def delete_user(id_searched):
    new_lines = []
    with open('Users.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[1] != str(id_searched):
                new_lines.append(line)
                print(f"Deleting a user with the id: {id_searched}")
    with open('Users.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line)

# When a param is readed or asked by a IF condition is changed to str because
# When we do the 'join' we have to change all the parameters to the same Type