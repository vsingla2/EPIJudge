from test_framework.binary_tree_utils import binary_tree_to_string


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None, height=0):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()
