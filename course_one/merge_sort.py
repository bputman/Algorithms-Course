import random
import timeit

import numpy as np


def merge_sort(x):
    """
    Recursively apply merge sort on subsequences of the input array.
    Base case is when array length is equal to 1.

    :param x: the array to sort
    :return: the sorted array
    """
    n = len(x)
    if n == 1:
        return x

    m = n // 2
    return merge(merge_sort(x[:m]), merge_sort(x[m:]))


def merge(a, b):
    """
    Given two sorted arrays, merge the arrays while maintaining sorting.

    :param a: the first sorted array
    :param b: the second sorted array
    :return: the sorted array containing all values from the two input arrays
    """
    a_size, b_size = len(a), len(b)
    c = [0] * (a_size + b_size)
    i, j = 0, 0
    for k in range(len(c)):
        # Check if either input array has run out of elements, if so, add all elements from the remaining array.
        if i == a_size:
            c[k:] = b[j:]
            return c
        elif j == b_size:
            c[k:] = a[i:]
            return c
        # Add the first element from one of the two input arrays, and increment the counter for that array.
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1


if __name__ == "__main__":
    # Simple tests
    x = np.random.randn(121)
    y = merge_sort(x)
    assert all(np.diff(y) >= 0)

    x = [random.randrange(1000) for r in range(1000)]
    y = merge_sort(x)
    assert all(np.diff(y) >= 0)

    # Simple timer
    # Note: Both of these sort algorithms are not-in-place. If it was in-place, make a copy before for every iteration.
    setup = "import numpy as np; from __main__ import merge_sort; x = np.random.random(1000)"
    merge_sort_times = timeit.repeat(setup=setup, stmt="merge_sort(x)", repeat=7, number=1000)
    built_in_sort_times = timeit.repeat(setup=setup, stmt="sorted(x)", repeat=7, number=1000)

    print(f"Native python merge sort - min time: {min(merge_sort_times)}")
    print(f"Built-in sort - min time: {min(built_in_sort_times)}")
