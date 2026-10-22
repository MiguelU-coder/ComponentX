# Binary tree: every node has at most two children (left and right)
# It is used as a plain binary tree (order statuses)
# and as a binary search tree (orders ordered by ID)

class BinaryNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def show(node, level=0, side="Raiz"):
    if node is None:
        return
    print("  " * level + side + ": " + str(node.key))
    show(node.left, level + 1, "Izq")
    show(node.right, level + 1, "Der")


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def height(node):
    # An empty tree has height -1 and a single node has height 0
    if node is None:
        return -1

    left_height = height(node.left)
    right_height = height(node.right)
    if left_height > right_height:
        return 1 + left_height
    return 1 + right_height


def preorder(node):
    if node is None:
        return []
    return [node.key] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.key] + inorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.key]


## Function for finding a key looking at both sides (for trees that are not ordered)
## @params: node, key
## @return: the node found or None
def find(node, key):
    if node is None:
        return None
    if node.key == key:
        return node

    found = find(node.left, key)
    if found is not None:
        return found
    return find(node.right, key)


# ---------- Binary search tree (BST) ----------
# Smaller keys go to the left and bigger keys go to the right


## Function for inserting a key in a binary search tree
## @params: node, key, value
## @return: the root of the tree
def insert(node, key, value):
    if node is None:
        return BinaryNode(key, value)

    if key < node.key:
        node.left = insert(node.left, key, value)
    elif key > node.key:
        node.right = insert(node.right, key, value)
    else:
        print(f"The key {key} is already in the tree")
    return node


## Function for searching a key in a binary search tree
## @params: node, key
## @return: the node found or None
def search(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return search(node.left, key)
    return search(node.right, key)


## Function for getting the node with the smallest key (the leftmost node)
## @params: node
## @return: the node with the smallest key or None
def minimum(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node


## Function for deleting a key from a binary search tree
## @params: node, key
## @return: the root of the tree
def delete(node, key):
    if node is None:
        return None

    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        # Case 1 and 2: the node has no children or only one child
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        # Case 3: the node has two children,
        # it is replaced by the smallest node of the right side
        successor = minimum(node.right)
        node.key = successor.key
        node.value = successor.value
        node.right = delete(node.right, successor.key)
    return node
