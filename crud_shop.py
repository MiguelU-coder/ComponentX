# Crud creation for 'ComponentX' basic operations
# This crud will help with the shops organizations and inventory

## Function for checking if an ID exists in a file
## @params: filename, id_searched
## @return: None

import os
# OS is imported to check if the file exists
def check_id_exists(filename, id_searched):
    if not os.path.exists(filename):
        return False
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            if fields and fields[0] == str(id_searched):
                return True
    return False
## Function for creating a new Shop
## @params: id, name, description, admin_user_id
def create_shop(id, name, description, admin_user_id):
    if not check_id_exists('Users.txt', admin_user_id):
        print(f"\nError: User ID {admin_user_id} does not exist.")
        return False
    with open('Shops.txt', 'a', encoding='utf-8') as file:
        lines = (f"{id}, {name}, {description}, {admin_user_id}\n") 
        file.write(lines)
        print("A new line was written")

## Function for reading the Shops file
## @params: None    
## @return: None
def read_shops():
    with open('Shops.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            print(f"Fields read are: {fields}")

## Function for updating the shop information
## @params: id_searched, name, description, admin_user_id
## @return: None
def update_shop(id_searched, name, description, admin_user_id):
    new_lines = []
    with open('Shops.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
# The if function will help to identify if the id_searched is equal to the id of the shop
            if fields[0] == str(id_searched):
                fields[1] = str(name)
                fields[2] = str(description)
                fields[3] = str(admin_user_id)
            new_lines.append(','.join(fields))

    with open('Shops.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line + '\n')

## Function for deleting a shop
## @params: id_searched
## @return: None
def delete_shop(id_searched):
    new_lines = []
    with open('Shops.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] != str(id_searched):
                new_lines.append(line)
                print(f"Deleting a shop with the id: {id_searched}")
    with open('Shops.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line)

# When a param is readed or asked by a IF condition is changed to str because
# When we do the 'join' we have to change all the parameters to the same Type