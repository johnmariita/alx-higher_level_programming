#!/usr/bin/python3
""" A module containing a write to a file function """


def write_file(filename="", text=""):
    """
    Function that writes to a file

    Args:
        filename: the name of the file
        text: the text to be written to the file

    Returns:
        returns the number of characters written
    """
    with open(filename, "w") as f:
        f.write(text)
        return len(text)
