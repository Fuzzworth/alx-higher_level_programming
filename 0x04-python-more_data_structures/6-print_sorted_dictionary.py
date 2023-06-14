#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    print(keys)
    for i in keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
