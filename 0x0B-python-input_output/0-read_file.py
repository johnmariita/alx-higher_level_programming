#!/usr/bin/python3
""" Module containing the definition of a reading file function """


def read_file(filename=""):
    """
    function that reads a file

    Args:
        filename: the name of the file to be read
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
