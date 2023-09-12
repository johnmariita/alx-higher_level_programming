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

    def to_json(self):
        """
        Function that retrieves a dictionary representation
        of a Student instance
        """
        return self.__dict__
