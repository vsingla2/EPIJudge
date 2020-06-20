from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    keys = set(A)  # O(n) space
    for num in A:  # O(n) time
        if t - num in keys:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
