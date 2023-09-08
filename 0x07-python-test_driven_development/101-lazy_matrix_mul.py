#!/usr/bin/python3
"""This module contains a function that multiplies two matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies two matrices.
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    """

    return (np.matmul(m_a, m_b))
