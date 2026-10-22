import os

from arboles.binary_tree import BinaryNode, find, insert, search, delete

ORDERS_FILE = "Orders.txt"

# Position of the status field in a line of Orders.txt
STATUS_INDEX = 6


## Function for building the binary tree of the order statuses
## Left side: orders in progress, right side: finished orders
##
##                 Pedidos
##              /           \
##        En curso         Finalizados
##        /      \          /        \
##  pendiente   activo  entregado  cancelado
##
## @params: None
## @return: root of the status tree
def build_status_tree():
    root = BinaryNode("Pedidos")
    root.left = BinaryNode("En curso")
    root.right = BinaryNode("Finalizados")

    root.left.left = BinaryNode("pendiente")
    root.left.right = BinaryNode("activo")
    root.right.left = BinaryNode("entregado")
    root.right.right = BinaryNode("cancelado")
    return root


## Function for checking if a status exists (only the leaves are statuses)
## @params: status
## @return: True if the status is valid, False otherwise
def is_valid_status(status):
    node = find(build_status_tree(), status)
    if node is None:
        return False
    return node.left is None and node.right is None


## Function for checking if a status is on the "En curso" side of the tree
## @params: status
## @return: True if the order is still in progress, False otherwise
def is_in_progress(status):
    root = build_status_tree()
    return find(root.left, status) is not None


## Function for reading the orders file and building two binary search trees
## ordered by ID: one with the orders in progress and one with the finished ones
## @params: None
## @return: in_progress_root, finished_root
def load_order_trees():
    in_progress = None
    finished = None

    if not os.path.exists(ORDERS_FILE):
        return in_progress, finished

    with open(ORDERS_FILE, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "":
                continue

            # strip() removes the spaces that are saved after each comma
            fields = []
            for field in line.split(","):
                fields.append(field.strip())

            order_id = int(fields[1])
            if is_in_progress(fields[STATUS_INDEX]):
                in_progress = insert(in_progress, order_id, fields)
            else:
                finished = insert(finished, order_id, fields)

    return in_progress, finished


## Function for showing one order
## @params: fields
## @return: None
def show_order(fields):
    print("ID:", fields[1], "- client:", fields[2], "- date:", fields[4],
          "- total:", fields[5], "- status:", fields[STATUS_INDEX])


## Function for showing the orders of a tree in order of ID (inorder traversal)
## @params: node
## @return: None
def show_orders(node):
    if node is None:
        return
    show_orders(node.left)
    show_order(node.value)
    show_orders(node.right)


## Function for moving an order from the in progress tree to the finished tree
## @params: in_progress, finished, order_id, new_status
## @return: in_progress, finished (the roots can change)
def finish_order(in_progress, finished, order_id, new_status):
    from sequential.orders import update_order

    node = search(in_progress, order_id)
    if node is None:
        print(f"The order {order_id} is not in progress")
        return in_progress, finished

    if is_in_progress(new_status) or not is_valid_status(new_status):
        print("The new status must be 'entregado' or 'cancelado'")
        return in_progress, finished

    fields = node.value
    fields[STATUS_INDEX] = new_status

    # The change is saved in the file too
    update_order(order_id, fields[2], fields[3], fields[4], fields[5], new_status, fields[7])

    in_progress = delete(in_progress, order_id)
    finished = insert(finished, order_id, fields)
    return in_progress, finished
