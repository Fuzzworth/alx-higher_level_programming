#!/usr/bin/python3
"""
Module Docs
"""


def _fp_r(list_of_integers, begin, end):
    """
    Function Docs
    """
    if end - begin < 2:
        return None
    mid = (begin + end) // 2
    if (list_of_integers[mid] >= list_of_integers[mid - 1]
            and list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]
    return (_fp_r(list_of_integers, begin, mid)
            or _fp_r(list_of_integers, mid, end))


def find_peak(list_of_integers):
    """
    Function Docs
    """
    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return _fp_r(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]
