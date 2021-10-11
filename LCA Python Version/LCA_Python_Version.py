
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Checks if the tree rooted at this node contains the given key
def contains(node, key):
    if node is None:
        return False
    if node.val == key:
        return True
    elif key < node.val:
        return contains(node.left, key)
    else:
        return contains(node.right, key)

def LCAof(root, key1, key2):
    if contains(root, key1) and contains(root, key2):
        current_node = root
        while current_node is not None:
            if current_node.val > key1 and current_node.val > key2:
                current_node = current_node.left
            elif current_node.val < key1 and current_node.val < key2:
                current_node = current_node.right
            else: return current_node.val
    return None

def printKeysInOrder(node):
    if node is None:
        return ""
    return "(" + printKeysInOrder(node.left) + ")" + node.val + "(" + printKeysInOrder(node.right) + ")"
