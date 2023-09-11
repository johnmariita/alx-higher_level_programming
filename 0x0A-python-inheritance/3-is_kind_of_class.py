#!/usr/bin/python3
""" Module containing the is_kind_of_class function definition"""


def is_kind_of_class(obj, a_class):
    """
    function that checks if an object is a subclass or an instance

    Args:
        obj: the instance or subclass
        a_class: the class or superclass

    Return:
        returns True or False
    """
    try:
        if issubclass(obj, a_class):
            return True
        else:
            return False
    except TypeError:
        pass
    if isinstance(obj, a_class):
        return True
    else:
        return False
