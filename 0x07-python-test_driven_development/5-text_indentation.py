#!/usr/bin/python3
""" Text Indentation """


def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: the strig

    Raises:
        TypeError: raised if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        if text[i] != ":" and text[i] != "." and text[i] != "?":
            print(text[i], end="")
            i += 1
        else:
            print(text[i], end="")
            print("")
            print("")
            i += 1
            while i < len(text):
                if text[i] == " ":
                    i += 1
                else:
                    break
            continue
