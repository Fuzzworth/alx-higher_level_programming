#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary).sort()
    print(keys)
    b_dictionary = {x: a_dictionary.get(x) for x in keys}
