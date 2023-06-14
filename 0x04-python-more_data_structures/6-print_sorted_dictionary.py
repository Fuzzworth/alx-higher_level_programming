#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b_dictionary = {x: a_dictionary.get(x) for x in list(a_dictionary).sort()}
