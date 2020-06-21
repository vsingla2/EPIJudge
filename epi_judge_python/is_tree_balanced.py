from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# brute force, O(n) time, O(n) space
def is_balanced_binary_tree(tree_root: BinaryTreeNode) -> bool:
    if not tree_root:
        return True

    left_result = is_balanced_binary_tree(tree_root.left)
    if not left_result:
        return False

    right_result = is_balanced_binary_tree(tree_root.right)
    if not right_result:
        return False

    left_height = tree_root.left.height if tree_root.left else 0
    right_height = tree_root.right.height if tree_root.right else 0
    tree_root.height = max(left_height, right_height) + 1

    if abs(left_height - right_height) <= 1:
        return True

    return False


# optimized, O(n) time, O(h) space
def is_balanced_binary_tree_optimized(tree_root: BinaryTreeNode) -> bool:
    def check_balanced(tree):
        if not tree:
            return True, -1

        left_result = check_balanced(tree.left)
        if not left_result[0]:
            return False, 0

        right_result = check_balanced(tree.right)
        if not right_result[0]:
            return False, 0

        is_balanced = abs(left_result[1] - right_result[1]) <= 1
        height = max(left_result[1], right_result[1]) + 1

        return is_balanced, height

    return check_balanced(tree_root)[0]


if __name__ == '__main__':
    generic_test.generic_test_main('is_tree_balanced.py',
                                   'is_tree_balanced.tsv',
                                   is_balanced_binary_tree)

    generic_test.generic_test_main('is_tree_balanced.py',
                                   'is_tree_balanced.tsv',
                                   is_balanced_binary_tree_optimized)
