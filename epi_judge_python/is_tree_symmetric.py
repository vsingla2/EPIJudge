from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def check_symmetric(left_tree, right_tree):
    if not left_tree and not right_tree:
        return True
    elif left_tree and right_tree:
        return left_tree.data == right_tree.data and \
               check_symmetric(left_tree.left, right_tree.right) and \
               check_symmetric(left_tree.right, right_tree.left)
    return False


def is_symmetric_optimized(tree: BinaryTreeNode) -> bool:
    return check_symmetric(tree, tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric_optimized))
