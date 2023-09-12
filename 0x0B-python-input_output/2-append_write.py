#!/usr/bin/python3
""" A module contaning an append to file function"""


def append_write(filename="", text=""):
    """
    Function that appends text to a file

    Args:
        filename: the name of the file
        text: the text to be appended

    Returns:
        returns the number of characters appended
    """
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
