import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(rotate_amount: int, A: List[int]) -> None:
    # O(n) time, O(1) space
    if len(A) > 1:
        n = len(A)
        rotate_amount %= n  # take care of large numbers
        if rotate_amount < 0:  # take care of negative numbers
            rotate_amount += n
        reverse_array(A, 0, n - 1)
        reverse_array(A, 0, rotate_amount - 1)
        reverse_array(A, rotate_amount, n - 1)
    return


def reverse_array(array_input, i, j):
    while i < j:
        array_input[i], array_input[j] = array_input[j], array_input[i]
        i += 1
        j -= 1


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rotate_array.py', 'rotate_array.tsv',
                                       rotate_array_wrapper))
