#!/usr/bin/python3
"""
Module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
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

    result = []
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            result.append([0] * len(m_b[0]))
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
