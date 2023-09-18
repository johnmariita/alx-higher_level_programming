#!/usr/bin/python3
""" A module containing the rectangle class model """


from models.base import Base


class Rectangle(Base):
    """ class definition """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class instantiation

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
            x: the horizontal offset
            y: vertical offset

        Raises:
            TypeError: when any of the arguments is not an int
            ValueError: when width/height <= 0 or when x/y < 0
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter

        Args:
            value: the value we're setting our attribute to

        Raises:
            ValueError: when the value == 0
            TypeError: when the value is not an ineger
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ Getter to access the height. """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter

        Args:
            value: the value we're setting our attribute to

        Raises:
            ValueError: when the value == 0
            TypeError: when the value is not an ineger
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ Getter to access x. """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter

        Args:
            value: the value we're setting our attribute to

        Raises:
            ValueError: when the value < 0
            TypeError: when the value is not an ineger
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be > 0')
        self.__x = value

    @property
    def y(self):
        """ Getter to access y. """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter

        Args:
            value: the value we're setting our attribute to

        Raises:
            ValueError: when the value < 0
            TypeError: when the value is not an ineger
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be > 0')
        self.__y = value

    def area(self):
        """
        calculates the area of the rectangle

        Returns:
            returns the area of the triangle
        """
        return self.__height * self.__width

    def display(self):
        """
        function to display the rectangle
        """
        for v in range(self.__y):
            print("")
        for i in range(self.__height):
            for h in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ returns the string representation of an instance """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ Function to update the instance attributes """
        attrs = ['self.id', 'self.width', 'self.height', 'self.x', 'self.y']
        for i in range(len(args)):
            exec(f"{attrs[i]} = {args[i]}")
        if not args:
            for arg, val in kwargs.items():
                exec(f"self.{arg} = {val}")

    def to_dictionary(self):
        """ returns a dictionary representation of an instance """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
