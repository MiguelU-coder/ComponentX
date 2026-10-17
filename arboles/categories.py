import os

TREE_FILE = "Categories.txt"

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def show(node, level=0):
    print("  " * level + node.data)
    for child in node.children:
        show(child, level + 1)


def count_nodes(node):
    total = 1
    for child in node.children:
        total += count_nodes(child)
    return total


def count_leaves(node):
    if len(node.children) == 0:
        return 1

    total = 0
    for child in node.children:
        total += count_leaves(child)
    return total


def height(node):
    if len(node.children) == 0:
        return 0

    highest = 0
    for child in node.children:
        child_height = height(child)
        if child_height > highest:
            highest = child_height
    return 1 + highest


def preorder(node):
    result = [node.data]
    for child in node.children:
        result += preorder(child)
    return result


def postorder(node):
    result = []
    for child in node.children:
        result += postorder(child)
    result.append(node.data)
    return result


def search(node, data):
    if node.data == data:
        return node

    for child in node.children:
        found = search(child, data)
        if found is not None:
            return found

    return None


def level_of(node, data, level=0):
    if node.data == data:
        return level

    for child in node.children:
        child_level = level_of(child, data, level + 1)
        if child_level != -1:
            return child_level

    return -1


def delete(node, data):
    for child in node.children:
        if child.data == data:
            node.children.remove(child)
            return True

        if delete(child, data):
            return True

    return False


def save_tree(node, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        _write_node(node, file, level=0)


def _write_node(node, file, level):
    file.write(f"{level};{node.data}\n")
    for child in node.children:
        _write_node(child, file, level + 1)


def load_tree(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    root = None
    last_by_level = {}

    for line in lines:
        level_text, data = line.strip().split(";")
        level = int(level_text)
        current_node = Node(data)

        if level == 0:
            root = current_node
        else:
            last_by_level[level - 1].add_child(current_node)

        last_by_level[level] = current_node

    return root


def build_categories():
    root = Node("ComponentX")
    components = Node("Componentes")
    peripherals = Node("Perifericos")
    storage = Node("Almacenamiento")

    root.add_child(components)
    root.add_child(peripherals)
    root.add_child(storage)

    components.add_child(Node("Procesadores"))
    components.add_child(Node("Memoria RAM"))
    peripherals.add_child(Node("Mouse"))
    peripherals.add_child(Node("Teclados"))
    peripherals.add_child(Node("Monitores"))
    return root


def get_tree():
    # If the file exists the tree is loaded, if not the initial tree is created and saved
    if os.path.exists(TREE_FILE):
        return load_tree(TREE_FILE)

    root = build_categories()
    save_tree(root, TREE_FILE)
    return root


def add_category(root, parent, new):
    parent_node = search(root, parent)
    if parent_node is None:
        print("The parent category does not exist")
        return False

    if search(root, new) is not None:
        print("That category already exists")
        return False

    parent_node.add_child(Node(new))
    return True
