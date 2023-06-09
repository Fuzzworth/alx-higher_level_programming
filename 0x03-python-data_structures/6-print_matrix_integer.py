#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for array in range(len(matrix)):
        for element in range(len(array)):
            if element != (len(array) - 1):
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element), end="\n")
