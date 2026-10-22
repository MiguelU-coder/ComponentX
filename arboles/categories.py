from arboles.tree import (Node, show, count_nodes, count_leaves, height, preorder, postorder, search, level_of, delete, save_tree, get_or_build)

TREE_FILE = "Categories.txt"


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
    return get_or_build(TREE_FILE, build_categories)


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
