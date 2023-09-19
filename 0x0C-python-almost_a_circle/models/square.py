#!/usr/bin/python3
""" A module containing the class Square definition """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Definition of the square class """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter to access the size """
        return self.__width

    @size.setter
    def size(self, value):
        """
        function to set the size

        Args:
            value: the new size
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    def __str__(self):
        """
        function to return the string representation of an instance
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        function to update the attributes
        """
        attrs = ["id", "size", "x", "y"]
        for i in range(len(args)):
            exec(f"self.{attrs[i]} = {args[i]}")
        if not args:
            for arg, val in kwargs.items():
                exec(f"self.{arg} = {val}")

    def to_dictionary(self):
        """ function to return the dict representation of a class """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
