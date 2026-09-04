# Crud creation for 'ComponentX' basic operations
# This crud will help with the orders organizations and inventory

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

## Function for creating a new order
## @params: id, client_id, shop_id, date, total, status, product_id
def create_order(id, client_id, shop_id, date, total, status, product_id):
    if not check_id_exists('Clients.txt', client_id):
        print(f"\nError: Client ID {client_id} does not exist.")
        return False
    if not check_id_exists('Shops.txt', shop_id):
        print(f"\nError: Shop ID {shop_id} does not exist.")
        return False
    if not check_id_exists('Products.txt', product_id):
        print(f"\nError: Product ID {product_id} does not exist.")
        return False
    with open('Orders.txt', 'a', encoding='utf-8') as file:
        lines = (f"{id}, {client_id}, {shop_id}, {date}, {total}, {status}, {product_id}\n") 
        file.write(lines)
        print("A new line was written")

## Function for reading the orders file
## @params: None
## @return: None
def read_orders():
    with open('Orders.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            print(f"Fields read are: {fields}")

## Function for updating the order information
## @params: id_searched, client_id, shop_id, date, total, status, product_id
## @return: None
def update_order(id_searched, client_id, shop_id, date, total, status, product_id):
    new_lines = []
    with open('Orders.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
# The if function will help to identify if the id_searched is equal to the id of the shop
            if fields[0] == str(id_searched):
                fields[1] = str(client_id)
                fields[2] = str(shop_id)
                fields[3] = str(date)
                fields[4] = str(total)
                fields[5] = str(status)
                fields[6] = str(product_id)
            new_lines.append(','.join(fields))

    with open('Orders.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line + '\n')

## Function for deleting an order
## @params: id_searched
## @return: None
def delete_order(id_searched):
    new_lines = []
    with open('Orders.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
            if fields[0] != str(id_searched):
                new_lines.append(line)
                print(f"Deleting an order with the id: {id_searched}")
    with open('Orders.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line)

# When a param is readed or asked by a IF condition is changed to str because
# When we do the 'join' we have to change all the parameters to the same Type