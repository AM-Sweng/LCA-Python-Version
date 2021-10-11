import unittest
from LCA_Python_Version import *

class LCA_Unit_Test(unittest.TestCase):

    def set_up(self):
        pass

    def test_insert(self):
        # Test inserting into an empty tree
        root = insert(None, 'R')
        self.assertEqual(printKeysInOrder(root), "()R()")

        # Test inserting into a tree where the given key should go into the left subtree
        root = insert(root, 'E')
        self.assertEqual(printKeysInOrder(root), "(()E())R()")

        # Test inserting into a tree where the given key should go into the right subtree
        root = insert(root, 'T')
        self.assertEqual(printKeysInOrder(root), "(()E())R(()T())")

        # Test multiple inserts in a row and check if the correct tree is generated
        #
        # The tree used is:
        #
        #                 _____R_____
        #                |           |
        #            ____E____       T____
        #           |         |           |
        #           A__     __H__         X__
        #              |   |     |           |
        #              C   F     P         __Z
        #                                 |
        #                                 Y

        root = insert(root, 'A')
        root = insert(root, 'H')
        root = insert(root, 'F')
        root = insert(root, 'X')
        root = insert(root, 'Z')
        root = insert(root, 'Y')
        root = insert(root, 'P')
        root = insert(root, 'C')
        self.assertEqual(printKeysInOrder(root), "((()A(()C()))E((()F())H(()P())))R(()T(()X((()Y())Z())))")

        # Test inserting a key that is already present
        root = insert(root, 'Z')
        self.assertEqual(printKeysInOrder(root), "((()A(()C()))E((()F())H(()P())))R(()T(()X((()Y())Z())))")

    def test_LCA(self):
        # Test LCA on an empty tree
        self.assertEqual(LCAof(None, 'F', 'J'), None)

        # Test LCA on a tree with one node, where neither given key is in the tree
        root = insert(None, 'D')
        self.assertEqual(LCAof(root, 'H', 'A'), None)

        # Test LCA on a tree with one node, where one of the given keys is in the tree
        self.assertEqual(LCAof(root, 'D', 'F'), None)

        # Tests for LCA on a tree with multiple nodes
        root = None
        root = insert(root, 'G')
        root = insert(root, 'N')
        root = insert(root, 'K')
        root = insert(root, 'E')
        root = insert(root, 'A')
        root = insert(root, 'P')
        root = insert(root, 'J')
        root = insert(root, 'F')
        root = insert(root, 'Z')
        root = insert(root, 'H')
        root = insert(root, 'L')

        # The tree used is:
        #
        #            ________G________
        #           |                 |
        #       ____E____         ____N____
        #      |         |       |         |
        #      A         F     __K__       P__
        #                     |     |         |
        #                   __J     L         Z
        #                  |
        #                  H

        # Test LCA where neither key is in the tree
        self.assertEqual(LCAof(root, 'D', 'M'), None)

        # Test LCA where one of the keys is in the tree
        self.assertEqual(LCAof(root, 'J', 'X'), None)

        # Test LCA with keys that are in the tree at varying levels
        self.assertEqual(LCAof(root, 'A', 'F'), 'E')
        self.assertEqual(LCAof(root, 'H', 'L'), 'K')
        self.assertEqual(LCAof(root, 'J', 'Z'), 'N')
        self.assertEqual(LCAof(root, 'H', 'A'), 'G')

        # Test LCA where one of the given keys is the ancestor of the other
        self.assertEqual(LCAof(root, 'K', 'H'), 'K')

        # Test LCA where the two given keys are the same
        self.assertEqual(LCAof(root, 'J', 'J'), 'J')

if __name__ == '__main__':
    unittest.main()
