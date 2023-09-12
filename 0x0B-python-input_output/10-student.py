#!/usr/bin/python3
""" A module containing student class """


class Student:
    """ Definition of a class """
    def __init__(self, first_name, last_name, age):
        """
        instantiation of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that retrieves a dictionary representation
        of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            d = {}
            for i in attrs:
                if i in self.__dict__:
                    d.update({i: self.__dict__[i]})
            return d
