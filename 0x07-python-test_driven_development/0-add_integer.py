#!/usr/bin/python3
"""
Addition Module
"""


def add_integer(a, b=98):
    """
    Function to add two integers or floats

    Args:
        a (number): Float or Number
        b (:obj:number:optional): Optional Float or Integer

    Raises:
        TypeError: If not float or integer

    Returns:
        float:int: Integer or float
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
