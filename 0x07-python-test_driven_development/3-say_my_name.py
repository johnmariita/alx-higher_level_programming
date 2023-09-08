#!/usr/bin/python3
"""A module containing the say my name function"""


def say_my_name(first_name, last_name=""):
    """
    Function that says a name

    Args:
        first_name: the first name
        last_name: the last name

    Raises:
        TypeError: raises a TypeError if either the first name
                    or last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"my name is {first_name} {last_name}")
