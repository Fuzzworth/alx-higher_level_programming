#!/usr/bin/python3
"""
module doc
"""


def pascal_triangle(n):
    """
    function docs
    """
    final_list = []
    if n <= 0:
        return final_list
    for i in range(n):
        new_row = []
        num = 1
        for j in range(i+1):
            num = num * (i - j) // j
            new_row.append(num)
        final_list.append(new_row)
