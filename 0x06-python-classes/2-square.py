#!/usr/bin/python3
"""Module containing the square """


class Square:
    """A square class"""

    def __init__(self, size=0):
        """
        Initializing this square class
        Args:
            size: the size of the square
        Raises:
            ValueError: less than zero size
            TypeError: non-integer size
        """

        if size < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        self.__size = size
