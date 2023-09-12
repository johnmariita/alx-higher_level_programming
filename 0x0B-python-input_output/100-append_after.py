#!/usr/bin/python3
""" A module containing a function """


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a new line new_string
    in cases where a line has the search_string

    Args:
        filename: the name o the file
        search_string: the string we're looking for
        new_string: the string to be inserted
    """
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)  # Reset file position to the beginning
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
