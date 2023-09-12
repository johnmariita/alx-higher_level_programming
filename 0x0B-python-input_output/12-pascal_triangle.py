#!/usr/bin/python3
""" A module containing pascal triangle definition """


def pascal_triangle(n):
    """
    Function that prints the pascal triangle

    Args:
        n: the number of rows needed

    Returns:
        returns the list containing the pascal triangle
    """
    triangle = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
