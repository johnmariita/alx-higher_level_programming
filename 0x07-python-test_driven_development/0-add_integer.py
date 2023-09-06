#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Function that sums up two integers

    Args:
        a: the first integer
        b: the second integer that is optional

    Raises:
        TypeError:
            raises a TypeError when the integers are not ints or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(a, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
