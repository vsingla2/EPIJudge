from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode, lower_bound=float('-inf'), upper_bound=float('inf')) -> bool:
    if not tree:
        return True
    elif not lower_bound <= tree.data <= upper_bound:  # tree is not null and tree.left is not null
        return False
    return (is_binary_tree_bst(tree.left, lower_bound, tree.data) and
            is_binary_tree_bst(tree.right, tree.data, upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
