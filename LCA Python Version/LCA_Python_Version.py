
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

def LCAof(root, key1, key2):
    current_node = root
    while current_node is not None:
        if current_node.val > key1 and current_node.val > key2:
            current_node = current_node.left
        elif current_node.val < key1 and current_node.val < key2:
            current_node = current_node.right
        else: return current_node.val
    return None

r = Node('G')
r = insert(r, 'N')
r = insert(r, 'K')
r = insert(r, 'E')
r = insert(r, 'A')
r = insert(r, 'P')
r = insert(r, 'J')
r = insert(r, 'F')
r = insert(r, 'Z')
r = insert(r, 'H')
r = insert(r, 'L')

#             G
#           /   \
#          /     \
#         E       N
#        / \     / \
#       A   F   K   P
#              / \   \
#             J   L   Z
#            /
#           H


print("The LCA of A and F is " + LCAof(r, 'A', 'F')) # Should be E
print("The LCA of H and L is " + LCAof(r, 'H', 'L')) # Should be K
print("The LCA of J and Z is " + LCAof(r, 'J', 'Z')) # Should be N
print("The LCA of E and P is " + LCAof(r, 'E', 'P')) # Should be G