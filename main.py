import os

from sequential.products import create_product, read_products, update_product, delete_product
from sequential.orders import create_order, read_orders, update_order, delete_order

from direct.clients import create_client_direct, read_clients_direct, update_client_direct, delete_client_direct
from direct.users import create_user_direct, read_users_direct, update_user_direct, delete_user_direct
from direct.shops import create_shop_direct, read_shops_direct, update_shop_direct, delete_shop_direct

from sorting.external_sorting import organize_external
from sorting.direct_sorting import sort_clients_direct, sort_users_direct, sort_shops_direct

from arboles.categories import (TREE_FILE, get_tree, add_category, show, count_nodes, count_leaves, height, preorder, postorder, search, level_of, delete, save_tree)
from arboles.roles import (ROLES_FILE, get_roles_tree, list_roles, add_area, add_role, delete_role, build_roles_with_users)
# The binary tree functions are used with the module name (binary_tree.show, binary_tree.search...)
# because the categories tree already uses the names show, search, height...
from arboles import binary_tree
from arboles.orders_tree import build_status_tree, load_order_trees, show_order, show_orders, finish_order

# Fields of every entity used to ask the user which field to sort by.
FIELD_BY_ENTITY = {
    "clients":  ["id", "name", "mail", "shop_id"],
    "products": ["id", "name", "category", "stock", "price", "shop_id", "description"],
    "users":    ["id", "name", "mail", "rol", "shop_id"],
    "orders":   ["id", "client_id", "shop_id", "date", "total", "status", "product_id"],
    "shops":    ["id", "name", "description", "admin_user_id"],
}

# Sequential files of the sequential-access entities (products and orders).
ENTITY_FILES = {
    "products": "Products.txt",
    "orders":   "Orders.txt",
}

# Entities that use fixed-length direct access (CRUD and direct merge sort).
# The rest (products, orders) use sequential access and the external sort.
DIRECT_ACCESS_ENTITIES = ("clients", "users", "shops")

# Direct input files of the entities that use direct access.
DIRECT_ENTITY_FILES = {
    "clients": "Clients_direct.txt",
    "users":   "Users_direct.txt",
    "shops":   "Shops_direct.txt",
}


def menu_clients():
    while True:
        print("\n===== CLIENTS (DIRECT ACCESS) =====")
        print("1. Create client")
        print("2. Read clients")
        print("3. Update client")
        print("4. Delete client")
        print("0. Back")

        option = input("Select an option: ")

        match option:
            case "1":
                id = int(input("Enter the client's ID: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                shop_id = int(input("Enter the shop's ID: "))
                create_client_direct(id, name, mail, shop_id)

            case "2":
                read_clients_direct()

            case "3":
                id_searched = int(input("Enter the client's ID to update: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                shop_id = int(input("Enter the shop's ID: "))
                update_client_direct(id_searched, name, mail, shop_id)

            case "4":
                id_searched = int(input("Enter the client's ID to delete: "))
                delete_client_direct(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_products():
    while True:
        print("\n===== PRODUCTS (SEQUENTIAL ACCESS) =====")
        print("1. Create product")
        print("2. Read products")
        print("3. Update product")
        print("4. Delete product")
        print("0. Back")

        option = input("Select an option: ")

        match option:
            case "1":
                id = int(input("Enter the product's ID: "))
                name = input("Enter the name: ")
                category = input("Enter the category: ")
                stock = int(input("Enter the stock: "))
                price = float(input("Enter the price: "))
                shop_id = int(input("Enter the shop's ID: "))
                description = input("Enter the description: ")
                create_product(id, name, category, stock, price, shop_id, description)

            case "2":
                read_products()

            case "3":
                id_searched = int(input("Enter the product's ID to update: "))
                name = input("Enter the name: ")
                category = input("Enter the category: ")
                stock = int(input("Enter the stock: "))
                price = float(input("Enter the price: "))
                shop_id = int(input("Enter the shop's ID: "))
                description = input("Enter the description: ")
                update_product(id_searched, name, category, stock, price, shop_id, description)

            case "4":
                id_searched = int(input("Enter the product's ID to delete: "))
                delete_product(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_users():
    while True:
        print("\n===== USERS (DIRECT ACCESS) =====")
        print("1. Create user")
        print("2. Read users")
        print("3. Update user")
        print("4. Delete user")
        print("0. Back")

        option = input("Select an option: ")

        match option:
            case "1":
                id = int(input("Enter the user's ID: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                print("Valid roles:", ", ".join(list_roles(get_roles_tree())))
                rol = input("Enter the rol: ")
                shop_id = int(input("Enter the shop's ID: "))
                create_user_direct(id, name, mail, rol, shop_id)

            case "2":
                read_users_direct()

            case "3":
                id_searched = int(input("Enter the user's ID to update: "))
                name = input("Enter the name: ")
                mail = input("Enter the mail: ")
                print("Valid roles:", ", ".join(list_roles(get_roles_tree())))
                rol = input("Enter the rol: ")
                shop_id = int(input("Enter the shop's ID: "))
                update_user_direct(id_searched, name, mail, rol, shop_id)

            case "4":
                id_searched = int(input("Enter the user's ID to delete: "))
                delete_user_direct(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_orders():
    while True:
        print("\n===== ORDERS (SEQUENTIAL ACCESS) =====")
        print("1. Create order")
        print("2. Read orders")
        print("3. Update order")
        print("4. Delete order")
        print("5. Show status tree")
        print("6. Orders in progress (by ID)")
        print("7. Finished orders (by ID)")
        print("8. Next order to prepare")
        print("9. Finish order")
        print("10. Search order")
        print("0. Back")

        option = input("Select an option: ")

        match option:
            case "1":
                id = int(input("Enter the order's ID: "))
                client_id = int(input("Enter the client's ID: "))
                shop_id = int(input("Enter the shop's ID: "))
                date = input("Enter the date: ")
                total = float(input("Enter the total: "))
                print("Valid status: pendiente, activo, entregado, cancelado")
                status = input("Enter the status: ")
                product_id = int(input("Enter the product's ID: "))
                create_order(id, client_id, shop_id, date, total, status, product_id)

            case "2":
                read_orders()

            case "3":
                id_searched = int(input("Enter the order's ID to update: "))
                client_id = int(input("Enter the client's ID: "))
                shop_id = int(input("Enter the shop's ID: "))
                date = input("Enter the date: ")
                total = float(input("Enter the total: "))
                print("Valid status: pendiente, activo, entregado, cancelado")
                status = input("Enter the status: ")
                product_id = int(input("Enter the product's ID: "))
                update_order(id_searched, client_id, shop_id, date, total, status, product_id)

            case "4":
                id_searched = int(input("Enter the order's ID to delete: "))
                delete_order(id_searched)

            case "5":
                status_root = build_status_tree()
                binary_tree.show(status_root)
                print("\nTotal nodes:", binary_tree.count_nodes(status_root))
                print("Total leaves (statuses):", binary_tree.count_leaves(status_root))
                print("Height:", binary_tree.height(status_root))

            case "6":
                # The trees are built again from the file every time
                in_progress, finished = load_order_trees()
                show_orders(in_progress)
                print("\nInorder:", binary_tree.inorder(in_progress))
                print("Preorder:", binary_tree.preorder(in_progress))
                print("Postorder:", binary_tree.postorder(in_progress))
                print("Height:", binary_tree.height(in_progress))

            case "7":
                in_progress, finished = load_order_trees()
                show_orders(finished)
                print("\nInorder:", binary_tree.inorder(finished))
                print("Height:", binary_tree.height(finished))

            case "8":
                # The smallest ID in progress is the oldest order
                in_progress, finished = load_order_trees()
                node = binary_tree.minimum(in_progress)
                if node is None:
                    print("There are no orders in progress")
                else:
                    print("Next order to prepare:")
                    show_order(node.value)

            case "9":
                in_progress, finished = load_order_trees()
                order_id = int(input("Enter the order's ID to finish: "))
                new_status = input("Enter the new status (entregado / cancelado): ")
                in_progress, finished = finish_order(in_progress, finished, order_id, new_status)
                print("\nIn progress:", binary_tree.inorder(in_progress))
                print("Finished:", binary_tree.inorder(finished))

            case "10":
                in_progress, finished = load_order_trees()
                order_id = int(input("Enter the order's ID to search: "))
                node = binary_tree.search(in_progress, order_id)
                if node is not None:
                    print("The order is in progress")
                else:
                    node = binary_tree.search(finished, order_id)
                    if node is not None:
                        print("The order is finished")
                if node is None:
                    print("Order not found")
                else:
                    show_order(node.value)

            case "0":
                break

            case _:
                print("Invalid Option")


def menu_shops():
    while True:
        print("\n===== SHOPS (DIRECT ACCESS) =====")
        print("1. Create shop")
        print("2. Read shops")
        print("3. Update shop")
        print("4. Delete shop")
        print("0. Back")

        option = input("Select an option: ")

        match option:
            case "1":
                id = int(input("Enter the shop's ID: "))
                name = input("Enter the name: ")
                description = input("Enter the description: ")
                admin_user_id = int(input("Enter the admin user's ID: "))
                create_shop_direct(id, name, description, admin_user_id)

            case "2":
                read_shops_direct()

            case "3":
                id_searched = int(input("Enter the shop's ID to update: "))
                name = input("Enter the name: ")
                description = input("Enter the description: ")
                admin_user_id = int(input("Enter the admin user's ID: "))
                update_shop_direct(id_searched, name, description, admin_user_id)

            case "4":
                id_searched = int(input("Enter the shop's ID to delete: "))
                delete_shop_direct(id_searched)

            case "0":
                break

            case _:
                print("Invalid Option")


## Function for sorting an entity using the correct algorithm.
## Direct merge sort is used for shops, users and clients.
## Sequential (external) sort is used for products and orders.
## @params: entity, field_name, field_index, input_file
## @return: None
def sort_by_entity(entity, field_name, field_index, input_file):
    direct_sorters = {
        "clients": sort_clients_direct,
        "users":   sort_users_direct,
        "shops":   sort_shops_direct,
    }
    # If statement for checking if the entity uses direct merge sort
    if entity in DIRECT_ACCESS_ENTITIES:
        # Run the direct merge sort algorithm,
        # It writes the configured *_direct_sorted.txt file
        direct_sorters[entity](field_name)
    else:
        # Create the output name for the sorted file
        output_name = os.path.splitext(input_file)[0] + '_sorted.txt'
        # Run the sequential (external) sorting algorithm
        organize_external(input_file, output_name, field_index)


## Function for the sort menu, dispatching each entity to its sorting algorithm
## @params: None
## @return: None
def menu_sort():
    entities = {
        "1": "clients",
        "2": "products",
        "3": "users",
        "4": "orders",
        "5": "shops",
    }

    while True:
        print("\n===== SORT MENU =====")
        print("1. Clients")
        print("2. Products")
        print("3. Users")
        print("4. Orders")
        print("5. Shops")
        print("0. Back")

        option = input("Select an entity: ")

        if option == "0":
            break

        entity = entities.get(option)
        # If statement for avoid invalid options from user
        if entity is None:
            print("Invalid Option")
            continue

        # If statement for selecting the input file of each sorting algorithm
        if entity in DIRECT_ACCESS_ENTITIES:
            file_name = DIRECT_ENTITY_FILES[entity]
        else:
            file_name = ENTITY_FILES[entity]

        # If statement for checking if the file exists
        if not os.path.exists(file_name):
            print(f"\nError: {file_name} does not exist. Create records first.")
            continue

        fields = FIELD_BY_ENTITY[entity]

        # New loop for selecting the field to sort by
        while True:
            print(f"\n===== SORT {entity.upper()} by {file_name} =====")
            for i, field in enumerate(fields, start=1):
                print(f"{i}. {field}")
            print("0. Back")

            field_option = input("Select a field: ")

            # If 0 is selected, return to the previous menu
            if field_option == "0":
                break

            # Try to convert the field_option to an integer
            try:
                index = int(field_option)
                # If the index is not in the range of the fields throw error
                if index < 1 or index > len(fields):
                    raise ValueError
            except ValueError:
                print("\nInvalid Option")
                continue

            # The field name is sent to the direct merge sort,
            # The field index is sent to the sequential (external) sort
            field_name = fields[index - 1]

            # Run the sorting algorithm for the selected entity
            sort_by_entity(entity, field_name, index, file_name)

            # Create the output name for the sorted file
            output_name = os.path.splitext(file_name)[0] + '_sorted.txt'
            print(f"\nSorted file written: {output_name}")
            break

## Function for the categories menu, using the categories tree
## @params: None
## @return: None
def menu_categories():
    # The tree is loaded from the file (or created if it does not exist)
    root = get_tree()

    while True:
        print("\n===== CATEGORIES (TREE) =====")
        print("1. Show categories")
        print("2. Add category")
        print("3. Search category")
        print("4. Delete category")
        print("5. Traversals")
        print("0. Back")

        option = input("Select an option: ")

        match option:
            case "1":
                show(root)
                print("\nTotal nodes:", count_nodes(root))
                print("Total leaves:", count_leaves(root))
                print("Height:", height(root))

            case "2":
                parent = input("Enter the parent category: ")
                name = input("Enter the new category: ")
                # The tree is saved only if the category was added
                if add_category(root, parent, name):
                    save_tree(root, TREE_FILE)
                    print("Category added")

            case "3":
                name = input("Enter the category to search: ")
                node = search(root, name)
                if node is not None:
                    print("Found:", node.data, "- level", level_of(root, name))
                    print("Subcategories:")
                    show(node)
                else:
                    print("Category not found")

            case "4":
                name = input("Enter the category to delete: ")
                # The root can not be deleted
                if name == root.data:
                    print("The root can not be deleted")
                elif delete(root, name):
                    save_tree(root, TREE_FILE)
                    print("Category deleted (with its subcategories)")
                else:
                    print("Category not found")

            case "5":
                print("Preorder:", preorder(root))
                print("Postorder:", postorder(root))

            case "0":
                break

            case _:
                print("Invalid Option")


## Function for the roles menu, using the roles tree (areas -> roles -> users)
## @params: None
## @return: None
def menu_roles():
    # The tree is loaded from the file (or created if it does not exist)
    root = get_roles_tree()

    while True:
        print("\n===== ROLES (TREE) =====")
        print("1. Show roles")
        print("2. Show roles with users")
        print("3. Add area")
        print("4. Add role")
        print("5. Search role")
        print("6. Delete role/area")
        print("7. Traversals")
        print("0. Back")

        option = input("Select an option: ")

        match option:
            case "1":
                show(root)
                print("\nTotal nodes:", count_nodes(root))
                print("Total leaves:", count_leaves(root))
                print("Height:", height(root))

            case "2":
                show(build_roles_with_users(root))

            case "3":
                name = input("Enter the new area: ")
                # The tree is saved only if the area was added
                if add_area(root, name):
                    save_tree(root, ROLES_FILE)
                    print("Area added")

            case "4":
                area = input("Enter the area: ")
                name = input("Enter the new role: ")
                # The tree is saved only if the role was added
                if add_role(root, area, name):
                    save_tree(root, ROLES_FILE)
                    print("Role added")

            case "5":
                name = input("Enter the role or area to search: ")
                node = search(root, name)
                if node is not None:
                    print("Found:", node.data, "- level", level_of(root, name))
                    show(node)
                else:
                    print("Role not found")

            case "6":
                name = input("Enter the role or area to delete: ")
                if delete_role(root, name):
                    save_tree(root, ROLES_FILE)
                    print("Deleted")

            case "7":
                print("Preorder:", preorder(root))
                print("Postorder:", postorder(root))

            case "0":
                break

            case _:
                print("Invalid Option")


def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Clients")
        print("2. Products")
        print("3. Users")
        print("4. Orders")
        print("5. Shops")
        print("6. Sort")
        print("7. Categories")
        print("8. Roles")
        print("0. Exit")

        option = input("Select an option: ")

        match option:
            case "1":
                menu_clients()
            case "2":
                menu_products()
            case "3":
                menu_users()
            case "4":
                menu_orders()
            case "5":
                menu_shops()
            case "6":
                menu_sort()
            case "7":
                menu_categories()
            case "8":
                menu_roles()
            case "0":
                break
            case _:
                print("Invalid Option")


if __name__ == "__main__":
    main()