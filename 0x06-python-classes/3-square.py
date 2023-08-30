#!/usr/bin/python3
"""A module containing a square """


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """
        Initializing the class
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

    def area(self):
        """
        Calculates the squares area
        Returns: returns the area of the square
        """

        return (self.__size ** 2)
