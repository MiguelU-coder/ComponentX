from arboles.tree import (Node, show, count_nodes, count_leaves, height, preorder, postorder, search, level_of, delete, save_tree, get_or_build)

# Categories tree: the catalog of the shop.
# It is a general tree because a category can have any number of subcategories.
#
#   ComponentX                 <- level 0 (root)
#   |-- Componentes            <- level 1
#   |   |-- Procesadores       <- level 2 (leaf)
#   |   |-- Memoria RAM        <- level 2 (leaf)
#   |-- Perifericos            <- level 1
#   |   |-- Mouse              <- level 2 (leaf)
#   |   |-- Teclados           <- level 2 (leaf)
#   |   |-- Monitores          <- level 2 (leaf)
#   |-- Almacenamiento         <- level 1 (leaf, it has no subcategories)
#
# Height = 2, nodes = 9, leaves = 6

# File where the tree is saved
TREE_FILE = "Categories.txt"


## Function for building the initial categories tree (used when the file does not exist)
## @params: None
## @return: the root of the tree
def build_categories():
    root = Node("ComponentX")
    components = Node("Componentes")
    peripherals = Node("Perifericos")
    storage = Node("Almacenamiento")

    # Level 1: the main categories
    root.add_child(components)
    root.add_child(peripherals)
    root.add_child(storage)

    # Level 2: the subcategories
    components.add_child(Node("Procesadores"))
    components.add_child(Node("Memoria RAM"))
    peripherals.add_child(Node("Mouse"))
    peripherals.add_child(Node("Teclados"))
    peripherals.add_child(Node("Monitores"))
    return root


## Function for getting the categories tree (loaded from Categories.txt or created)
## @params: None
## @return: the root of the tree
def get_tree():
    return get_or_build(TREE_FILE, build_categories)


## Function for adding a new category as a child of another category
## @params: root, parent (name of the parent category), new (name of the new one)
## @return: True if it was added, False otherwise
def add_category(root, parent, new):
    # The parent must exist in the tree
    parent_node = search(root, parent)
    if parent_node is None:
        print("The parent category does not exist")
        return False

    # Two categories can not have the same name
    if search(root, new) is not None:
        print("That category already exists")
        return False

    parent_node.add_child(Node(new))
    return True
