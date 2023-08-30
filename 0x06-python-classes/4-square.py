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

    @property
    def size(self):
        """Gets the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates the squares area
        Returns: returns the area of the square
        """

        return (self.__size ** 2)
