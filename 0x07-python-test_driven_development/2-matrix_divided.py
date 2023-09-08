#!/usr/bin/python3
""" A module containing a function that divides matrices"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or any([not isinstance(sub, list)
                                            for sub in matrix]):
        raise TypeError("matrix must be a matrix "
                "(list of lists) of integers/floats")
    if not all(isinstance(x, (int, float))
               for sub in matrix for x in sub):
        raise TypeError("matrix must be a matrix "
                "(list of lists) of integers/floats")
    if not all([len(x) == len(matrix[0]) for x in matrix]):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(float(x) / div, 2) for x in sub] for sub in matrix]
