#!/usr/bin/python3
""" Module containing MyList class"""


class MyList(list):
    """ a list subclass. """

    def print_sorted(self):
        """A method that prints the list sorted"""
        print(sorted(self))
