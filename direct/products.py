# Crud creation for 'ComponentX' direct access operations
# This crud will help with the Products organizations and inventory


# Define the width of the register
# active = 1
# id = 4
# name = 30
# category = 20
# stock = 6
# price = 10
# shop_id = 4
# description = 50
# newline = 1

PRODUCT_REGISTER_LEN = 126


## Function for building a fixed-length product register
## @params: active, id, name, category, stock, price, shop_id, description
## @return: Fixed-length product register
def build_product(active, id, name, category, stock, price, shop_id, description):
    return (
        str(active).ljust(1) +
        str(id).zfill(4) +
        str(name)[:30].ljust(30) +
        str(category)[:20].ljust(20) +
        str(stock).zfill(6) +
        str(price).zfill(10) +
        str(shop_id).zfill(4) +
        str(description)[:50].ljust(50) +
        "\n"
    )

with open('Products.txt', 'a', encoding='utf-8') as file:
    pass

## Function for checking if a product ID exists using direct access
## @params: id_searched
## @return: True if the product exists, False otherwise
def check_product_exists(id_searched):
    with open('Products.txt', 'r', encoding='utf-8') as file:
        file.seek((id_searched - 1) * PRODUCT_REGISTER_LEN)
        register = file.read(PRODUCT_REGISTER_LEN)
        if not register or len(register) < PRODUCT_REGISTER_LEN:
            return False
        active = register[0:1]
        if active == "0":
            return False


## Function for creating a new product using direct access
## @params: id, name, category, stock, price, shop_id, description
## @return: True if the product was created, False otherwise
def create_product_direct(id, name, category, stock, price, shop_id, description):
    if check_product_exists(id):
        print(f"\nError: Product ID {id} already exists.")
        return False
    try:
        with open('Shops.txt', 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        print("\nError: Shops.txt does not exist.")
        return False

    register = build_product(
        1,
        id,
        name,
        category,
        stock,
        price,
        shop_id,
        description
    )
    with open('Products.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * PRODUCT_REGISTER_LEN)
        file.write(register)
    print(f"\nProduct {id} was created.")

## Function for reading a specific product using direct access
## @params: id
## @return: None
def read_product_direct(id):
    with open('Products.txt', 'r', encoding='utf-8') as file:
        file.seek((id - 1) * PRODUCT_REGISTER_LEN)
        register = file.read(PRODUCT_REGISTER_LEN)
        if not register or len(register) < PRODUCT_REGISTER_LEN:
            print(f"\nProduct with ID {id} was not found.")
            return
        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")
            return
        product_id = register[1:5].strip()
        name = register[5:35].strip()
        category = register[35:55].strip()
        stock = register[55:61].strip()
        price = register[61:71].strip()
        shop_id = register[71:75].strip()
        description = register[75:125].strip()
        print("\nProduct found:")
        print("ID:", product_id)
        print("Name:", name)
        print("Category:", category)
        print("Stock:", stock)
        print("Price:", price)
        print("Shop ID:", shop_id)
        print("Description:", description)

## Function for reading all products from the file
## @params: None
## @return: None
def read_products_direct():
    with open('Products.txt', 'r', encoding='utf-8') as file:
        while True:
            register = file.read(PRODUCT_REGISTER_LEN)
            if not register:
                break
            if len(register) < PRODUCT_REGISTER_LEN:
                break
            active = register[0:1]
            if active == "0":
                continue
            product_id = register[1:5].strip()
            name = register[5:35].strip()
            category = register[35:55].strip()
            stock = register[55:61].strip()
            price = register[61:71].strip()
            shop_id = register[71:75].strip()
            description = register[75:125].strip()
            print(product_id, "-", name, "-", category, "-", stock, "-", price, "-", shop_id, "-", description)

## Function for updating a product using direct access
## @params: id, name, category, stock, price, shop_id, description
## @return: True if the product was updated, False otherwise
def update_product_direct(id, name, category, stock, price, shop_id, description):
    with open('Products.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * PRODUCT_REGISTER_LEN)
        register = file.read(PRODUCT_REGISTER_LEN)
        if not register or len(register) < PRODUCT_REGISTER_LEN:
            print(f"\nProduct with ID {id} was not found.")
            return False
        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")
        new_register = build_product(
            active,
            id,
            name,
            category,
            stock,
            price,
            shop_id,
            description
        )
        file.seek((id - 1) * PRODUCT_REGISTER_LEN)
        file.write(new_register)
    print(f"\nProduct {id} was updated.")

## Function for deleting a product using direct access
## @params: id
## @return: True if the product was deleted, False otherwise
def delete_product_direct(id):
    with open('Products.txt', 'r+', encoding='utf-8') as file:
        file.seek((id - 1) * PRODUCT_REGISTER_LEN)
        register = file.read(PRODUCT_REGISTER_LEN)
        if not register or len(register) < PRODUCT_REGISTER_LEN:
            print(f"\nProduct with ID {id} was not found.")
            return False
        active = register[0:1]
        if active == "0":
            print(f"\nThe register {id}: WAS DELETED")
        file.seek((id - 1) * PRODUCT_REGISTER_LEN)
        file.write("0")
    print(f"\nProduct {id} was deleted.")
