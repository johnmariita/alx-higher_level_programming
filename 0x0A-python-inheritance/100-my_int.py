#!/usr/bin/python3
""" Module containing MyInt class """


class MyInt(int):
    """ class definition """
    def __ne__(self, equality):
        """ not equal to equal """
        return super().__eq__(equality)

    def __eq__(self, equality):
        """equal to not equal"""
        return super().__ne__(equality)
