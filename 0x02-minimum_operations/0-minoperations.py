#!/usr/bin/python3
"""
finds miminum number of operations then returns the actual
number if its a prime number
"""


def minOperations(n):
    """
    using recursion to find the minimum number of operations
    as (n) the function to be found
    """
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return minOperations(i) + minOperations(n // i)

    return n
