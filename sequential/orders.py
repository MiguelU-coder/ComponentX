# Crud creation for 'ComponentX' basic operations
# This crud will help with the orders organizations and inventory

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

## Function for creating a new order
## @params: id, client_id, shop_id, date, total, status, product_id
def create_order(id, client_id, shop_id, date, total, status, product_id):
    if check_id_exists('Orders.txt', id):
        print(f"\nError: Order ID {id} already exists.")
        return False
    from direct.clients import check_client_exists
    from direct.shops import check_shop_exists
    if not check_client_exists(client_id):
        print(f"\nError: Client ID {client_id} does not exist.")
        return False
    if not check_shop_exists(shop_id):
        print(f"\nError: Shop ID {shop_id} does not exist.")
        return False
    if not check_id_exists('Products.txt', product_id):
        print(f"\nError: Product ID {product_id} does not exist.")
        return False
# If statement for checking if the status exists in the status tree
    from arboles.orders_tree import is_valid_status
    if not is_valid_status(status):
        print(f"\nError: Status '{status}' does not exist in the status tree.")
        return False
    with open('Orders.txt', 'a', encoding='utf-8') as file:
        lines = (f"0,{id}, {client_id}, {shop_id}, {date}, {total}, {status}, {product_id}\n") 
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
# If statement for checking if the status exists in the status tree
    from arboles.orders_tree import is_valid_status
    if not is_valid_status(status):
        print(f"\nError: Status '{status}' does not exist in the status tree.")
        return False

    new_lines = []
    with open('Orders.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split(',')
# The if function will help to identify if the id_searched is equal to the id of the shop
            if fields[1] == str(id_searched):
                fields[2] = str(client_id)
                fields[3] = str(shop_id)
                fields[4] = str(date)
                fields[5] = str(total)
                fields[6] = str(status)
                fields[7] = str(product_id)
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
            if fields[1] != str(id_searched):
                new_lines.append(line)
            else:
                print(f"Deleting an order with the id: {id_searched}")
    with open('Orders.txt', 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line)

# When a param is readed or asked by a IF condition is changed to str because
# When we do the 'join' we have to change all the parameters to the same Type