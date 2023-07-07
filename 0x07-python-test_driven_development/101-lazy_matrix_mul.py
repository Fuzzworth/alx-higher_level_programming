#!/usr/bin/python3
"""
Module that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Raises:
        TypeError: Errrors raised when matrix not a list of list integers/float
        ValueError: Empty matrix

    Returns:
        list: matrix dot product of m_a and m_b
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
    size_a = len(m_a[0])
    size_b = len(m_b[0])
    for i in range(len(m_a)):
        if len(m_a[i]) != size_a:
            raise TypeError("each row of m_a must be of the same size")
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                if len(m_b[k]) != size_b:
                    raise TypeError("each row of m_b must be of the same size")
                if not isinstance(m_a[i][k], (int, float)):
                    raise TypeError("m_a should contain only " +
                                    "integers or floats")
                if not isinstance(m_b[k][j], (int, float)):
                    raise TypeError("m_b should contain only " +
                                    "integers or floats")
    try:
        result = np.dot(m_a, m_b)
    except Exception:
        ValueError("m_a and m_b can't be multiplied")
    return result
