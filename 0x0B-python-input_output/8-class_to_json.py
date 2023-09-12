#!/usr/bin/python3
""" A module containing the class to json function """


def class_to_json(obj):
    """
    Function that returns the json of a class

    Args:
        obj: the class
    """
    return obj.__dict__
