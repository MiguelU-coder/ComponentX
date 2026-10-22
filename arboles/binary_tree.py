# Binary tree: every node has at most two children (left and right)
# It is used as a plain binary tree (order statuses)
# and as a binary search tree (orders ordered by ID)

## A node of the binary tree
class BinaryNode:
    def __init__(self, key, value=None):
        self.key = key          # what identifies the node (a name or the order ID)
        self.value = value      # extra data (for orders: the fields of the line)
        self.left = None        # left child
        self.right = None       # right child


## Function for printing the tree, each level with more spaces to the right
## Each node says if it is the root (Raiz), a left child (Izq) or a right child (Der)
## @params: node, level, side
## @return: None
def show(node, level=0, side="Raiz"):
    if node is None:
        return
    print("  " * level + side + ": " + str(node.key))
    show(node.left, level + 1, "Izq")
    show(node.right, level + 1, "Der")


## Function for counting all the nodes: 1 for this node + the nodes of each side
## @params: node
## @return: number of nodes
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


## Function for counting the leaves (nodes without left and right child)
## @params: node
## @return: number of leaves
def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


## Function for getting the height: 1 + the height of the tallest side
## @params: node
## @return: height of the tree
def height(node):
    # An empty tree has height -1 and a single node has height 0
    if node is None:
        return -1

    left_height = height(node.left)
    right_height = height(node.right)
    if left_height > right_height:
        return 1 + left_height
    return 1 + right_height


## Function for the preorder traversal: node, left side, right side
## @params: node
## @return: list with the keys in preorder
def preorder(node):
    if node is None:
        return []
    return [node.key] + preorder(node.left) + preorder(node.right)


## Function for the inorder traversal: left side, node, right side
## In a binary search tree it gives the keys from smallest to biggest
## @params: node
## @return: list with the keys in inorder
def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.key] + inorder(node.right)


## Function for the postorder traversal: left side, right side, node
## @params: node
## @return: list with the keys in postorder
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

    # First search on the left; if it is not there, search on the right
    found = find(node.left, key)
    if found is not None:
        return found
    return find(node.right, key)


# ---------- Binary search tree ----------
# Smaller keys go to the left and bigger keys go to the right
# Example with the orders 4, 2, 6, 1, 3, 5, 7:
#            4
#          /   \
#         2     6
#        / \   / \
#       1   3 5   7


## Function for inserting a key in a binary search tree
## It goes down comparing: smaller to the left, bigger to the right,
## until it finds an empty place
## @params: node, key, value
## @return: the root of the tree
def insert(node, key, value):
    # Empty place found: the new node goes here
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
## It only goes down one side each time, so it does not visit all the nodes
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
    # Always go to the left until there is no left child
    while node.left is not None:
        node = node.left
    return node


## Function for deleting a key from a binary search tree
## First it looks for the node like search(), then it removes it (3 cases)
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
        # (the child, or None, takes the place of the node)
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        # Case 3: the node has two children,
        # it is replaced by the smallest node of the right side
        successor = minimum(node.right)
        node.key = successor.key
        node.value = successor.value
        # The successor is removed from its old place
        node.right = delete(node.right, successor.key)
    return node
