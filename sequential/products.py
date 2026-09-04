# Crud creation for 'ComponentX' basic operations
# This crud will help with the Products organizations and inventory

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

## Function for creating a new Product
## @params: id, name, category, stock, price, shop_id, description 
def create_product(id, name, category, stock, price, shop_id, description):
    if not check_id_exists('Shops.txt', shop_id):
        print(f"\nError: Shop ID {shop_id} does not exist.")
        return False
    with open('Products.txt', 'a', encoding='utf-8') as file:
        lines = (f"{id}, {name}, {category}, {stock}, {price}, {shop_id}, {description}\n") 
        file.write(lines)
        print("A new line was written")

## Function for reading the Products file
## @params: None
## @return: None
def read_products():
    with open('Products.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            print(f"Fields read are: {fields}")

## Function for updating the product information
## @params: id_searched, name, category, stock, price, shop_id, description
## @return: None
def update_product(id_searched, name, category, stock, price, shop_id, description):
    new_lines = []
    with open('Products.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
# The if function will help to identify if the id_searched is equal to the id of the product
            if fields[0] == str(id_searched):
                fields[1] = str(name)
                fields[2] = str(category)
                fields[3] = str(stock)
                fields[4] = str(price)
                fields[5] = str(shop_id)
                fields[6] = str(description)
            new_lines.append(','.join(fields))

    with open('Products.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line + '\n')

## Function for deleting a product
## @params: id_searched
## @return: None
def delete_product(id_searched):
    new_lines = []
    with open('Products.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] != str(id_searched):
                new_lines.append(line)
                print(f"Deleting a product with the id: {id_searched}")
    with open('Products.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line)


# When a param is readed or asked by a IF condition is changed to str because
# When we do the 'join' we have to change all the parameters to the same Type
