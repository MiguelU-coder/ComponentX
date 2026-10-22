import os

# General tree: every node can have any number of children.
# It is used by the categories tree and by the roles tree.
#
# Words used in the comments:
#   root   = the first node, it has no parent (level 0)
#   leaf   = a node without children
#   level  = how many steps there are from the root to the node
#   height = the level of the deepest leaf


## A node of the tree: it saves its data and a list with its children
class Node:
    def __init__(self, data):
        self.data = data        # the name saved in the node
        self.children = []      # the child nodes (empty list = it is a leaf)

    ## Function for adding a child at the end of the children list
    ## @params: child (a Node)
    ## @return: None
    def add_child(self, child):
        self.children.append(child)


## Function for printing the tree, each level with more spaces to the right
## @params: node, level (0 when it starts at the root)
## @return: None
def show(node, level=0):
    print("  " * level + node.data)
    # Each child is printed one level deeper
    for child in node.children:
        show(child, level + 1)


## Function for counting all the nodes of the tree
## The node counts as 1, plus the nodes of each child
## @params: node
## @return: number of nodes
def count_nodes(node):
    total = 1
    for child in node.children:
        total += count_nodes(child)
    return total


## Function for counting the leaves (nodes without children)
## @params: node
## @return: number of leaves
def count_leaves(node):
    # A node without children is a leaf
    if len(node.children) == 0:
        return 1

    # If it has children, the leaves are inside them
    total = 0
    for child in node.children:
        total += count_leaves(child)
    return total


## Function for getting the height of the tree
## A leaf has height 0, any other node is 1 + the height of its tallest child
## @params: node
## @return: height of the tree
def height(node):
    if len(node.children) == 0:
        return 0

    # Look for the tallest child
    highest = 0
    for child in node.children:
        child_height = height(child)
        if child_height > highest:
            highest = child_height
    return 1 + highest


## Function for the preorder traversal: first the node, then its children
## @params: node
## @return: list with the data in preorder
def preorder(node):
    result = [node.data]
    for child in node.children:
        result += preorder(child)
    return result


## Function for the postorder traversal: first the children, at the end the node
## @params: node
## @return: list with the data in postorder
def postorder(node):
    result = []
    for child in node.children:
        result += postorder(child)
    result.append(node.data)
    return result


## Function for searching a node by its data
## It checks the node and if it is not, it searches inside each child
## @params: node, data
## @return: the node found or None if it does not exist
def search(node, data):
    if node.data == data:
        return node

    for child in node.children:
        found = search(child, data)
        # If a child found it, we stop searching
        if found is not None:
            return found

    return None


## Function for getting the level of a node (root = 0, its children = 1...)
## Every time we go down to a child the level grows by 1
## @params: node, data, level (0 when it starts at the root)
## @return: the level of the node or -1 if it does not exist
def level_of(node, data, level=0):
    if node.data == data:
        return level

    for child in node.children:
        child_level = level_of(child, data, level + 1)
        if child_level != -1:
            return child_level

    return -1


## Function for deleting a node, it is deleted with all its children (its subtree)
## The parent removes it from its children list
## @params: node, data
## @return: True if it was deleted, False if it was not found
def delete(node, data):
    for child in node.children:
        # The node to delete is a child of this node: remove it from the list
        if child.data == data:
            node.children.remove(child)
            return True

        # If not, search it inside the child
        if delete(child, data):
            return True

    return False


## Function for saving the tree in a file
## Each line is "level;data", for example "1;Perifericos"
## @params: node, file_path
## @return: None
def save_tree(node, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        _write_node(node, file, level=0)


## Function for writing a node and then its children (in preorder)
## @params: node, file, level
## @return: None
def _write_node(node, file, level):
    file.write(f"{level};{node.data}\n")
    for child in node.children:
        _write_node(child, file, level + 1)


## Function for reading a tree from a file saved with save_tree()
## The parent of a node is the last node read on the level before it
## @params: file_path
## @return: the root of the tree
def load_tree(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    root = None
    # Saves the last node read on each level: {level: node}
    last_by_level = {}

    for line in lines:
        level_text, data = line.strip().split(";")
        level = int(level_text)
        current_node = Node(data)

        if level == 0:
            root = current_node
        else:
            # The parent is the last node of the level before
            last_by_level[level - 1].add_child(current_node)

        last_by_level[level] = current_node

    return root


## Function for getting a tree: it is loaded from the file if the file exists,
## if not, the initial tree is built and saved
## @params: file_path, build_function (the function that builds the initial tree)
## @return: the root of the tree
def get_or_build(file_path, build_function):
    # If the file exists the tree is loaded, if not the initial tree is created and saved
    if os.path.exists(file_path):
        return load_tree(file_path)

    root = build_function()
    save_tree(root, file_path)
    return root
