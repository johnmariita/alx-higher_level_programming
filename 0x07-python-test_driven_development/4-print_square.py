#!/usr/bin/python3
"""A module containing a function that prints a square"""


def print_square(size):
    """
    Function that prints a square

    Args:
        size: the size of the square
    Raises:
        TypeError: when the size is of any other type apart from an int
        ValueError: when the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print("")
